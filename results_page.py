import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

df = pd.read_csv("https://raw.githubusercontent.com/DonaldB89/Twitter-Tracker/main/submission.csv")
df = df.loc[df["Category"] !='N']
df = df.drop(labels=["clean_text", "predict_prob"], axis=1)
df = df.rename(columns={'Text': 'Tweets', 'Category': 'Important?'})

st.title("Twitter Tracker")

st.write("""### The latest trending news sources""")

st.table(df)
