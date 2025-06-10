import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter

st.set_page_config(page_title="Image Editor", layout="wide")
st.header("Image Editor")
st.subheader("Upload an image to edit")

image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], accept_multiple_files=False)

if image is not None:
    img = Image.open(image)
    original_img = img.copy()

    st.sidebar.header("Edit Options")
    st.sidebar.subheader("Adjustments")
    brightness = st.sidebar.slider("Brightness", 0.0, 2.0, 1.0)
    contrast = st.sidebar.slider("Contrast", 0.0, 2.0, 1.0)
    sharpness = st.sidebar.slider("Sharpness", 0.0, 2.0, 1.0)
    blur = st.sidebar.slider("Blur", 0, 10, 0)
    flip_Image = st.sidebar.selectbox("Flip Image", options=["Select Option", "FLIP_TOP_BOTTOM", "FLIP_LEFT_RIGHT"])

    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(brightness)

    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(contrast)

    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(sharpness)

    if blur > 0:
        img = img.filter(ImageFilter.GaussianBlur(radius=blur))

    if flip_Image == "FLIP_TOP_BOTTOM":
        img = img.transpose(Image.FLIP_TOP_BOTTOM)
    elif flip_Image == "FLIP_LEFT_RIGHT":
        img = img.transpose(Image.FLIP_LEFT_RIGHT)

    col1, col2 = st.columns(2)
    with col1:
        st.image(original_img, caption="Original Image", use_container_width=True)
    with col2:
        st.image(img, caption="Edited Image", use_container_width=True)

    st.sidebar.download_button(
        label="Download Edited Image",
        data=img.convert("RGB").tobytes(),
        file_name="edited_image.png",
        mime="image/png"
    )
else:
    st.warning("Please upload an image to start editing.")


