import streamlit as st
import numpy as np
from PIL import Image
import torch
import torchvision.transforms as transforms

# Dummy model for placeholder (replace with actual model loading)
class DummyModel:
    def predict(self, image_tensor):
        return "Real" if torch.rand(1).item() > 0.5 else "Fake"

model = DummyModel()

st.set_page_config(page_title="ML Hackathon: PVH", layout="centered")

st.title("ML Hackathon: PVH")
st.subheader("Detecting AI-Generated Images")

st.markdown("""
## Upload Image for Classification
Upload an image to check if it's **AI-generated (Fake)** or **Real**. The image will be resized to 32x32 as per CIFAKE format.
""")

uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Preprocess image
    transform = transforms.Compose([
        transforms.Resize((32, 32)),
        transforms.ToTensor(),
    ])
    image_tensor = transform(image).unsqueeze(0)  # Add batch dimension

    # Predict (replace with actual model call)
    prediction = model.predict(image_tensor)
    
    st.markdown(f"### Prediction: **{prediction}**")

st.markdown("""
---
## About the Challenge
AI tools like **Adobe Firefly**, **Stable Diffusion**, and **Midjourney** are revolutionizing content creation. However, detecting AI-generated images—especially those with adversarial perturbations—remains a significant challenge.

### Problem Statement
Build a model to classify images as **Real** or **Fake**, with a focus on diffusion-based synthetic images.

### Dataset
- 50,000 Real + 50,000 Fake images for training  
- 10,000 Real + 10,000 Fake images for testing  
- Image Size: 32x32 (CIFAKE format)  
- [Download Dataset](https://www.kaggle.com/datasets/birdy654/cifake-real-and-ai-generated-synthetic-images)

### Evaluation
- Test Dataset 1 (no perturbations): 40%  
- Test Dataset 2 (with perturbations): 60%  
- Metrics: Accuracy, Precision, Recall, F1 Score

### Deliverables
- All code files and model weights  
- README with instructions  
- `Test_1_results.csv` and `Test_2_results.csv`

### Guidelines
- Predictions must be "Real" or "Fake"  
- Submit via Google Form  
- Zip format: `TEAM_NAME_PVH_ML.zip`  
- No plagiarism  
- Mention pre-trained models if used

---
Built for the **ML Hackathon | PVH Challenge 2025**
""")
