import tensorflow as tf
import streamlit as st
from newspaper import Article
import streamlit as st
import validators
import numpy as np

# url = "https://www.cnn.com/2021/07/12/health/us-coronavirus-monday/index.html"

model = tf.keras.models.load_model("debunker_model")

class_names = ["fake news", "true news"]

def scrape_text(url):

    article = Article(url)
    article.download()
    article.parse()

    return article.text


def main():
    user_input = st.text_input("Add News Url here", "")

    url = user_input

    valid=validators.url(url)

    if valid:

        text = scrape_text(url)

        replaced_string = text.replace('"', "")
        

        

        

        st.header(pred)

        st.write(replaced_string)

        data = model.predict([replaced_string])
        pred = class_names[np.argmax(data)]





main()

