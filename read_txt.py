#-*-coding:utf-8-*-
import time

file_object = open("borrowhis.txt","r")  
_All_Line = file_object.readlines()  
file_object.close

_Count_Line =0

books_list=[]
result_book = {}
result_stu = {}
_Len_Line = len(_All_Line)
    
_Ex_Str = ''

print _Len_Line

while _Count_Line<_Len_Line:
		_Str = _All_Line[_Count_Line]  
		words =_Str.split(",")
		if ( _Count_Line>0 and _Count_Line<1000 and words[4]=='True'):
#			print _Str
			books_list.append(words[9])
				
		_Count_Line+=1
		
for book in books_list:
    if book not in result_book:  
        result_book[book] = 0  
    result_book[book] += 1 
	
for key,value in  result_book.items():  
    print key + "    :%d" % value 
		
		
print "finished!"