FROM python:3.12
ADD . /src
RUN pip install kopf
RUN pip install kubernetes
CMD kopf run /src/handlers.py --verbose