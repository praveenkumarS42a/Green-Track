import streamlit as st # type: ignore
import tensorflow as tf # type: ignore
import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore
from PIL import Image # type: ignore

# Function to load the model
def load_model(model_path):
    return tf.keras.models.load_model(model_path)

# Function to preprocess the image
def preprocess_image(img, target_size=(299, 299)):
    img = img.resize(target_size)
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    return img_array

# Function to get predictions
def get_prediction(model, img, class_names):
    img_array = preprocess_image(img)
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions)
    predicted_class_name = class_names[predicted_class]

    return predicted_class_name

# Streamlit app
def main():
    st.title("Garbage Classification")
   
    
    # Path to the saved model
    model_path = "model_aug_no_sh.h5"

    # Load the model
    model = load_model(model_path)

    # Class names
    class_names = ['battery', 'biological', 'brown-glass', 'cardboard', 'clothes', 'green-glass', 'metal', 'paper', 'plastic', 'shoes', 'trash', 'white-glass']

    # Recyclable wastes
    recyclable_wastes = ['metal', 'paper', 'brown-glass', 'green-glass', 'white-glass', 'plastic','cardboard']

    # Upload image
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        st.write("Classifying...")
        
        predicted_class = get_prediction(model, image, class_names)
        st.write(f"The predicted class is: {predicted_class}")

        if predicted_class in recyclable_wastes:
            st.success("Your item is recyclable!")
            if st.button("Schedule Pickup"):
                st.markdown("[Schedule Pickup](http://127.0.0.1:8000/schedule)")
        else:
            st.error("This item is not recyclable.")

if __name__ == "__main__":
    main()
