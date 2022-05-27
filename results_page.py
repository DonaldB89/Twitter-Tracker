import streamlit as st
pip install typing-extensions
import numpy as np
import pandas as pd
from PIL import Image

df = pd.read_csv("submission.csv")
df = pd.read_csv('submission.csv')
df = df.loc[df["Category"] !='N']
df = df.drop(labels=["clean_text", "predict_prob","Unnamed:"], axis=1)
df = df.rename(columns={'Text': 'Tweets', 'Category': 'Important?'})

st.title("Twitter Tracker")

st.write("""### The latest trending news sources""")

st.table(df)

#image
image = Image.open('8MS logo2.jpg')
st.image(image,width=300)
