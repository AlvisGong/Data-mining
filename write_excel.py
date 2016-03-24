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

_Count_Line =0
_Len_Line = len(_All_Line)

while _Count_Line<1000:
#	fieldList =[];
	_Str = _All_Line[_Count_Line]  
	words =_Str.split(",")
	str1 = words[3]
	str2 = words[9]
	str1.decode('gbk')
	str2.decode('gbk')
	worksheet.write(_Count_Line, 0, label = str1)
	worksheet.write(_Count_Line, 2, label = str2)
#	fieldList.append(str1)
#	fieldList.append(str2)
#	writer.writerow(fieldList)
	_Count_Line+=1


workbook.save('Excel_Workbook.xls')