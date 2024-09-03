import json
import base64
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottie_file(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)
lottie_animation1 = load_lottie_file("greendiamond.json")
lottie_animation = load_lottie_file("boomboom.json")

def create_copy_button(text_to_copy):
    button_id = "copyButton" + text_to_copy
    button_html = f"""<button id="{button_id}">Copy</button>
    <script>
    document.getElementById("{button_id}").onclick = function() {{
        navigator.clipboard.writeText("{text_to_copy}").then(function() {{
            console.log('Async: Copying to clipboard was successful!');
        }}, function(err) {{
            console.error('Async: Could not copy text: ', err);
        }});
    }}
    </script>"""
    st.markdown(button_html, unsafe_allow_html=True)

def main():
    st.set_page_config(
        page_title="Blober",
        page_icon="download.png", 
        layout="wide",     
        initial_sidebar_state="auto"
    )
    st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css?family=Audiowide" rel="stylesheet">
    <style>
        .grey-qo-regular {
            font-family: "Audiowide", sans-serif;
            font-weight: 200;
            font-style: normal;
        }
        .zeyada-regular {
            font-family: "Audiowide", sans-serif;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<p class='grey-qo-regular' style='text-align: center;color:red;font-size:90px;'>Blober</p>", unsafe_allow_html=True)     
    st.markdown("<p </p>", unsafe_allow_html=True)     
 
    st.markdown(
        """
        <style>
        /* Reduce width of dropdown */
        .css-1e5mbc4 {
            width: 120px !important;
        }
        /* Increase height of text areas */
        .css-1cpxqw2, .css-1d391kg {
            height: 500px !important;
        }
        /* Center the Lottie animation */
        .centered-lottie {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        </style>
        """, unsafe_allow_html=True
    )

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
                label="Download Result",
                data=st.session_state.formatted_text,
                file_name="result.txt",
                mime="text/plain"
            )
        
        with st.container():
            st.markdown('<div class="centered-lottie">', unsafe_allow_html=True)
            # st.text("")   
            # st.text("")   
            # st.text("")  
            st_lottie(lottie_animation, height=250, key="lottie_animation")

            st_lottie(lottie_animation1, height=250, key="lottie_animation1")
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
if __name__ == "__main__":
    main()
