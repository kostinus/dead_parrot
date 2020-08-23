f = open("parsing.txt", encoding="UTF")

line = [line.split() for line in f]
data_line = [data_line for data_line in line if len(data_line) > 0]    # Оставляем в списке только непустые строки.

column1 = list()
column2 = list()
column3 = list()
column4 = list()


for row in data_line:
    try:
        column1.append(int(row[0]))
    except:
        pass
    try:
        column2.append(int(row[1]))
    except:
        pass
    try:
        column3.append(int(row[2]))
    except:
        pass
    try:
        column4.append(int(row[3]))
    except:
        pass

column1.sort()
column2.sort()
column3.sort()
column4.sort()

print(column1[len(column1)-3:len(column1)])
print(column2[len(column2)-3:len(column2)])
print(column3[len(column3)-3:len(column3)])
print(column4[len(column4)-3:len(column4)])