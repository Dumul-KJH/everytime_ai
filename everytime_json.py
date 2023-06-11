#json 파일 만들기
import pandas as pd
import json
import math

# CSV 파일 읽기
df = pd.read_csv('everytime_hotarticle_merged.csv')

# 좋아요 수를 반올림하여 반복 횟수 결정
df['likes_rounded'] = df['Number of Likes'].apply(lambda x: math.ceil(float(x)))

# 빈 리스트 생성
data_list = []

# 각 행에 대해
for _, row in df.iterrows():
    # 좋아요 수에 비례하여 반복
    for _ in range(row['likes_rounded']):
        # 원하는 형식의 dict 생성
        data_dict = {
            "prompt": f"제목: {row['Title']}, 내용: {row['Content']}",
            "completion": row['Comments']
        }
        # 리스트에 추가
        data_list.append(data_dict)

# JSON 파일로 저장
with open('dataset.json', 'w', encoding='utf-8') as f:
    json.dump(data_list, f, ensure_ascii=False, indent=4)
