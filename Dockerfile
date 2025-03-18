FROM python:3.10-slim

# Set the working directory in the container
WORKDIR  /yellowcab_app

# Install the dependencies
COPY requirements.txt /yellowcab_app/requirements.txt
RUN pip install --upgrade pip

COPY yellowcab /yellowcab_app/yellowcab
COPY api.py /yellowcab_app/api.py
COPY setup.py /yellowcab_app/

RUN pip install -r requirements.txt

EXPOSE $PORT

# Command to run on container start
#docker run -e PORT=8002 -p 8002:8002 yellowcab:latest   
CMD uvicorn api:app --host 0.0.0.0 --port $PORT 