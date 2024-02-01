#import library
import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image



def run():
    #set title
    st.markdown("<h1 style='text-align: center; color: grey;'>Welcome to the Exploration Data Analysis (EDA)</h1>", unsafe_allow_html=True)
        
    #set header
    st.markdown("<h2 style='text-align: center; color: grey;'>Halaman ini menampilkan hasil EDA dari Brain Tumor</h2>", unsafe_allow_html=True)

    st.write('----')

    # EDA 1
    st.markdown("<h3 style='text-align: center; color: grey;'>Persebaran Data Target Pada Dataframe Train dan Val</h3>", unsafe_allow_html=True)

    image = Image.open('eda11.png')
    st.image(image)
    
    image = Image.open('eda12.png')
    st.image(image)
    
    with st.expander('Explanation'):    
        st.caption("Terlihat distribusi label masing-masing kelas pada target sudah terbilang balanced.")
    st.write('---')

    # EDA 2
    st.markdown("<h3 style='text-align: center; color: grey;'>Melihat perbedaan pada sample target Healthy dan Brain Tumor</h3>", unsafe_allow_html=True)

    image = Image.open('eda2.png')
    st.image(image)
       
    with st.expander('Explanation'):
        st.caption('Jika dilihat dari sample gambar masing-masing kelas yang telah ditampilkan diatas, dapat disimpulkan bahwa gambar-gambar yang ada di dalam dataset ini belum dilakukan proses Data Augmentasi, dikarenakan shape yang masih berbeda-beda.')
    st.write('---')
    
if __name__ == "__main__":
    run()