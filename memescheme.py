import streamlit as st
import random

st.sidebar.title("Meme Priority")
thelist = ["Hera Pheri Memes", "Welcome Memes"]
chioce = st.sidebar.radio("Haan, idhar pehle dabaneka", thelist )

st.title("**memeScheme**")

def get_memes(path, img_num):
    try:
        st.image(path+img_num+".jpg", width=600)
    except FileNotFoundError:
        try:
            st.image(path+img_num+".png")
        except FileNotFoundError:
            st.image("https://media.makeameme.org/created/hmmm-nope-try.jpg")

if chioce == "Hera Pheri Memes":
    path = "./herapheri/herapheri_"
    img_num = str(random.randint(0,600))
    st.sidebar.button("Abhi majja ayega na bhidu!", get_memes(path, img_num))
    
if chioce == "Welcome Memes":
    path = "./welcome/welcome_"
    img_num = str(random.randint(0,20))
    st.sidebar.button("Aloo, leyloooo. Kaande, leyloooo", get_memes(path, img_num))

st.info("""
### Note
* All the memes are downloaded somewhere from the internet 🤗
* We do not own the content 😶 
* But we love the content 😍

### Want to contribute?
Simple. Upload your own memes to the Github repository.

""")
