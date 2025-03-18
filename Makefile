########################################################################################################################

# Setup virtual environment
ENV_NAME := $(shell echo $(notdir $(CURDIR)) | sed 's/^[0-9]*-//' | tr '[:upper:]' '[:lower:]')

.PHONY : setup, create-venv, install-requirements
setup : create-venv install-requirements

create-venv:
	@if ! pyenv virtualenvs | grep -q $(ENV_NAME); then pyenv virtualenv 3.10.12 $(ENV_NAME); \
	else echo "virtualenv already exists"; fi
	# Set virtualenv as local
	@pyenv local $(ENV_NAME)
	@echo "✅ Virtualenv $(ENV_NAME) created and set as local"

install-requirements:
	@pip install --upgrade pip --quiet
	@pip install -e . 
	@pip install -r requirements.txt 
	@echo "✅ Requirements installed"


########################################################################################################################


test_api : 
	@curl -X 'POST' \
  'http://127.0.0.1:8080/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' -d '{ "PULocationID": 1,"DOLocationID": 1,"passenger_count": 1}'

########################################################################################################################

### STRIP_START ###
.PHONY: docker_build docker_run docker_push gcp_build deploy

docker_build:
	docker build -t ${IMAGE} . --file Dockerfile-flask

docker_run: 
	docker run -e PORT=${PORT} -p ${PORT}:${PORT} ${IMAGE}

gcp_build:
	docker build -t ${LOCATION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY}/${IMAGE}:latest . --file Dockerfile-flask

run_local_gcp:
	docker run -e PORT=${PORT} -p ${PORT}:${PORT} ${LOCATION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY}/${IMAGE}:latest

docker_push:
	docker push ${LOCATION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY}/${IMAGE}:latest

gcloud_auth:
	gcloud auth configure-docker ${LOCATION}-docker.pkg.dev

deploy_service:
	gcloud run deploy ${IMAGE} --image=${LOCATION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY}/${IMAGE}:latest \
  --platform=managed --region=${LOCATION_DETAIL} --allow-unauthenticated