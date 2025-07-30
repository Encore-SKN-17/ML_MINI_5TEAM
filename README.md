# SK네트윅스 Family AI 캠프 17기 ML Project MINI_5TEAM #

# 1. 팀 소개
### 👉 팀명 : 로켓단
로켓처럼 정상을 향해 날아오르겠다는 의미를 담은 팀명명
<br>
<br>

### 👉 팀원 소개 
|이름|사진|이름|사진|이름|사진|
|:---|---|:---|---|:---|---|
|[김태완](https://github.com/Kicangel)|<img src="https://github.com/Encore-SKN-17/EDA_MINI_5TEAM/blob/main/image_1/%EB%A1%B1%EC%8A%A4%ED%86%A42.jpg" width="150" height="400"/>|[이재은](https://github.com/JAEEUN0129)|<img src="https://github.com/Encore-SKN-17/EDA_MINI_5TEAM/blob/main/image_1/%EC%83%A4%EB%AF%B8%EB%A5%B4.jpg" width="150" height="400"/>|[임산별](https://github.com/ImMountainStar)|<img src="https://github.com/Encore-SKN-17/EDA_MINI_5TEAM/blob/main/image_1/%ED%8C%8C%EC%B9%98%EB%A6%AC%EC%8A%A4.jpg" width="150" height="400"/>|
|[양송이](https://github.com/songeeeey)|<img src="https://github.com/Encore-SKN-17/EDA_MINI_5TEAM/blob/main/image_1/%ED%91%B8%ED%81%AC%EB%A6%B0.jpg" width="150" height="400"/>|[전상아](https://github.com/sang-a-le)|<img src="https://github.com/Encore-SKN-17/EDA_MINI_5TEAM/blob/main/image_1/%ED%8E%AD%ED%83%9C%EC%9E%90.jpg" width="150" height="400"/>|

------
<br>
<br>

# 2. 프로젝트 개요

## 👉 2.1 프로젝트 명 
### {프로젝트 명 쓰세요}
- 기간 : 2025.07.26 ~ 2025.08.01
<br>

<br>

## 👉 2.2 프로젝트 필요성 및 목적
### 2.2.1 프로젝트 배경
**(1) 혼잡도의 사회적 문제**  
- 국토교통부 조사에 따르면, 수도권 지하철은 **평일 출근 시간대 평균 혼잡도가 150%를 초과하는 구간이 다수 존재**한다 *(서울연구원, 2023)*.  
- 혼잡도로 인해 시민들의 스트레스는 물론 **재난·사고 시 대피 지연과 안전사고 증가로 이어질 수 있다**.
<br>

**(2) 기상 조건의 영향**  
- 최상기 외(2013)는  
  > “강우량과 체감온도는 대중교통 수요 감소와 높은 상관관계를 보이며,  
  > 특히 **버스 이용률은 기상 악화 시 7% 이상 감소**하는 것으로 나타났다.”
  </p><img width="4400" height="2534" alt="설문조사_그래프" src="https://github.com/user-attachments/assets/06aeadea-4988-41af-a5a0-7a8864b5cfac" />
  <sub>출처: <a href="https://blog.naver.com/kma_131/220996892740">기상청 블로그</a> & 최상기(2021) *기상조건에 따른 대중교통 수요변화에 관한 연구*</sub>

 

<br>

**(3) 기존 대중교통 서비스의 한계**  
- 네이버 지도, 카카오 지도 등 주요 대중교통 안내 서비스는  
  - 도착 시간/환승 횟수 등 **거리·시간 중심의 경로 추천만 제공**  
  - 기상 정보는 단순 기온 제공에 그쳐, **날씨 조건에 따른 혼잡도 변화 정보는 부재**
  <img width="4400" height="2534" alt="서비스_비교" src="https://github.com/user-attachments/assets/e78dee02-5ffc-4727-a1f8-7012ec3347bf" />
  
    <br>
- 실제로 많은 이용자들이 날씨에 따라 경로 변경을 고민하지만 이를 돕는 정보는 부족  
  - 설문조사(최상기 외, 2013):  
    **우천 시 출근길 경로 변경 경험 40% 이상**
    


<br>
<br>

### 2.2.2 프로젝트 필요성
- 지하철 혼잡도는 **시민 안전과 직결되는 데이터**  
- **기상 요인을 반영한 예측 시스템이 현재 부재**  
- 이용자들은 날씨별 혼잡도 정보를 통해 **최적 이동 루트** 를 제공
> **⇒ 혼잡도 + 기상 요인을 반영한 예측 시스템 구축 필요**

---

<br>
<br>

### 2.3 프로젝트 목적
**(1) 기상 요인과 지하철 혼잡도 간 관계 분석**  
- 2019~2024년 서울시 지하철 **호선별 일별 승차 인구 데이터 기반 분석**  
- 강수량, 기온, 습도 등 기상 요소와 혼잡도의 정량적 관계 도출  
- 호선별·시간대별 혼잡도 변동 패턴 파악 → **기상 조건별 혼잡도 예측 가능성 확보**
<br>

**(2) 지하철 혼잡도 예측 모델 개발**  
- 기상 데이터와 다년간 지하철 이용 데이터를 결합  
- **호선별 혼잡도 예측 모델 구축**  
- 평일 데이터 기준 분석으로 요일 효과 최소화 & **기상 조건 영향 명확 식별**
<br>

**(3) 이용자 중심 서비스 기획**  
- 예측 모델 결과를 기반으로 지도 어플리케이션(네이버 지도, 카카오 지도 등)에  
  **날씨 조건을 반영한 맞춤형 최적 경로 추천 서비스** 기획  


<br>
<br>

## 3. 데이터 

### 3.1 서울시 지하철 호선별 승하차 수 데이터 
- 데이터 출처 :
- 데이터 설명 :
    - 기간 :
    - 데이터 규모 :
- 주요 변수 : 
<br>

### 3.2 기상 데이터 
  - 데이터 출처 :
  - 데이터 설명
      - 기간 :
      - 데이터 규모 :
  - 주요 변수 :
     
<br>
<br>

-----
# 4. 기술 스택
|Python|Github|Pandas|Matplotlib|
|---|---|---|---|
|<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">|<img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"> <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">|<img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white">|<img src='https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black'>|

<br>
<br>

-----
# 5. 전처리과정

### 5.1 기상 데이터 전처리 
<br>

### 5.2 지하철 승하차 인구 데이터 전처리 
<br>

-----
<br>
<br>

# 6. 머신러닝 



---
<br>
<br>

# 7. 서비스 구현 
### 7.1 고객 여정 지도를 통한 서비스 시현 

<br>

### 7.2 Streamlit 구현 


<br>
<br>
---- 

# 8. 기대효과 
## **(1) 대중교통 운영 및 정책 측면**  
- 혼잡도 예측에 따른 **경찰·안전 인력 효율적 배치** 가능  
- 기상 악화 시 예상되는 혼잡 구간을 사전 식별 → **선제적 대응 가능**  
- 교통 병목 완화 및 **도시 전체 교통 효율성 향상**

<br>

## **(2) 이용자 서비스 측면**  
- 주요 시간대에 **날씨별 혼잡도 반영 최적 경로 추천 제공**  
- 지도 앱에서 `쾌적성(혼잡도)` + `효율성(소요시간)` 동시 고려한 루트 제안  
- 날씨 변화로 인한 이동 스트레스 감소 & **시민 만족도 향상**

