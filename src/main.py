import sys

import PIL
import streamlit as st
from streamlit_cropper import st_cropper

from file_manager import FileManager
from image import Image
from models import FrameModel
from tag import Tag


def add_tag():
    global image
    global tag_name_text_input
    global frame

    image.add_tag(Tag(name=tag_name_text_input, frame=frame))


st.set_page_config(page_title="Peeker", page_icon=PIL.Image.open("docs/logo.png"))


image_file = sys.argv[-1]
file_manager = FileManager(image_file)
st.sidebar.markdown(file_manager.file_browser_repr())
left_column, right_column = st.sidebar.columns(2)
left_column.button("👈", on_click=file_manager.left_file)
right_column.button("👉", on_click=file_manager.right_file)

image = Image(file_manager.get_current_image_file_path())


tag_view_mode: bool = st.sidebar.checkbox("Tag view mode")

if not tag_view_mode:
    st.image(image.get_pil_image())
else:

    tag_name_text_input = st.sidebar.text_input("Enter a name for the new tag", "")
    st.sidebar.button(
        "Add",
        on_click=add_tag,
        disabled=not tag_name_text_input,
        help="Enter the tag name above. Mark an area of the image. Click this button.",
    )

    tag_to_remove = st.sidebar.selectbox(
        "Select a tag to remove", image.get_tags_name()
    )
    st.sidebar.button(
        "Remove",
        on_click=image.remove_tag,
        args=(tag_to_remove,),
        help="Select tag for removing above",
    )

    if not tag_name_text_input:
        st.image(image.get_tagged_image())
    else:
        cropped_img = st_cropper(
            image.get_tagged_image(), realtime_update=True, return_type="box"
        )
        frame = FrameModel.parse_obj(cropped_img)
