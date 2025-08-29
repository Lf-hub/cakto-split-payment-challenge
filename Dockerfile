FROM python:3.11-slim

WORKDIR /app

# Instalar pacotes necessários para compilar algumas dependências
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libpq-dev \
    libffi-dev \
    libbz2-dev \
    liblzma-dev \
    libssl-dev \
    libreadline-dev \
    zlib1g-dev \
    libsqlite3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["bash", "-c", "python src/manage.py migrate && python src/manage.py runserver 0.0.0.0:8000"]
