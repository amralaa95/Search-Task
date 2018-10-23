FROM ubuntu:16.04
RUN apt-get update && \
  apt-get install -y nodejs && \
  apt-get install -y npm && \
  apt-get clean && \
  rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*
RUN npm install -g localtunnel
RUN npm install -g @angular/cli
FROM python:3.6
ENV PYTHONUNBUFFERED 1
ENV CONSUMER_KEY 'DAJxuF8xaRVkx48CaZLIK65Zh'
ENV CONSUMER_SECRET '6h3bCLNPkusVCyF4WhRPBMfxQJoYEvaOuyd7Lj6AsIQG6Zbi6x'
ENV ACCESS_TOKEN '979516170255642626-mJcvmpmI0nxR1oZD2amfKIXAit9HV5j'
ENV ACCESS_TOKEN_SECRET 'AwzXXO91l1oEWcP4hHrmRMML9F1o7jLYR0iXik2jXY95G'
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt
ADD . /code/

