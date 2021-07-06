import csv
from tkinter import filedialog

folder = filedialog.askopenfilename(title='open')
with open(folder, encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter = ",")
    i = 0
    size = 0
    date = []
    name = []
    hour = []

    # Створюю список заголовка
    date.append("Name / Date")
    for row in file_reader:
        if row[1] in date or i==0 :
            i += 1
        else:
            date.append(str(row[1]))
    r_file.close

    #Список унікальних імен
with open(folder, encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter = ",")
    i = 0
    for row in file_reader:
        if row[0] in name or i==0 :
            i += 1
        else:
            name.append(str(row[0]))
    r_file.close

    #Список годин роботи 
with open(folder, encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter = ",")
    i = 0
    for row in file_reader:
        if size==0 :
            size += 1
        else:
            h = list()
            h.append(str(row[0]))
            h.append(str(row[1]))
            h.append(str(row[2]))
            hour.append(h)
            size += 1
    hour_T = [] 
    name_hour = [] 
    i = 0
    j = 0
    d = 1
#    print(hour)
    while(True):
        hour_T = [0] * (len(date)-1)
#        print(j)
        hour_T.insert(0, name[j]) 
        while(True):
            if hour[i][0] == name[j]:
                ind = date.index(hour[i][1])
                hour_T.insert(ind, hour[i][2]) 
#                 print(hour[i][1])
            i += 1
            if i == size-1: 
                i = 0
                break
        while(len(hour_T)>len(date)):
            hour_T.pop()
        name_hour.append(hour_T)
        j += 1
        d += 1
        if j == len(name): 
            break
#print(name_hour)
newstr = folder.replace(".csv", "_test.csv")

with open(newstr, mode="w", encoding='utf-8') as w_file:            
    file_writer_date = csv.writer(w_file, delimiter = ",", lineterminator="\r")
    file_writer_date.writerow(row for row in date)
    file_writer_name = csv.writer(w_file, delimiter = ",", lineterminator="\r")
    for row in name_hour:
        file_writer_name.writerow(row)