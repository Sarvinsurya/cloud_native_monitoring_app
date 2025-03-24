## **Cloud Native Monitoring App**
A **Cloud-Native Monitoring Application** built with **Flask**, containerized using **Docker**, and deployed using **Kubernetes**.  

---

## **Table of Contents**
- [About the Project](#about-the-project)  
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Setup Instructions](#setup-instructions)  
- [Docker Configuration](#docker-configuration)  
- [Kubernetes Deployment](#kubernetes-deployment)  

---

## **About the Project**
This project is a **Flask-based monitoring system** that collects **system metrics** and exposes them through an API.  
- Containerized with **Docker**  
- Deployed in **Kubernetes**  
- Allows real-time monitoring of **CPU, Memory, and Disk usage**  

---

## **Features**
- **Dockerized Flask App**  
- **Kubernetes Deployment**  
- **Exposes API for system metrics**  
- **Can be accessed via `kubectl port-forward`**  
- **Real-time monitoring**  

---

## **Tech Stack**
- **Backend:** Flask (Python)  
- **Containerization:** Docker  
- **Orchestration:** Kubernetes  

---

## **Setup Instructions**
### **1. Clone the Repository**
```bash
git clone https://github.com/Sarvinsurya/cloud_native_monitoring_app.git
cd cloud_native_monitoring_app
```

### **2. Install Dependencies (For Development)**
```bash
pip install -r requirements.txt
```

### **3. Run the Flask App Locally**
```bash
python app.py
```

---

## **Docker Configuration**
### **1. Build the Docker Image**
```bash
docker build -t my-flask-app .
```

### **2. Run the Container**
```bash
docker run -p 5000:5000 my-flask-app
```

### **3. Verify Running Containers**
```bash
docker ps
```

### **4. Stop the Container**
```bash
docker stop <container-id>
```

---

## **Kubernetes Deployment**
### **1. Apply Kubernetes Manifest**
Ensure you have **minikube** or **a Kubernetes cluster** running.  
```bash
kubectl apply -f deployment.yaml
```

### **2. Check Running Deployments**
```bash
kubectl get deployments -n default
```

### **3. Get Running Pods (Watch Mode)**
```bash
kubectl get pods -n default -w
```

### **4. Port Forward Flask Service**
```bash
kubectl port-forward svc/my-flask-service 5000:5000
```
Now, the app should be accessible at:  
**`http://localhost:5000`**

### **5. Check Logs**
```bash
kubectl logs <pod-name>
```

