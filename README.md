# Criando uma função Lambda através de uma imagem Docker

## 1. Acessar a AWS e criar um repositório no Amazon ECR

Acesse o [Amazon Elastic Container Registry (ECR)](https://console.aws.amazon.com/ecr/) e crie um novo repositório.

## 2. Criar a imagem Docker que será enviada para o ECR

Você pode seguir o exemplo de `Dockerfile` fornecido pela AWS neste link:  
[https://gallery.ecr.aws/lambda/python](https://gallery.ecr.aws/lambda/python)

### Estrutura do seu projeto

Como ficou o meu Dockerfile:

```dockerfile
FROM public.ecr.aws/lambda/python:3.11

# Copia os arquivos da pasta "files" para o contêiner
COPY files/ ${LAMBDA_TASK_ROOT}/

# Define o diretório de trabalho
WORKDIR ${LAMBDA_TASK_ROOT}

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Define o handler (arquivo app.py, função lambda_handler)
CMD ["app.lambda_handler"]
```

Minha organização de arquivos:

```
.
├── Dockerfile
└── files
    ├── app.py
    └── requirements.txt
```

- O arquivo `app.py` deve conter uma função chamada `lambda_handler`, que será o ponto de entrada da Lambda.

## 3. Criar a imagem Docker

Navegue até a pasta do projeto e execute o comando abaixo para criar a imagem:

```bash
docker build -t lambda_function .
```

## 4. Fazer push da imagem para o ECR

Após criar a imagem, acesse seu repositório no Amazon ECR e clique em **"Visualizar comandos de push"** para obter as instruções completas.

⚠️ **Importante:** Certifique-se de usar o mesmo nome `lambda_function` ao criar a imagem. Caso contrário, será necessário ajustar os comandos fornecidos pela AWS.

## 5. Criar a função Lambda com imagem Docker

Na AWS Lambda, crie uma nova função escolhendo a opção de **imagem de contêiner**.

- Se o seu código depender de arquivos adicionais, como modelos treinados ou pipelines, você pode armazená-los no S3, que foi como eu fiz. Se necessário, atribua uma role com permissão de leitura no S3 para que a Lambda possa acessar esses arquivos.

## 6. Configurações adicionais

Algumas bibliotecas como `scikit-learn`, `pandas` e `joblib` aumentam o tempo de inicialização da função. Para evitar erros de timeout, vá até:

> Aba **Configuração** → Seção **Configuração geral** → Aumente o tempo limite (**Timeout**)
