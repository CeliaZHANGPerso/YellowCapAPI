# YellowCapAPI

To deploy a docker container on GCP (Makefile is so important):
1. local test on your computer or your VM that it works
2. create a artifact registry repository
3. follow the make file (all variables are saved in .env, using direnv)
  1) make gcp_build
  2) make run_local_gcp (test if it works well)
  3) if your account is not authentified, do:
    gcloud auth configure-docker $LOCATION-docker.pkg.dev
  4) make docker_push
  5) make deploy_service
Then you can see your image in Artifact Registry and your api in Cloud Run.