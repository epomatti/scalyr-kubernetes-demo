# Scalyr-Kubernetes Demo

## Minikube


### 1 - Install Scalyr Helm Chart

Start Minikube: `minikube start`

The [recommended method](https://app.scalyr.com/help/install-agent-kubernetes-helm) is using the official [Helm chart](https://github.com/scalyr/helm-scalyr):

```sh
# Create or copy your API Key from the Scalyr portal
apikey='<API KEY>'

helm install '<release>' scalyr-agent --set scalyr.apiKey=$apikey --repo 'https://scalyr.github.io/helm-scalyr/' --wait
```

### 2 - Docker Image Cache

Builde the image locally:

```sh
# Build the image locally
docker build --tag scalyr-demo .

# Add to Minikube cache (takes a minute)
minikube image load scalyr-demo
```

### 3 - Kubernetes Deploy

```sh
# Root manifest
kubectl apply -f .

# To access it, open a tunnel in Minikube
minikube tunnel
```

## Local Development

To run and make change to the local application:

```sh
# In-project pipenv dependencies
mkdir .venv

# Ubuntu 22 ad-hoc fix for https://github.com/pypa/setuptools/issues/3278
export SETUPTOOLS_USE_DISTUTILS=stdlib

# Get the dependencies
pipenv install --dev
pipenv shell

# Flask Env
cp config/dev.flaskenv .flaskenv

# Running locally
python3 -m flask run
```