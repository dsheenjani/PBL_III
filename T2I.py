import streamlit as st # type: ignore
from huggingface_hub import InferenceClient # type: ignore
from PIL import Image

# Define a function to generate images
def generate_image(prompt):
    try:
        # Set up Hugging Face Inference Client
        client = InferenceClient(
            model="runwayml/stable-diffusion-v1-5", 
            token="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"
        )
        
        # Generate the image
        image = client.text_to_image(prompt=prompt)
        return image  # Return the generated image object
    
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Streamlit UI
st.title("AI Image Generator")
st.write("Generate images from text descriptions using Stable Diffusion.")

# Input box for the user to provide a text prompt
prompt = st.text_input("Enter your image description:", value="A beautiful sunset over the ocean")

# Button to trigger image generation
if st.button("Generate Image"):
    if prompt.strip():
        st.write("Generating image, please wait...")
        # Generate the image
        generated_image = generate_image(prompt)
        
        # Display the image
        if generated_image:
            st.image(generated_image, caption="Generated Image", use_column_width=True)
    else:
        st.warning("Please enter a valid text prompt.")

st.write("Powered by [Hugging Face](https://huggingface.co) and Streamlit.")
