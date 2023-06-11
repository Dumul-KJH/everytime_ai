# 단어 토큰화 시키는 프로그램
import pandas as pd
from konlpy.tag import Okt

# Okt 형태소 분석기 인스턴스 생성
okt = Okt()

# CSV 파일 불러오기
df = pd.read_csv('everytime_hotarticle_merged.csv')

# 'Title', 'Content', 'Comments' 열을 토큰화
df['Title'] = df['Title'].fillna('')
df['Title'] = df['Title'].apply(okt.morphs)
df['Content'] = df['Content'].apply(okt.morphs)
df['Comments'] = df['Comments'].fillna('')
df['Comments'] = df['Comments'].apply(okt.morphs)

# 결과를 CSV 파일로 저장
df.to_csv('tokenized_data.csv', index=False)
