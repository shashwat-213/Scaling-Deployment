FROM python:3.12
ADD handlers.py .
RUN pip install kopf
RUN pip install kubernetes
CMD kopf run handlers.py --verbose