# -*- coding: utf-8 -*-
import sys
import xlwt
reload(sys)
sys.setdefaultencoding('utf8')

workbook = xlwt.Workbook(encoding = 'gbk')
worksheet = workbook.add_sheet('My Worksheet')



file_object = open("borrowhis.txt","r")  
_All_Line = file_object.readlines()  
file_object.close

col = 0
str1=''
str2=''
str3=''
str4=''
_Count_Line =0
_Len_Line = len(_All_Line)

while _Count_Line<100:
#	fieldList =[];words[4] !='' and 'Ture' in words[4]  and 
	_Str = _All_Line[_Count_Line]  
	words =_Str.split(",")
	if( words[3] != '' and  words[9] != '' and words[10] != ''and words[6] != '' and '2011' in words[6][0:4]):
#		print words[4]
		str1 = words[3]
		str2 = words[9]
		str3 = words[10]
		str4 = words[6]
		str1.decode('gbk')
		str2.decode('gbk')
		str3.decode('gbk')
		str4.decode('gbk')
		worksheet.write(col, 0, label = str1)
		worksheet.write(col, 1, label = str3)
		worksheet.write(col, 2, label = str2)
		worksheet.write(col, 3, label = str4)
		col+=1
#	fieldList.append(str1)
#	fieldList.append(str2)
#	writer.writerow(fieldList)
	_Count_Line+=1


workbook.save('Excel_Workbook.xls')

print 'success!'