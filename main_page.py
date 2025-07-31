import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image

# 날씨 데이터 불러오기
weather_df = pd.read_csv('./data/2019_2024_weather.csv', encoding='euc-kr')

# 지하철 데이터 불러오기
# subway_df = pd.read_csv('./data/subway_2019_2024.csv')

#=============================================================================================================
# head
st.header("🌦️날씨별 / 지하철 노선별 혼잡도 알아보기")

#=============================================================================================================
# 지하철 선택

st.divider()
col1, col2 = st.columns(2)

with col1:
    # content
    st.subheader("⬇️ 노선 선택")
    line = st.selectbox('', ['1호선', '2호선', '3호선', '4호선', '5호선', '6호선', '7호선', '8호선', '9호선'])

    if st.button("지하철 노선도 보기"):
        image = Image.open("./data/subway_img.jpg")
        st.image(image)



#=============================================================================================================
# 날씨 선택

with col2:
    st.subheader("⬇️ 날씨 선택")
    st.subheader("")
    st.caption("")

    # 온도 최소, 최댓값 
    min_temp = min(weather_df['AvgTemp(°C)'])
    max_temp = max(weather_df['AvgTemp(°C)'])
    # 온도 입력
    temperature = st.slider("온도를 입력해주세요. (단위: °C)", min_temp, max_temp)

    # 강수량 최소, 최댓값
    min_rain = min(weather_df['Rainfall(mm)'])
    max_rain = max(weather_df['Rainfall(mm)'])
    # 강수량 입력
    rainfall = st.slider("강수량을 입력해주세요. (단위: mm)", min_rain, max_rain)    

    # 습도 최소, 최댓값
    min_humi = weather_df['Humidity(%)'].min()
    max_humi = weather_df['Humidity(%)'].max()
    # 습도 입력
    humidity = st.slider("습도를 입력해주세요. (단위: %)", min_humi, max_humi)  

    _, _, col3 = st.columns(3)

    with col3:
        select_button = st.button("선택하기") 


#=============================================================================================================
# 혼잡도 표시

st.divider()
col11, col22 = st.columns(2)

with col11:
    if select_button == True:
        st.subheader(f"""{line}의 혼잡도🚇
        - 온도: {temperature}°C
    - 강수량: {rainfall}mm
    - 습도: {humidity}%""")

# 예시
def get_congestion_level(congestion):
    if congestion < 30:
        return "여유", "green"
    elif congestion < 60:
        return "보통", "yellow"
    elif congestion < 80:
        return "다소 혼잡", "orange"
    else:
        return "매우 혼잡", "red"


with col22:
    st.subheader("")
    
    if select_button == True:
        congestion_rate = 72.4  # 예측값
        level, color = get_congestion_level(congestion_rate)
        st.write("(예시)")
        st.markdown(f"### 현재 혼잡도는? **{congestion_rate:.1f}%**")
        st.markdown(f"<span style='color:{color}; font-size:24px;'>● {level}</span>", unsafe_allow_html=True)











