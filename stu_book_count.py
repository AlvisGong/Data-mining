#-*-coding:utf-8-*-
import time
import xlwt
import collections 

_Count_Line =0
Top_Count = 100
books_list=[]
stus_list=[]
result_book = {}
result_stu = {}

workbook = xlwt.Workbook(encoding = 'gbk')
Stusheet = workbook.add_sheet('My Stusheet')
Booksheet = workbook.add_sheet('My Booksheet') 

def sort_by_count(d):  
    #字典排序  
    d = collections.OrderedDict(sorted(d.items(), key = lambda t: -t[1]))  
    return d  

file_object = open("borrowhis.txt","r")  
_All_Line = file_object.readlines()  
file_object.close




_Len_Line = len(_All_Line)

print _Len_Line

while _Count_Line<_Len_Line:
		_Str = _All_Line[_Count_Line]  
		words =_Str.split(",")
		if 	words[4]=='True' and words[9] !='' :
			books_list.append(words[9])
			if words[10] !='' and words[3]!='':
				stus_list.append(words[3])	
		_Count_Line+=1
		
for book in books_list:
    if book not in result_book:  
        result_book[book] = 0  
    result_book[book] += 1 
	
for stu in stus_list:
    if stu not in result_stu:  
        result_stu[stu] = 0  
    result_stu[stu] += 1 

res_books=sort_by_count(result_book)	
res_stus=sort_by_count(result_stu)


books=res_books.items()
stus=res_stus.items()

i=0
for key,value in books:
	if i<Top_Count:
		str1=key
		str2=value
		str1.decode('gbk')
		Booksheet.write(i, 0, label = str1)
		Booksheet.write(i, 2, label = str2)
		i+=1
	else :
		break
		
j=0
for key,value in stus:
	if j<Top_Count:
		str1=key
		str2=value
		str1.decode('gbk')
		Stusheet.write(j, 0, label = str1)
		Stusheet.write(j, 2, label = str2)
		j+=1
	else :
		break
	
		
workbook.save('Excel_StusBooks.xls')		
print "finished!"