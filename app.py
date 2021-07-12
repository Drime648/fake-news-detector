import tensorflow as tf
import streamlit as st
from newspaper import Article
import streamlit as st
import validators

# url = "https://www.cnn.com/2021/07/12/health/us-coronavirus-monday/index.html"



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

        print(text)



main()

