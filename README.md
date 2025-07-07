# 🌿 Plant Disease Detection using Deep Learning

A Streamlit-powered web application that uses a deep learning model to classify diseases in **Potato** and **Pepper Bell** plants based on leaf images. The project leverages computer vision techniques to assist farmers and agriculturists in early disease detection and prevention.

---

## 🚀 Features

- 🌱 **Upload and Analyze**: Upload an image of a plant leaf and get instant predictions.
- 🤖 **Deep Learning Model**: Uses a trained Keras model (`.h5`) to classify diseases.
- 🎨 **User-Friendly UI**: Built with Streamlit and styled with custom CSS.
- 📚 **Disease Info**: Provides care tips and prevention advice based on the prediction.
- 💬 **Sidebar Navigation**: Includes fun facts about plants and a contact section.

---

## 🧠 Model Classes

The model is trained to classify the following classes:

- `Pepper__bell___Bacterial_spot`  
- `Pepper__bell___healthy`  
- `Potato___Early_blight`  
- `Potato___Late_blight`  
- `Potato___healthy`  

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **TensorFlow / Keras**
- **NumPy / PIL**
- **Streamlit** – for building the interactive web app

---

## 📷 How It Works

1. Upload an image of a plant leaf.
2. The image is resized and preprocessed to match the model's expected input.
3. The deep learning model makes a prediction.
4. The class label and care suggestions are shown to the user.

---



