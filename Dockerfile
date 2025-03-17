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

EXPOSE 5042

# Run the application
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "5042", "--reload"]