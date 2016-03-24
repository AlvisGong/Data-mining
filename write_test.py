# -*- coding: utf-8 -*-  
import csv
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )

file = open("d:\\brand.csv", "wb+")  
file.write('\xEF\xBB\xBF');  
writer = csv.writer(file) 

str1='快速突破英语专业八级词汇10000 kuai su tupo ying yu zhuan ye ba ji ci hui 10000 张福元主编'
str2='201420070702'
_Count_Line =0

print('Read Start ----')

while _Count_Line<10:
	fieldList =[];
	fieldList.append(str2);
	fieldList.append(str1);
	writer.writerow(fieldList)
	_Count_Line+=1

file.close()