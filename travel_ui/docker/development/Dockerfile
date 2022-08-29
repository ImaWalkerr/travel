FROM node:17.6-slim

WORKDIR /home/nodeuser/app

COPY ./package*.json ./

RUN yarn install

COPY . ./
