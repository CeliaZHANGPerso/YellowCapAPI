FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
#RUN pip install -r requirements.txt

COPY yellowcab/src/. /app/yellowcab/src
COPY yellowcab/model/. /app/yellowcab/model
COPY api.py /app/api.py
COPY setup.py /app/setup.py

RUN pip install .

EXPOSE 8002

CMD [ "uvicorn", "api:app", "--host", "0.0.0.0",  "--port", "8002",  "--reload"]