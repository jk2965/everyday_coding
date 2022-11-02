#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import datetime
import pyupbit

#달력으로 날짜를 입력받습니다.
d = st.date_input(
"날짜를 선택하세요",
datetime.date.today())


st.write('비트코인 일일차트')

#비트코인의 1시간 데이터를 24개 가져옵니다.
ticker = "KRW-BTC"

interval = 'minute60'

#입력한 날짜에 하루를 더해줍니다.
#이전 데이터 24개를 가지고 오기 때문에 만약 12월 6일의 값을 알고 싶다면 
#12월 7일부터 이전 24개의 데이터를 가지고 오면 됩니다.
to= str(d+datetime.timedelta(days=1))
count = 24
price_now = pyupbit.get_ohlcv(ticker=ticker,interval=interval,to=to,count=count)

#그래프를 그려줍니다.
st.line_chart(price_now.close)


# In[ ]:




