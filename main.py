import streamlit as st
from streamlit_cropper import st_cropper

from image import Image

st.set_option("deprecation.showfileUploaderEncoding", False)

image = Image("/home/rahmaevao/Pictures/I.jpg")

cropped_img = st_cropper(image.image, realtime_update=True)
st.sidebar.markdown(image.get_information())
