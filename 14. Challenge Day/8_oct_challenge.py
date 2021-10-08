import streamlit as st
from PIL import Image
import pandas as pd
logo = Image.open("logo.png")
st.sidebar.image(logo, width=100)

st.title("Body Mass Index Study")

st.subheader("Total number of Overweight Men and Women")
img = Image.open("_total_no_men_women_overweight.png")
st.image(img, caption="From the above graph we can observe that 32 men and 36 women are overweight")

st.subheader("more general")
img = Image.open("weight_height_by_bmi.png")
st.image(img, caption="")

st.subheader("")
img = Image.open("weight_height_by_bmi_PLUS_THE_MEAN.png")
st.image(img, caption="")

st.subheader("")
img = Image.open("weight_height_by_bmi_men_only.png")
st.image(img, caption="")

st.subheader("")
img = Image.open("weight_height_by_bmi_women_only.png")
st.image(img, caption="")

st.subheader("")
img = Image.open("men_height.png")
st.image(img, caption="")

st.subheader("")
img = Image.open("men_weight.png")
st.image(img, caption="")

st.subheader("")
img = Image.open("women_height.png")
st.image(img, caption="")

st.subheader("")
img = Image.open("women_weight.png")
st.image(img, caption="")

st.subheader("Average Height and Weight with Respect to the Body Mass Index")
img = Image.open("mean_values_of_weight_and_height.png")
st.image(img, caption="")

st.subheader("")
img = Image.open("means_idontget.png")
st.image(img, caption="")





st.subheader("")
img = Image.open("")
st.image(img, caption="")
