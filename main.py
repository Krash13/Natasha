import xlrd
path=input("Введите путь к файлу c тегами: ")
f=open(path,"r")
tags=f.read()

file=input("Введите путь к файлу xls: ")
rb = xlrd.open_workbook(file,formatting_info=True)
number=int(input("Введите номер нужного листа: "))
sheet = rb.sheet_by_index(number-1)
number=int(input("Введите номер строки с тегами: "))
tags_file=sheet.row_values(number-1)

tags_file=tags_file[1:]
n=1
numbers=[]
for t in tags_file:
    if tags.find(t)>=0:
        numbers.append(n)
    n+=1

f=open("NUMBERS.txt","w")
for n in numbers:
    f.write(str(n)+"\n")
