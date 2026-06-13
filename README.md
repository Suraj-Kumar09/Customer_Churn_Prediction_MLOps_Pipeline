# 🚀 Customer Churn Prediction - End-to-End MLOps Pipeline

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge\&logo=python)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-orange?style=for-the-badge)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge\&logo=scikitlearn)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-green?style=for-the-badge\&logo=mongodb)
![Flask](https://img.shields.io/badge/Flask-Web%20API-black?style=for-the-badge\&logo=flask)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue?style=for-the-badge\&logo=docker)
![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-black?style=for-the-badge\&logo=githubactions)
![AWS S3](https://img.shields.io/badge/AWS-S3-red?style=for-the-badge\&logo=amazons3)
![CI/CD](https://img.shields.io/badge/CI%2FCD-Automation-success?style=for-the-badge)
![YAML](https://img.shields.io/badge/YAML-Configuration-red?style=for-the-badge\&logo=yaml)

---

# ⚡ Project Overview

Customer churn is one of the most critical business challenges for telecom companies. This project implements a complete **End-to-End MLOps Pipeline** for predicting customer churn using Machine Learning while following production-grade software engineering and deployment practices.

The project automates the entire workflow from data ingestion to model deployment using a modular architecture, Docker containerization, CI/CD automation, and cloud-ready configurations.

---

# 🛠️ Core Tech Stack

* 🐍 Python
* 🤖 Scikit-Learn
* 📊 Pandas
* 🔢 NumPy
* 📈 Matplotlib
* 📉 Seaborn
* ⚖️ SMOTEENN
* 🌲 Random Forest
* ⚡ XGBoost
* 🐱 CatBoost
* 👥 KNN
* 🍃 MongoDB Atlas
* 🌐 Flask API
* ☁️ AWS S3
* 🐳 Docker
* 🔄 GitHub Actions
* 📄 YAML Configuration
* 🏗️ MLOps Pipeline

---

# 🎯 Business Problem

Telecommunication companies lose significant revenue due to customer churn.

The goal of this project is to:

* Identify customers likely to churn.
* Enable proactive retention strategies.
* Reduce customer acquisition costs.
* Improve customer lifetime value.

---

# 🏗️ Project Architecture

```text
MongoDB Atlas
      │
      ▼
Data Ingestion
      │
      ▼
Data Validation
      │
      ▼
Data Transformation
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
Model Pusher
      │
      ▼
Saved Model
      │
      ▼
Flask Application
      │
      ▼
Prediction API
```

---

# 📂 Project Structure

```text
customer_churn/

├── components/
│   ├── data_ingestion.py
│   ├── data_validation.py
│   ├── data_transformation.py
│   ├── model_trainer.py
│   ├── model_evaluation.py
│   └── model_pusher.py
│
├── entity/
│   ├── config_entity.py
│   ├── artifact_entity.py
│   └── estimator.py
│
├── pipeline/
│   ├── training_pipeline.py
│   └── prediction_pipeline.py
│
├── utils/
│   └── main_utils.py
│
├── logger/
├── exception/
│
├── config/
│   ├── schema.yaml
│   └── model.yaml
│
├── app.py
├── Dockerfile
├── requirements.txt
└── setup.py
```

---

# ⚙️ Key Features

## 1️⃣ Modular Architecture Design

* Industry-standard project structure.
* Component-based architecture.
* Easy maintenance and scalability.
* Reusable pipeline components.

### Modules

* Data Ingestion
* Data Validation
* Data Transformation
* Model Training
* Model Evaluation
* Model Pusher
* Prediction Pipeline

---

## 2️⃣ Production Engineering Practices

### Custom Logging

* Centralized logging system.
* Easier debugging and monitoring.

### Custom Exception Handling

* Structured error reporting.
* Production-grade fault tracking.

### Configuration Driven Development

Uses:

```yaml
schema.yaml
model.yaml
```

Benefits:

* No hardcoding
* Easy experimentation
* Better maintainability

---

## 3️⃣ Data Pipeline

### Data Ingestion

* Reads customer data from MongoDB Atlas.
* Stores raw dataset in artifact directory.

### Data Validation

* Schema validation.
* Data drift detection.
* Validation reports generation.

### Data Transformation

* Missing value handling.
* Feature engineering.
* Scaling.
* Encoding.
* SMOTEENN balancing.

### Feature Set

```text
Partner
Tenure Months
Internet Service
Tech Support
Contract
Monthly Charges
```

Target:

```text
Churn Label
```

---

# 🤖 Machine Learning Models

The pipeline supports multiple models:

### Base Models

* Random Forest
* XGBoost
* KNN
* CatBoost
* Gradient Boosting
* Logistic Regression
* Decision Tree
* AdaBoost
* SVC

### Hyperparameter Tuning

Implemented using:

```python
RandomizedSearchCV
```

---

# 🏆 Final Model Performance

### Best Performing Model

```text
KNeighborsClassifier
```

### Accuracy

```text
99.08%
```

### Classification Report

```text
Precision : 0.99
Recall    : 0.99
F1 Score  : 0.99
```

---

# 🧪 Model Selection Strategy

The project performs:

* Model benchmarking
* Hyperparameter tuning
* Performance comparison
* Automated best model selection

This ensures only the highest-performing model is deployed.

---

# 📦 Docker Containerization

The complete application is containerized using Docker.

Benefits:

* Environment consistency
* Easy deployment
* Reproducibility
* Portability

### Docker Build

```bash
docker build -t customer-churn .
```

### Docker Run

```bash
docker run -p 5000:5000 customer-churn
```

---

# 🔄 CI/CD Pipeline

Implemented using GitHub Actions.

### Workflow

```text
Code Push
    │
    ▼
GitHub Actions
    │
    ▼
Build Docker Image
    │
    ▼
Push to Docker Hub
    │
    ▼
Ready for Deployment
```

### Benefits

* Fully automated builds
* Continuous Integration
* Continuous Deployment
* Secure credential management via GitHub Secrets

---

# 🐳 Docker Hub Registry

Docker Hub is used as:

```text
Container Registry
```

Benefits:

* Version control
* Artifact storage
* Easy deployment
* Reusable images

---

# 🌐 Flask Prediction API

The trained model is served through a Flask web application.

Features:

* User-friendly interface
* Real-time prediction
* Production-ready architecture

Input:

```text
Tenure Months
Monthly Charges
Contract
Partner
Internet Service
Tech Support
```

Output:

```text
Churn
or
No Churn
```

---

# 📈 MLOps Workflow Summary

| Stage            | Implementation                         |
| ---------------- | -------------------------------------- |
| Project Setup    | Modular architecture using template.py |
| Data Storage     | MongoDB Atlas                          |
| Validation       | Schema & drift validation              |
| Transformation   | Encoding, Scaling, SMOTEENN            |
| Training         | Multiple ML algorithms                 |
| Tuning           | RandomizedSearchCV                     |
| Evaluation       | Automated model comparison             |
| Serving          | Flask API                              |
| Containerization | Docker                                 |
| Registry         | Docker Hub                             |
| Automation       | GitHub Actions                         |
| Deployment Ready | Yes                                    |

---

# 🚀 Future Improvements

* MLflow Integration
* Model Versioning
* DVC Integration
* AWS Deployment
* Monitoring Dashboard
* Automated Retraining
* Kubernetes Deployment

---

# 💡 Key Learnings

Through this project I gained hands-on experience in:

* End-to-End MLOps
* Production ML Pipelines
* Software Engineering Best Practices
* Docker Containerization
* CI/CD Automation
* Model Lifecycle Management
* API Deployment
* Cloud-Ready Architecture

---


---

# 👨‍💻 Author

## Suraj Kumar

### 📫 Contact Information

📧 Email: srsuraj009@gmail.com

📱 Phone: +91 9801263970

💼 LinkedIn: https://www.linkedin.com/in/aideveloperontop/

🐙 GitHub: https://github.com/Suraj-Kumar09

Aspiring **AI/ML Engineer** with hands-on experience in:

* 🤖 Machine Learning
* ⚙️ MLOps
* 🧠 Generative AI
* 🔍 Retrieval-Augmented Generation (RAG)
* 📚 Large Language Models (LLMs)
* 🚀 Production-Ready AI Systems


---

### 💼 Open to Opportunities

I am actively seeking opportunities in:

* Machine Learning Engineer
* AI Engineer
* Generative AI Engineer
* MLOps Engineer
* Data Scientist

Feel free to connect for collaborations, internships, full-time opportunities, or technical discussions.

---

⭐ If you found this project useful, please consider giving it a star.