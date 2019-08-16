FROM python:3.7

ARG project_dir=/home/jovyan
WORKDIR $project_dir

FROM jjanzic/docker-python3-opencv

# https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#core-stacks
FROM jupyter/scipy-notebook:latest

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
