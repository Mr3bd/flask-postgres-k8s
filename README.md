# 📚 Books API - Flask + PostgreSQL (Docker + Kubernetes)

A simple RESTful API to manage a list of books using Flask and PostgreSQL, deployed using Docker and Kubernetes. The setup includes ConfigMaps, Secrets, Persistent Volumes, Health Checks, and Horizontal Pod Autoscaling (HPA).

---

## 🚀 Features

- REST API endpoints for book management
- PostgreSQL database with persistent volume
- Flask app containerized with Docker
- Kubernetes deployment with:
  - ConfigMap & Secret for environment configs
  - Readiness & Liveness probes
  - Horizontal Pod Autoscaler (HPA)
  - NodePort service for external access (via Minikube)

---

## 🧰 Requirements

- Docker
- Minikube
- kubectl
- curl (optional for testing)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

git clone https://github.com/Mr3bd/flask-postgres-k8s.git
cd books-api-k8s

### 2. Build and Push the Docker Image

cd app
docker build -t yourdockerhubusername/books-api:latest .
docker push yourdockerhubusername/books-api:latest
cd ..

Update the image name in k8s/flask-deployment.yaml:

image: yourdockerhubusername/books-api:latest

### 3. Start Minikube

minikube start

### 4. Create ConfigMap and Secret

kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/secret.yaml
kubectl create configmap init-sql --from-file=init-db/init.sql

### 5. Deploy Kubernetes Resources

kubectl apply -f k8s/

### 6. Access the Application

minikube service flask-service

This will open the app in your browser.

---

## 🧪 Example Usage with curl

### Add a Book:

curl -X POST http://localhost:PORT/books -H "Content-Type: application/json" -d '{"title": "DevOps for Beginners"}'

### Get All Books:

curl http://localhost:PORT/books

Replace PORT with the NodePort assigned by minikube service flask-service.

---

## 📈 Autoscaling

Check HPA status:

kubectl get hpa

To customize HPA settings, edit k8s/hpa.yaml.

---

## 🧼 Cleanup

kubectl delete -f k8s/
kubectl delete configmap init-sql

----

## 👨‍💻 Author

[Abdullrahman Wasfi](https://www.linkedin.com/in/abdullrahmanwasfi)

Made with ❤️ using Vagrant, Ansible, and Node.js

---

## 📄 License

MIT License

Let me know if you'd like it saved as a downloadable `.md` file or want me to help generate a GitHub repo structure for publishing.