FROM python:3-slim-bullseye

WORKDIR /app

RUN apt update && apt install -y build-essential libpoppler-cpp-dev pkg-config python3-dev && rm -rf /var/lib/apt/lists/*
RUN pip install pdftotext
COPY pdfreader.py /app

ENTRYPOINT ["python3", "/app/pdfreader.py"]