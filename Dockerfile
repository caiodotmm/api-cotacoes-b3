# Dockerfile
FROM python:3.11-slim

# Recebe os IDs do host como argumentos
ARG USER_ID
ARG GROUP_ID

# Cria usuário/grupo com IDs idênticos aos do host
RUN groupadd -g $GROUP_ID appgroup && \
    useradd -u $USER_ID -g appgroup -s /bin/bash appuser

# Define o diretório de trabalho
WORKDIR /app
RUN chown -R appuser:appgroup /app

# Copia os arquivos de dependências
COPY requirements.txt .

# Instala dependências
USER root
COPY --chown=appuser:appgroup requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
USER appuser
COPY --chown=appuser:appgroup . .

# Expõe a porta da aplicação
EXPOSE 8000

# Comando para rodar a API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
