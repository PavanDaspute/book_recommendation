#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pickle
import pandas as pd


# In[3]:


def recommend(book_name):
    books_index = books[books['title'] == book_name].index[0]
    distances = similarity[books_index]
    books_list = sorted(list(enumerate(distances)),reverse = True, key = lambda x:x[1])[1:6]
    
    rec_books = []
    for i in books_list:
        rec_books.append(books.iloc[i[0]].title)
    return rec_books

books_dict = pickle.load(open(r'C:\Users\PAVAN\book_recommendation_project\books_dict.pkl', 'rb'))
books = pd.DataFrame(books_dict)

similarity = pickle.load(open(r'C:\Users\PAVAN\book_recommendation_project\similarity.pkl', 'rb'))
st.title('Movie Recommender System')
option = st.selectbox('Select your Movie:', books['title'].values)

if st.button('Recommend'):
    recommendations = recommend(option)
    for i in recommendations:
        st.write(i)
    

