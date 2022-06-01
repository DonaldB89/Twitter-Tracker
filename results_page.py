import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title("Twitter Tracker")

st.write("""### The latest trending news sources""")

st.table(df)
