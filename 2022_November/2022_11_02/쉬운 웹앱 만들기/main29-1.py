#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

#차트에 넣을 데이터 생성
data_list = {1,2,3,4,5,6,7,8,9,10}
st.write('''
샘플데이터
''')

#차트를 생성합니다.
st.line_chart(data_list)


# In[ ]:




