FROM node:alpine

RUN npm install express

WORKDIR /app

COPY app/ .

CMD ["node", "random_gen.js"]