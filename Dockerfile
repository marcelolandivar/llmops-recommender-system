FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8

WORKDIR /llm-app

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY . .


RUN pip install --upgrade pip
RUN pip install --no-cache-dir -e .

EXPOSE 8501

CMD ["streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]
