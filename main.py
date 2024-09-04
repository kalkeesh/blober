import json
import base64
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottie_file(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)
lottie_animation1 = load_lottie_file("greendiamond.json")
lottie_animation = load_lottie_file("boomboom.json")

def main():
    st.set_page_config(
        page_title="Blober",
        page_icon="download.png", 
        layout="wide",     
        initial_sidebar_state="auto"
    )
    
    option = st.sidebar.radio("CHOOSE", ("TEXT", "IMAGE"))

    if option == "TEXT":
        st.markdown("""
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css?family=Audiowide" rel="stylesheet">
        <style>
            .grey-qo-regular {
                font-family: "Audiowide", sans-serif;
                font-weight: 800;
                font-style: normal;
            }
            .zeyada-regular {
                font-family: "Audiowide", sans-serif;
            }
        </style>
        """, unsafe_allow_html=True)

        st.markdown("<p class='grey-qo-regular' style='text-align: center;color:red;font-size:90px;'>Blober</p>", unsafe_allow_html=True)     
        st.markdown("<p </p>", unsafe_allow_html=True)     
        if "formatted_text" not in st.session_state:
            st.session_state.formatted_text = ""

        col1, col2, col3 = st.columns([3, 0.75, 3])  

        with col1:     
            text_data = st.text_area("PASTE YOUR TEXT HERE..!", height=500, key="input_text")
            if st.button("My Creations😎", key="about_creation_button"):
                with st.expander("MY APPS AND STUFF"):
                    st.image("download.png", use_column_width=True)
                    st.write("""
                             - [MY PORTFOLIO](https://kalkeesh.github.io/) - This is my portfolio, Please do check.
                             I've built several apps and websites to help people with various tasks.
                             Here are a few of my favorites:
                             
                             - [QrBLEND](https://qrblend.streamlit.app/) - A simple app to embed text in qrcode.
                             - [TeachVibe](https://teachvibe.streamlit.app/) - It is a analysis app that dispaly sentiments of studnet comments to lectures.
                             - [Know your Way](https://nourway.streamlit.app/) - This app analyses buses data retrived from trackers placed in them, and gives detailed information about buses.
                             - [pretty json](https://prettyjson.streamlit.app/) - converts normal json data to pretty and understandable JSON representation.
                             
                             If you're interested in learning more about coding, I'd recommend checking out my [YouTube channel
                    """)

        with col2:
            st.text("")   
            action = st.selectbox("Action", options=["Encode", "Decode"], index=0, key="action_select")
            if action == "Encode":
                execute_action = st.button("Encode now")
            else:
                execute_action = st.button("Decode now")
            if execute_action and text_data:
                try:
                    if action == "Encode":
                        
                        base64_encoded = base64.b64encode(text_data.encode("utf-8")).decode("utf-8")
                        st.session_state.formatted_text = base64_encoded
                    elif action == "Decode":
                        
                        base64_decoded = base64.b64decode(text_data.encode("utf-8")).decode("utf-8")
                        st.session_state.formatted_text = base64_decoded
                except Exception as e:
                    st.error(f"An error occurred: {e}")
            
            if st.session_state.formatted_text:
                st.download_button(
                    label="Download",
                    data=st.session_state.formatted_text,
                    file_name="result.txt",
                    mime="text/plain"
                )
            
            with st.container():
                st.markdown('<div class="centered-lottie">', unsafe_allow_html=True)
                st_lottie(lottie_animation, height=100, key="lottie_animation")

                st_lottie(lottie_animation1, height=100, key="lottie_animation1")
                st.markdown('</div>', unsafe_allow_html=True)

        with col3: 
            result_text = st.text_area("RESULT", value=st.session_state.formatted_text, height=500, key="output_text")
            st.markdown(f'<textarea id="formatted_text" style="display:none;">{st.session_state.formatted_text}</textarea>', unsafe_allow_html=True)
            if st.button("About Creator🧐", key="about_creator_button"):
                with st.expander("kalkeesh jami"):
                    st.image("mepic.jpg", use_column_width=True)
                    st.write("""
                    Hello! I'm KALKEESH JAMI 
                    
                    - I love building applications that make life easier.
                    - I'm good at Python and data analysis.
                    - Don't misunderstand me as a nerd; I'm socially adept too! 😄
                    - Thank you for checking out my app!
                    
                    Do check out my [LinkedIn](https://www.linkedin.com/in/kalkeesh-jami-42891b260/) and [GitHub](https://github.com/kalkeesh/).
                    """)

    elif option == "IMAGE":
        st.markdown("""
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css?family=Audiowide" rel="stylesheet">
        <style>
            .grey-qo-regular {
                font-family: "Audiowide", sans-serif;
                font-weight: 800;
                font-style: normal;
            }
            .zeyada-regular {
                font-family: "Audiowide", sans-serif;
            }
        </style>
        """, unsafe_allow_html=True)

        st.markdown("<p class='grey-qo-regular' style='text-align: center;color:red;font-size:90px;'>Blober</p>", unsafe_allow_html=True)     
        st.markdown("<p </p>", unsafe_allow_html=True)     
        col1, col2 = st.columns([2, 3])  

        with col1:
            action = st.selectbox("Action", options=["Encode", "Decode"], index=0, key="image_action_select")

            if action == "Encode":
                uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"], key="upload_image")
                if uploaded_file is not None:
                    img_bytes = uploaded_file.read()
                    base64_encoded = base64.b64encode(img_bytes).decode("utf-8")
                    st.session_state.encoded_image = base64_encoded
            else:  
                base64_input = st.text_area("Paste Base64 Here", height=250, key="base64_input")
                if st.button("Decode now") and base64_input:
                    try:
                        decoded_img_bytes = base64.b64decode(base64_input.encode("utf-8"))
                        st.session_state.decoded_image = decoded_img_bytes
                    except Exception as e:
                        st.error(f"An error occurred: {e}")

        with col2:
            if action == "Encode" and "encoded_image" in st.session_state:
                st.text_area("Base64 Encoded Image", st.session_state.encoded_image, height=250)
            elif action == "Decode" and "decoded_image" in st.session_state:
                st.image(st.session_state.decoded_image, caption="Decoded Image", use_column_width=True)

if __name__ == "__main__":
    main()
