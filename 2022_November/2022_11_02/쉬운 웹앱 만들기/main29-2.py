#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import datetime

#달력으로 날짜 입력받기
d = st.date_input("날짜를 선택하세요",datetime.date.today())

#선택한 날짜 출력
st.write('선택한 날짜:',d)

