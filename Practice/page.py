import streamlit as st
import requests


apikey = "DaegWBnQMgNKE3OnJZ2Q45bKp1rHwJsCsuXQ2DD2"

url = "https://api.nasa.gov/planetary/apod?api_key=DaegWBnQMgNKE3OnJZ2Q45bKp1rHwJsCsuXQ2DD2"

pics = "https://api.nasa.gov/assets/img/general/apod.jpg"

response1= requests.get(url)
data = response1.json()

print(data)

title = data["title"]
image = data["url"]
explanation = data["explanation"]

image_path = "img.png"
response2 = requests.get(image)

with open(image_path,"wb") as file:
    file.write(response2.content)

st.header(title)
st.image(image_path)
st.write(explanation)