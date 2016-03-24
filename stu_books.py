# -*- coding: utf-8 -*-
import sys
import xlwt
import time
import collections  

reload(sys)
sys.setdefaultencoding('utf8')

workbook = xlwt.Workbook(encoding = 'gbk')
worksheet = workbook.add_sheet('My Worksheet')

def sort_by_count(d):  
    #字典排序  
    d = collections.OrderedDict(sorted(d.items(), key = lambda t: -t[1]))  
    return d  

file_object = open("borrowhis.txt","r")  
_All_Line = file_object.readlines()  
file_object.close

_Count_Line =0

result={}

_Len_Line = len(_All_Line)
    
_Ex_Str = ''

print _Len_Line

while _Count_Line<_Len_Line:
		_Str = _All_Line[_Count_Line]  
		words =_Str.split(",")
#words[3] :number;words[9]:book name;words[10]:stu name
		if ( words[4]=='True' and words[10] !='' and words[3] !=''):
			key = words[10]
			value=words[9]
			result.setdefault(key,[]).append(value) 
		_Count_Line+=1
	

i=0
for key,value in result.items():
	if i<100:
		str1=key
		str2=''
		for m in value:
			str2+=m+'\n'
		str1.decode('gbk')
		str2.decode('gbk')
		worksheet.write(i, 0, label = str1)
		worksheet.write(i, 1, label = str2)
		i+=1
	else :
		break
			
workbook.save('Excel_Stu_books.xls')		
print "finished!"