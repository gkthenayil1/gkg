#!/usr/bin/env python
# coding: utf-8

# In[6]:


import streamlit as st
import pandas as pd
import numpy as np
def div(a, b):
  return a / b

st.title('Simple division')
a = st.number_input('Enter a number')
b = st.number_input('Enter another number',value=1.00)
st.write("your answer is ",div(a, b))








