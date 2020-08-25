from prettytable import PrettyTable

f = open("profile_log.txt")

lines = [line.split() for line in f]

for line in lines:
        if "/" in line[0]:
            no_dash = line[0].split("/")
            del line[0]
            line.insert(0, no_dash[0])
            line.insert(1, no_dash[1])
        else:
            line.insert(1," ")

lines[0].insert(1, "primitive_calls")

column1 = {}
column2 = {}
column3 = {}
column4 = {}
column5 = {}
column6 = {}


for line in lines:
    try:
        column1[float(line[0])] = line
        column2[float(line[1])] = line
        column3[float(line[2])] = line
        column4[float(line[3])] = line
        column5[float(line[4])] = line
        column6[float(line[5])] = line
    except:
        pass

list_keys1 = list(column1.keys())
list_keys1.sort()
list_keys2 = list(column2.keys())
list_keys2.sort()
list_keys3 = list(column3.keys())
list_keys3.sort()
list_keys4 = list(column4.keys())
list_keys4.sort()
list_keys5 = list(column5.keys())
list_keys5.sort()
list_keys6 = list(column6.keys())
list_keys6.sort()

print("Победители в первой колонке:")
print (lines[0])
for i in list_keys1[len(list_keys1)-3:]:
    print(column1[i])

print("Победители во второй колонке:")
print (lines[0])
for i in list_keys2[len(list_keys2)-3:]:
    print(column2[i])

print("Победители в третьей колонке:")
print (lines[0])
for i in list_keys3[len(list_keys3)-3:]:
    print(column3[i])

print("Победители в четвёртой колонке:")
print (lines[0])
for i in list_keys4[len(list_keys4)-3:]:
    print(column4[i])

print("Победители в пятой колонке:")
print (lines[0])
for i in list_keys5[len(list_keys5)-3:]:
    print(column5[i])

print("Победители в шестой колонке:")
print (lines[0])
for i in list_keys6[len(list_keys6)-3:]:
    print(column6[i])