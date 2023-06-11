#comment 필드를 하나로 합치는 프로그램
import csv

input_filename = 'everytime_hotarticle_quoted.csv'
output_filename = 'everytime_hotarticle_merged.csv'

# CSV 파일 읽기
with open(input_filename, 'r', newline='', encoding='utf-8') as in_file:
    reader = csv.reader(in_file)
    data = list(reader)

# 6번째 필드 이후의 모든 필드를 한 필드로 합치기
merged_data = []
for row in data:
    new_row = row[:5]  # 처음 5개 필드 가져오기
    new_row.append(','.join(row[5:]))  # 6번째 필드 이후의 모든 필드를 한 필드로 합치기
    merged_data.append(new_row)

# 결과를 새 CSV 파일에 쓰기
with open(output_filename, 'w', newline='', encoding='utf-8') as out_file:
    writer = csv.writer(out_file, quoting=csv.QUOTE_ALL)
    writer.writerows(merged_data)
