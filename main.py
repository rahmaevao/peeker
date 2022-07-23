import PIL
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


def remove_tag():
    global image
    global selected_tag

    image.remove_tag(selected_tag)


st.set_option("deprecation.showfileUploaderEncoding", False)
st.set_page_config(page_title="Peeker", page_icon=PIL.Image.open("docs/logo.png"))

image = Image("tests/images/ninja_turtles.jpeg")

# st.sidebar.markdown(image.get_information())
tag_view_mode: bool = st.sidebar.checkbox("Tag view mode")

if not tag_view_mode:
    st.image(image.get_pil_image())
else:

    selected_tag = st.sidebar.selectbox("Choose the tag", image.get_tags_name())

    st.sidebar.button("Remove", on_click=remove_tag)

    button = st.sidebar.checkbox("Add tag")
    if not button:
        st.image(image.get_tagged_image())
    else:
        cropped_img = st_cropper(
            image.get_tagged_image(), realtime_update=True, return_type="box"
        )
        frame = FrameModel.parse_obj(cropped_img)

        tag_name_text_input = st.sidebar.text_input("Create tag", "")
        st.sidebar.button("Add", on_click=add_tag)
