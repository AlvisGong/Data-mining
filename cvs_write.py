# -*- coding: utf-8 -*-  
import csv
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

file = open("d:\\brand.csv", "wb+")  
file.write('\xEF\xBB\xBF');  
writer = csv.writer(file) 

file_object = open("borrowhis.txt","r")  
_All_Line = file_object.readlines()  
file_object.close

_Count_Line =0
_Len_Line = len(_All_Line)

writer.writerow(['szReaderID' ,'szBookID'])

reader = csv.reader(file)

print('Read Start ----')

while _Count_Line<10:
	fieldList =[];
	_Str = _All_Line[_Count_Line]  
	words =_Str.split(",")
	str1 = words[3]
	str2 = words[9]
	writer.writerow([str1,str2])
#	fieldList.append(str1)
#	fieldList.append(str2)
#	writer.writerow(fieldList)
	_Count_Line+=1

file.close()