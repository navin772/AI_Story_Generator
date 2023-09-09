import streamlit as st
import os

from workflow_text_to_text import generate_story_from_text

st.set_page_config(
    page_title="Retail product detection", layout="wide"
)


st.sidebar.write("Select the genre/theme of the story:")

story_theme = st.sidebar.radio("Genre", ("Horror", "Action", "Romance", "Comedy", "Historical", "Science Fiction"))

theme_based_prompts = {
    "Horror": "Write a horror story that ends mysteriously using: ",
    "Action": "Write a story with lots of action using: ",
    "Romance": "Write a romantic story using: ",
    "Comedy": "Write a funny story using: ",
    "Historical": "Write a story based on a historical event with the help of the input: ",
    "Science Fiction": "Write a science fiction story using: "
}

st.markdown("# AI Story Generator")

st.markdown("## Choose the input type you want to give to start with the story generation")

input_type = st.radio("Input type", ("Text", "Image"))

if input_type == "Text":

    st.markdown("### Enter the sentences you want to have your story revolve around")

    input_text = st.text_area("Enter the text here", height=100)

    theme_based_input = theme_based_prompts[story_theme] + " " + input_text

    if st.button("Generate story"):
        with st.status("Generating story...", expanded=True) as status_text:

            st.write("Fusing your story elements together...")
            st.write("This may take about 30-40 seconds (more if runnung the first time), please hang tight...")

            story = generate_story_from_text(theme_based_input)

            status_text.update(label="Story created!")
        
        st.markdown("### Your Story based on your input!")
        story_lines = story.split('\n')
        formatted_story = "\n".join(["##### " + line for line in story_lines])
        
        st.markdown(formatted_story)
            

if input_type == "Image":
    st.markdown("### Upload the image you want to start with")
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        if st.button("Generate story"):
            st.write("Story will be generated here")

