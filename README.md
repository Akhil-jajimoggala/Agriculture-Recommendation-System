# 🌾 **Agriculture Yield Prediction System**  
### *Tool to Predict Yield Using Google Cloud Vertex AI*

---

![Agriculture Yield Prediction](https://xifagroup.com/wp-content/uploads/2024/06/rice-bag.webp)

This tool predicts crop yield based on historical data of weather conditions, soil properties, and other relevant factors. It is designed to help farmers and agricultural businesses make informed decisions about planting, harvesting, and resource allocation.

---

## 🛠 **Design**

- Build a crop yield predictor using **Google Cloud Vertex AI**.  
- Incorporates **historical weather and soil data** to train and deploy a machine-learning model.  

---

## 📋 **Prerequisites**

1. **Google Cloud Platform (GCP) Account:**  
   [Create an account here](https://console.cloud.google.com/)  
2. **Knowledge Base:**  
   - Basic Python programming  
   - Familiarity with Machine Learning concepts  
   - Working knowledge of GCP  
3. **Dataset:**  
   - [Synthetic Agricultural Yield Dataset](https://www.kaggle.com/datasets/blueloki/synthetic-agricultural-yield-prediction-dataset?resource=download)  

---

## 📝 **Step-by-Step Instructions**

---

### 1️⃣ **Create a GCP Project**  
   - Go to the [GCP Console](https://console.cloud.google.com/) and create a new project.  
   - Enable the **Vertex AI API** for your project.

---

### 2️⃣ **Prepare the Data**  
   - Download and preprocess your dataset (e.g., cleaning, handling missing values, normalizing features).  
   - Convert CSV data into **Vertex AI accepted JSONL format**.

---

### 3️⃣ **Create Google Cloud Bucket and Upload the Dataset**  
   - Navigate to **Cloud Storage Buckets** in the GCP console and create a bucket.  
   - Assign the necessary permissions.  
   - Upload the JSONL dataset to the bucket.

---

### 4️⃣ **Fine-Tune the Model in Vertex AI**  
   - Navigate to **Vertex AI** and select **Model Garden**.  
   - Select and fine-tune a model that fits your dataset.  
   - Configure the settings and train the model with the dataset.

---

### 5️⃣ **Create an Endpoint for the Model**  
   - Deploy and test the model using Vertex AI.  
   - Create an endpoint with the required configurations.

---

### 6️⃣ **Evaluate the Model**  
   - Use the **Freeform section** in Vertex AI to validate the model.  
   - Provide inputs (e.g., weather conditions, soil properties) to test predictions.  

---

## 📊 **Results**

- Predicts **yield in kg/ha** based on the provided weather and soil conditions.  
- Aids in optimizing resource allocation and planning agricultural operations.

---

## 🎯 **Call to Action**

- Learn more about Google Cloud services:  
  - [Register for Code Vipassana Sessions](#)  
  - [Become a Google Cloud Innovator](https://cloud.google.com/innovators/)

---

## 🔗 **GitHub Links**

- [🌱 Agriculture Yield Prediction System](https://github.com/Akhil-jajimoggala/Agriculture-Yield-Prediction-System)

Contribute to this project and explore its development further.

---

## ✍️ **Authors**

- [Akhil Jajimoggala](https://www.linkedin.com/in/akhil-jajimoggala-125a4b24b/)
- [Masthan Rao Gampala](https://www.linkedin.com/in/masthan-rao-7383452a9/)
