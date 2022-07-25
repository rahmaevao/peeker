import sys

import PIL
import streamlit as st
from streamlit_cropper import st_cropper

from image import Image
from models import FrameModel
from tag import Tag
from file_manager import FileManager

def add_tag():
    global image
    global tag_name_text_input
    global frame

    image.add_tag(Tag(name=tag_name_text_input, frame=frame))


def remove_tag():
    global image
    global tag_to_remove

    image.remove_tag(tag_to_remove)


st.set_page_config(page_title="Peeker", page_icon=PIL.Image.open("docs/logo.png"))


image_file = sys.argv[-1]
file_manager = FileManager(image_file)
st.sidebar.markdown(file_manager.file_browser_repr())
image = Image(file_manager.get_current_image_file_path())


tag_view_mode: bool = st.sidebar.checkbox("Tag view mode")

if not tag_view_mode:
    st.image(image.get_pil_image())
else:

    tag_name_text_input = st.sidebar.text_input("Enter a name for the new tag", "")
    st.sidebar.button("Add", on_click=add_tag, disabled=not tag_name_text_input)

    tag_to_remove = st.sidebar.selectbox(
        "Select a tag to remove", image.get_tags_name()
    )
    st.sidebar.button("Remove", on_click=remove_tag)

    if not tag_name_text_input:
        st.image(image.get_tagged_image())
    else:
        cropped_img = st_cropper(
            image.get_tagged_image(), realtime_update=True, return_type="box"
        )
        frame = FrameModel.parse_obj(cropped_img)
