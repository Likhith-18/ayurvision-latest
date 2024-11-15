# # FROM python:3.9-slim

# # # Install Node.js
# # RUN apt-get update && apt-get install -y --no-install-recommends curl && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && apt-get install -y --no-install-recommends nodejs && apt-get clean && rm -rf /var/lib/apt/lists/*

# # COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# # WORKDIR /app

# # COPY /rag-chatbot/requirements.txt .

# # RUN uv venv

# # ENV VIRTUAL_ENV=/app/.venv
# # ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# # RUN uv pip install --system -r requirements.txt

# # COPY . /app/

# # RUN npm install
# # # Verify installations
# # RUN which python && which pip && which node && which npm && which chainlit

# # CMD ["node","index.js"]

# FROM nikolaik/python-nodejs:python3.9-nodejs23-slim

# WORKDIR /app

# COPY package*.json ./

# COPY requirements.txt ./app

# RUN npm install --only=production

# RUN uv venv /app/.venv
# RUN uv pip install --no-cache-dir -r /app/requirements.txt

# ENV PATH="/app/.venv/bin:$PATH"

# COPY . /app

# EXPOSE 3000:3000

# EXPOSE 8000:8000

# RUN . /app/.venv/bin/activate && which chainlit

# CMD [ "/bin/sh","-c",". /app/.venv/bin/activate && chainlit run -h ./app/rag-chatbot/app.py && npm start" ]

# # FROM nikolaik/python-nodejs:python3.9-nodejs23-slim

# # WORKDIR /app

# # COPY package*.json ./
# # COPY requirements.txt ./

# # RUN npm install --only=production

# # RUN uv venv /app/.venv && . /app/.venv/bin/activate
# # RUN uv pip install --no-cache-dir -r requirements.txt

# # ENV PATH="/app/.venv/bin:$PATH"

# # COPY . .

# # EXPOSE 3000
# # EXPOSE 8000

# # CMD ["/bin/sh", "-c", ". /app/.venv/bin/activate && chainlit run -h ./rag-chatbot/app.py && npm start"]

FROM nikolaik/python-nodejs:python3.9-nodejs23-slim

WORKDIR /app

COPY ./rag-chatbot/requirements.txt ./rag-chatbot/

COPY /rag-chatbot/.env ./rag-chatbot/
COPY package*.json ./

RUN npm install

RUN uv venv /app/.venv
RUN uv pip install --no-cache-dir -r ./rag-chatbot/requirements.txt

COPY . .

COPY start.sh ./
RUN chmod +x start.sh

EXPOSE 3000

EXPOSE 8000

CMD [ "./start.sh"]
