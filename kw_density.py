import streamlit as st
import re

st.markdown("<h1 style='text-align: center;'> Keyword Density Checker </h1>",unsafe_allow_html=True)
st.markdown("---",unsafe_allow_html=True)
text=st.text_area("Enter your Paragraph Here")
col1,col2,col3=st.columns(3)
dict=dict()
if text:
    col1.markdown("<h6 style='text-align: center ;'>Keywords</h6>",unsafe_allow_html=True)
    col2.markdown("<h6 style='text-align: center ;'>Frequency</h6>",unsafe_allow_html=True)
    col3.markdown("<h6 style='text-align: center ;'>Percentage</h6>",unsafe_allow_html=True)
    preprocess=re.sub("[^a-zA-Z0-9]", " ", text)
    words=preprocess.lower().split(" ")
    totalwords=len(words)
    for word in words:
        if word in dict:
            dict[word]+=1
        else:
            dict[word]=1
    keys=list(dict.keys())
    values=list(dict.values())
    for i in range(len(keys)):
        col1.markdown("<h6 style='text-align: center ;'>"+keys[i]+"</h6>",unsafe_allow_html=True)
        col2.markdown("<h6 style='text-align: center ;'>"+str(values[i])+"</h6>",unsafe_allow_html=True)
        col3.markdown("<h6 style='text-align: center;'>{}%</h6>".format(round((values[i]/totalwords)*100)), unsafe_allow_html=True)
