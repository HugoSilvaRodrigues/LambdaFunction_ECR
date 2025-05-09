FROM public.ecr.aws/lambda/python:3.11

# Copia os arquivos da pasta "files" para o contêiner
COPY files/ ${LAMBDA_TASK_ROOT}/

# Define o diretório de trabalho
WORKDIR ${LAMBDA_TASK_ROOT}

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Define o handler (arquivo app.py, função lambda_handler)
CMD ["app.lambda_handler"]
