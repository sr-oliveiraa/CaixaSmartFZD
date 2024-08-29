# Usar uma imagem base do Python
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instalar as dependências da aplicação
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante dos arquivos da aplicação para o diretório de trabalho
COPY . .

# Expor a porta que a aplicação Flask usará
EXPOSE 5000

# Definir a variável de ambiente para desabilitar buffers para o log
ENV PYTHONUNBUFFERED=1

# Comando para rodar a aplicação
CMD ["python", "app.py"]
