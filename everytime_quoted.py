# 필드를 따옴표로 묶는 프로그램
import csv

# 입력 파일명과 출력 파일명 지정
input_filename = 'everytime_hotarticle.csv'
output_filename = 'everytime_hotarticle_quoted.csv'

# 입력 파일 읽기
with open(input_filename, 'r', newline='', encoding='utf-8') as in_file:
    reader = csv.reader(in_file)
    data = list(reader)

# 출력 파일에 쓰기 (필드를 따옴표로 묶음)
with open(output_filename, 'w', newline='', encoding='utf-8') as out_file:
    writer = csv.writer(out_file, quoting=csv.QUOTE_ALL)
    writer.writerows(data)
