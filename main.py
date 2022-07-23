import streamlit as st
from loguru import logger
from streamlit_cropper import st_cropper

from image import Image
from models import FrameModel, TagModel
from tag import Tag


def add_tag():
    global image
    global tag_name_text_input
    global frame

    image.add_tag(Tag(name=tag_name_text_input, frame=frame))


st.set_option("deprecation.showfileUploaderEncoding", False)

image = Image("tests/images/ninja_turtles.jpeg")

cropped_img = st_cropper(image.pil_image, realtime_update=True, return_type="box")

frame = FrameModel.parse_obj(cropped_img)
st.sidebar.markdown(image.get_information())
tag_name_text_input = st.sidebar.text_input("Tag name", "")
button = st.sidebar.button("Add tag", on_click=add_tag)
logger.info(f"{frame=}")
# st.sidebar.markdown(image.get_information())
