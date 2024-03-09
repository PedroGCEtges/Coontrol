    FROM python:3.10-slim

    WORKDIR /app

    RUN apt-get update && apt-get install -y libx11-6  x11-apps xauth libxrender1 libxext-dev libxrender-dev libxinerama-dev libxi-dev libxrandr-dev libxcursor-dev libxtst-dev tk-dev && rm -rf /var/lib/apt/lists/*
    COPY . .

    RUN pip install -r requirements.txt

    CMD ["python", "main.py"]

