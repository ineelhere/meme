import streamlit as st
import random
from sources import *

st.sidebar.title("Meme Priority")
thelist = ["Hera Pheri Memes", "Welcome Memes", "Kota Factory Reality"]
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
    img_num = str(random.randint(0,28))
    st.sidebar.button("Aloo, leyloooo. Kaande, leyloooo", get_memes(path, img_num))

if chioce == "Kota Factory Reality":
    path = "./kotafactory/kotafactory_"
    img_num = str(random.randint(0,26))
    st.sidebar.button("Not everything is a meme.", get_memes(path, img_num))

st.write("**P.S. - Not everything is a meme 🙂**")
st.success("""
### Note
* All the memes are downloaded somewhere from the internet 🤗
* We do not own the content 😶 
* But we love the content 😍
""")
st.image("https://pbs.twimg.com/profile_banners/1248075734603550720/1586524553/1500x500", width=700)
st.sidebar.info("""
### Want to contribute? It's Simple. 
* Share the meme urls with us in a csv file and upload them to the [Github repository](https://github.com/ineelhere/meme) with a [Pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests).
* OR, directly upload the memes to the [Github repository](https://github.com/ineelhere/meme) with a [Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests).
* We will add the memes to the website.

##### Points to note:
* Don't use any political/offensive/obscene/sexual language in the memes. Yeah, keep them simple.
* Your meme should make the audience laugh. Not attack or insult them.
* Don't use any racist or sexist language in the memes.
* Don't use hate speech in the memes.
""")

if st.checkbox("Show the source for these Memes"):
    sources()
