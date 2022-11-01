#!/usr/bin/env python
# coding: utf-8

pip install pyautogui
# 
# #마우스와 키보드를 자동으로 제어하기 위한 pyautogui 라이브러리 설치


# 
# #클립보드 값을 복사하거나 붙여넣기 위해 사용되는 라이브러리 설치
# 
# #pyautogui에는 한글이 지원되지 않으므로 검색에 필요한 한글을 클립보드를 이용해 사용하기 위해 사용합니다.
# #아나콘다 사용시 기본으로 설치되어있음

# 
# #schedule 라이브러리는 일정시간마다 함수를 동작시킬 때 사용됩니다.

# In[1]:
pip install pyautogui
pip install pyperclip 
pip install schedule 

import pyautogui
import os

#경로를  .py파일의 실행경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#mypic1.png와 동일한 그림을 찾아 좌표를 출력합니다.
picPosition = pyautogui.locateOnScreen('mypic1.png') 
print(picPosition)

#앞에서 사진을 찾지 못했다면 mypic2.png와 동일한 그림을 찾아 좌표를 출력합니다.
if picPosition is None:
    picPosition = pyautogui.locateOnScreen('mypic2.png') 
    print(picPosition)

#앞에서 사진을 찾지 못했다면 mypic3.png와 동일한 그림을 찾아 좌표를 출력합니다.
if picPosition is None:
    picPosition = pyautogui.locateOnScreen('mypic3.png')
    print(picPosition)


# In[ ]:





# In[ ]:




