#csv파일 읽기
import csv

file_name = './busanbus.csv'

f = open(file_name, mode = 'r', encoding = 'cp949')
reader = csv.reader(f, delemiter=',') # 구분자가 , 일 경우

next(reader) #제목줄 있을때 필요없을 경우
for line in reader:
    print(line)

f.close()