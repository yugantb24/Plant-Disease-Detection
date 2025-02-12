import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
from keras.models import load_model
import time
import random
model = load_model("plantDiseaseClassification.h5")
# Page Configurations
st.set_page_config(page_title="🌿 Plant Disease Detection", page_icon="🌱", layout="wide")

# Custom CSS for Styling
st.markdown("""
    <style>
    .main {
        background-color: #e8f5e9;
    }
    .reportview-container .main .block-container {
        padding-top: 2rem;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        transition-duration: 0.4s;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: white;
        color: black;
        border: 2px solid #4CAF50;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🌿 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Fun Facts", "Contact Us"])

if page == "Home":
    # Title and Description
    st.title("🌱 Plant Disease Detection")
    st.subheader("Upload an image of a plant leaf to detect the disease.")
    st.write("This is an Plant Disease Classification of two plants i.e Pepper Bell and Potato – Model integration ")

    # Upload Image
    uploaded_file = st.file_uploader("Choose a leaf image...", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        # Display Uploaded Image
        image = Image.open(uploaded_file)
        st.image(image, caption='🌿 Uploaded Leaf Image', use_container_width=True)

        # Analyze Button
        analyze = st.button("🌱 Analyze Image")

        if analyze:
            with st.spinner('Analyzing... Please wait...'):
                time.sleep(3)  # Simulating a delay for analysis

            # Dummy Prediction (Replace this with your model's prediction)
            diseases = ["Pepper__bell___Bacterial_spot",'Pepper__bell___healthy', 'Potato___Early_blight',
                         'Potato___Late_blight', 'Potato___healthy']
            image = Image.open(uploaded_file)
            image = image.convert('RGB')
            image = image.resize((256, 256))
            img_array = np.array(image)

            
            img_array = tf.expand_dims(img_array, 0)
            predictions = model.predict(img_array)


            
            predicted_class = diseases[np.argmax(predictions[0])]
            st.success(f"🌱 The leaf is likely affected by: **{predicted_class}**")

            # Disease Information (Basic)
            disease_info = {
                "Pepper__bell___Bacterial_spot": " Use disease-free seeds and copper bactericides to prevent bacterial spread through water and tools.",
                "Pepper__bell___healthy": "Monitor regularly and maintain proper irrigation and sanitation",
                "Potato___Early_blight": "Apply fungicides and rotate crops to minimize fungal spores from infected debris.",
                "Potato___Late_blight": "Use resistant varieties and fungicides to prevent spore spread via wind and rain.",
                "Potato___healthy": "Regular inspection and good agricultural practices ensure continued plant health."
            }
            
            st.info(disease_info[predicted_class])
    else:
        st.warning("Please upload an image to analyze.")

elif page == "Fun Facts":
    st.title("🌼 Fun Facts About Plants")
    facts = [
        "Bananas are berries, but strawberries are not! 🍓",
        "Sunflowers can clean radioactive soil. 🌻",
        "Bamboo can grow up to 3 feet in a day! 🎋",
        "There are over 390,000 plant species on Earth. 🌍",
        "Plants ‘talk’ to each other through their roots. 🌱"
    ]
    st.write(random.choice(facts))
    st.image("https://source.unsplash.com/800x400/?plants", caption="Nature's Wonders", use_container_width=True)

elif page == "Contact Us":
    st.title("📧 Contact Us")
    st.write("For inquiries or feedback, please reach out via:")
    st.markdown("""
        - **Email:** yugantbambal24@gmail.com  
        - **Phone:** 7559372777  
    
    """)
    st.image("https://source.unsplash.com/800x400/?nature", caption="Let's Grow Together!", use_container_width=True)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit | © 2025 Plant Detection Inc.")
