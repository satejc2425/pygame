FROM python:3.11-slim
WORKDIR /app
COPY game.py /app
CMD ["python" , "game.py"]
