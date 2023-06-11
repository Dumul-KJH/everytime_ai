#길이제한 해주는 프로그램 GPT3 최대 2048개의 토큰 처리 가능 -> 모두 다 사용 가능함
import pandas as pd

# CSV 파일 불러오기
df = pd.read_csv('tokenized_data.csv')

# 토큰화된 'Title', 'Content', 'Comments' 길이를 각각 계산
df['Total_tokens'] = df['Title'].apply(lambda x: len(str(x).split())) + df['Content'].apply(lambda x: len(str(x).split())) + df['Comments'].apply(lambda x: len(str(x).split()))

# 토큰 개수가 2048개 미만인 행만 남기기
df = df[df['Total_tokens'] < 2048]

# 삭제된 데이터를 별도의 CSV 파일로 저장
deleted_df = df[df['Total_tokens'] >= 2048]
deleted_df.to_csv('deleted_data.csv', index=False)

# 필요한 필드만 선택하여 새로운 데이터프레임 생성
filtered_df = df[['Title', 'Content', 'Comments']]

# 결과를 CSV 파일로 저장
filtered_df.to_csv('everytime_hotarticle_filtered.csv', index=False)
