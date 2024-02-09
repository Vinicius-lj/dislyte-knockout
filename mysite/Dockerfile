# Base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copia os arquivos requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Copy the application files into the working directory
COPY . /app

# Install the application dependencies
RUN pip install -r requirements.txt

# Expõe a porta 8000 para o servidor web do Django
EXPOSE 8000

# Define the entry point for the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--insecure"]