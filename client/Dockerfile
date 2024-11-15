FROM node:18-alpine

WORKDIR /app

RUN npm install -g pnpm

ENV PNPM_HOME=/pnpm-global
ENV PATH=$PNPM_HOME:$PATH

COPY package.json pnpm-lock.yaml ./

RUN pnpm install

COPY . .

EXPOSE 5173:5173

CMD ["pnpm","run","dev"]
