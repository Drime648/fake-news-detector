import tensorflow as tf
import streamlit as st
from newspaper import Article
import streamlit as st


url = "https://www.cnn.com/2021/07/12/health/us-coronavirus-monday/index.html"



def scrape_text(url):

    article = Article(url)
    article.download()
    article.parse()

    return article.text




