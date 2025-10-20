# syntax=docker/dockerfile:1
FROM python:3.11-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip wheel -r requirements.txt --wheel-dir /wheels

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /wheels /wheels
RUN pip install --no-index --find-links=/wheels -r requirements.txt
COPY app ./app
COPY model ./model
ENV PYTHONUNBUFFERED=1
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost:8000/health || exit 1
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
