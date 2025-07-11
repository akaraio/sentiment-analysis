import streamlit as st
import pandas as pd
import numpy as np

from transformers import pipeline

st.title("Fine Tuning BERT for Twitter Tweets for Multi Class Sentiment Classification")

classifier = pipeline('text-classification', model= 'data')

text = st.text_area("Enter some text")

if st.button("Predict"):
    result = classifier(text)
    st.write(result)