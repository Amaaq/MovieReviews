FROM node:20.12.0-alpine

RUN npm install -g http-server

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

EXPOSE 3000

CMD [ "http-server", "dist", "-a", "0.0.0.0", "-p", "3000" ]