# Kubernetes Auto-Scaling App

This project demonstrates Kubernetes Horizontal Pod Autoscaler (HPA) in action using a simple Flask app that simulates CPU load.

## Stack
- Python Flask
- Docker
- Kubernetes (HPA, Metrics Server)

##  Getting Started

### 1. Build and Push Docker Image

docker build -t <your-dockerhub-username>/autoscale-app:latest .
docker push <your-dockerhub-username>/autoscale-app:latest


### 2. Apply Kubernetes Resources

kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/hpa.yaml


### 3. Enable Metrics Server

kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml


### 4. Generate Load

hey -z 2m -c 20 http://<external-ip>/load


### 5. Observe Autoscaling

kubectl get hpa
kubectl get pods -w


---
