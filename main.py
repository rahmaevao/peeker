import streamlit as st
from streamlit_cropper import st_cropper

from image import Image

st.set_option("deprecation.showfileUploaderEncoding", False)

image = Image("tests/images/ninja_turtles.jpeg")

cropped_img = st_cropper(image.pil_image, realtime_update=True)
st.sidebar.markdown(image.get_information())
