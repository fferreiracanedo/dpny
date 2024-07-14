from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from pessoa.models import Pessoa
from avaliacao_desempenho.managers import AvaliacaoDesempenhoManager
from django.db.models import Avg


class AvaliacaoDesempenho(models.Model):
	OPCOES_TIPO_AVALIACAO = (
		('autoavaliacao', 'Autoavaliação'),
		('gestor', 'Gestor'),
		('subordinado', 'Subordinado'),
		('par', 'Par'),
	)

	OPCOES_RESPOSTA_POTENCIAL = (
		('NA', 'NA / Avaliação não apropriada no momento (menos de 6 meses na empresa)'),
		('R-', 'R- / Não satisfatório, devendo ser fruto de análise para atividade de menor complexidade ou desligamento'),
		('R', 'R / Situação estável'),
		('R+', 'R+ / Capacidade para crescimento horizontal, atividades mais complexas'),
		('AP', 'AP / Potencial para crescimento vertical'),
	)

	OPCOES_RESULTADO_COMITE = (
		('TRA', 'Transição'),
		('ATI', 'Atenção Imediata'),
		('DES', 'Em Desenvolvimento'),
		('EST', 'Estável'),
		('CON', 'Consistente'),
		('SUC', 'Sucessor'),
	)

	pessoa = models.ForeignKey(
		Pessoa,
		on_delete=models.CASCADE,
		verbose_name="Pessoa"
	)

	respondida = models.BooleanField(
		verbose_name="Avaliação Respondida",
		default=False
	)
	
	avaliador = models.ForeignKey(
		User,
		on_delete=models.SET_NULL,
		blank=True,
		null=True
	)

	data = models.DateField(
		verbose_name="Data",
		blank=True, null=True
	)

	nota_meta = models.DecimalField(
		verbose_name="Nota de Meta",
		max_digits=5,
		decimal_places=2,
		blank=True, null=True
	)

	nota_potencial = models.DecimalField(
		verbose_name="Nota de Potencial",
		max_digits=5,
		decimal_places=2,
		blank=True, null=True
	)

	resposta_potencial = models.CharField(
		verbose_name="Resposta de Potencial",
		max_length=2,
		choices=OPCOES_RESPOSTA_POTENCIAL,
		blank=True, null=True
	)

	resultado_comite = models.CharField(
		verbose_name="Resultado Comitê",
		max_length=3,
		choices=OPCOES_RESULTADO_COMITE,
		blank=True, null=True
	)

	tipo_avaliacao = models.CharField(
		verbose_name="Tipo de Avaliação",
		max_length=15,
		null=True,
		choices=OPCOES_TIPO_AVALIACAO
	)

	comentario = models.TextField(
		verbose_name="Comentários",
		blank=True, null=True
	)

	data_criacao = models.DateTimeField(
		verbose_name="Data de Criação",
		default=datetime.now
	)

	objects = AvaliacaoDesempenhoManager()

	@property
	def quantidade_competencias_eixo_pessoas(self):
		from .item_competencia import ItemCompetencia

		competencias = ItemCompetencia.objects.filter(
			avaliacao_desempenho=self,
			competencia__tipo='P'
		).count()

		return competencias
	
	@property
	def quantidade_competencias_eixo_negocios(self):
		from .item_competencia import ItemCompetencia

		competencias = ItemCompetencia.objects.filter(
			avaliacao_desempenho=self,
			competencia__tipo='N'
		).count()

		return competencias
	
	@property
	def nota_competencias(self):
		media_competencias = self.itemcompetencia_set.aggregate(Avg('nota'))['nota__avg']
		return round(media_competencias, 2) if media_competencias else None
	
	@property
	def nota_competencias_geral(self):
		from .item_competencia import ItemCompetencia
		media_competencias = ItemCompetencia.objects.filter(
			avaliacao_desempenho__pessoa=self.pessoa,
			avaliacao_desempenho__respondida=True
		).aggregate(Avg('nota'))['nota__avg']
		return round(media_competencias, 2) if media_competencias else 0
	
	@property
	def nota_metas(self):
		soma_metas = 0
		for meta in self.itemmeta_set.all():
			soma_metas += meta.resultado
		
		try:
			return round(soma_metas / len(self.itemmeta_set.all()), 2)
		except:
			return None
	
	def calcular_quadrante(self):
		print("Calculando quadrante")
		nota_geral = self.nota_competencias_geral
		print(nota_geral)
		resultado_comite = ''
		if nota_geral:
			if nota_geral == 0:
				resultado_comite = 'TRA'
			elif nota_geral >= 1 and nota_geral <= 25:
				resultado_comite = 'ATI'
			elif nota_geral >= 26 and nota_geral <= 50:
				resultado_comite = 'DES'
			elif nota_geral >= 51 and nota_geral <= 75:
				resultado_comite = 'EST'
			elif nota_geral >= 76 and nota_geral <= 89:
				resultado_comite = 'CON'
			elif nota_geral >= 90 and nota_geral <= 100:
				resultado_comite = 'SUC'
		else:
			resultado_comite = ''
		
		print(resultado_comite)
		if self.resultado_comite != resultado_comite:
			self.resultado_comite = resultado_comite
			self.save()
		

	'''
	def save(self, *args, **kwargs):
		if self.resultado_comite == None and self.respondida:
			if self.resposta_potencial == 'NA':
				self.resultado_comite = ''
			elif self.resposta_potencial == 'R-':
				self.resultado_comite = 'DES'
			elif self.resposta_potencial == 'R':
				self.resultado_comite = 'EST'
			elif self.resposta_potencial == 'R+':
				self.resultado_comite = 'CON'
			elif self.resposta_potencial == 'AP':
				self.resultado_comite = 'SUC'
		
		super(AvaliacaoDesempenho, self).save(*args, **kwargs)
	'''
	def save(self, *args, **kwargs):
		if self.pk:
			cls = self.__class__
			old = cls.objects.get(pk=self.pk)
			new = self

			changed_fields = []

			for field in cls._meta.get_fields():
				field_name = field.name
				try:
					if getattr(old, field_name) != getattr(new, field_name):
						changed_fields.append(field_name)
				except Exception as ex:
					pass
			kwargs['update_fields'] = changed_fields
		
		super(AvaliacaoDesempenho, self).save(*args, **kwargs)

	def __str__(self):
		return "{} - {}".format(self.id, self.pessoa.nome)

	class Meta:
		app_label = "avaliacao_desempenho"
		verbose_name = "Avaliação de Desempenho"
		verbose_name_plural = "Avaliações de Desempenho"