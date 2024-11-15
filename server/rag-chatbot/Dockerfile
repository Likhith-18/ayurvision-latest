FROM python:3.9-slim

WORKDIR /app

RUN pip install --upgrade pip && pip install uv

COPY requirements.txt ./

RUN uv venv && . .venv/bin/activate

RUN uv pip install -r requirements.txt

COPY . .

EXPOSE 8000:8000

CMD ["/bin/bash", "-c", "source .venv/bin/activate && chainlit run -h app.py"]
