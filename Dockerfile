# Use uma imagem oficial do Python como imagem pai
FROM python:3.6-slim

# Definir o diretório de trabalho no container
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instalar gcc e outras dependências necessárias
RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y \
    gcc \
    libc6-dev \
    libxml2 \
    libxml2-dev

# Instalar as dependências
# Copie o arquivo requirements.txt do diretório atual para o container em /app
COPY requirements-dev.txt /app/

# Instale quaisquer dependências necessárias
RUN pip install --no-cache-dir -r requirements-dev.txt

# Copie o restante dos arquivos do projeto para o container em /app
COPY . /app/

# Faça as migrações do banco de dados, colete arquivos estáticos, etc.
RUN python manage.py migrate
RUN python manage.py collectstatic --no-input

# Informe ao Docker que o container está ouvindo na porta 8000
EXPOSE 8000

# Execute o servidor de aplicação web ao iniciar o container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
