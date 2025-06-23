FROM public.ecr.aws/lambda/python:3.12

COPY files ${LAMBDA_TASK_ROOT}

WORKDIR ${LAMBDA_TASK_ROOT}

RUN pip install --no-cache-dir -r requirements.txt 

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.lambda_handler" ]