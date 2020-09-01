from prettytable import PrettyTable

f = open("profile_log.txt")

lines = [line.split() for line in f]

# Подправляем строку заголовков.
lines[0].insert(1, "primitive_calls")

# Объединяем в одну колонку текстовые значения, которые в изначальном файле разделены пробелами.
for line in lines[1 : len(lines)]:
    n = 0
    for column in line:
        try:
            int(column[0])
            n = n + 1
        except:
            break
    new_column = ""
    for q in range(n, len(line)):
        new_column = new_column + " " + line[q]
    for q in range(len(line)-1, n-1, -1):
        del line[q]
    line.append(new_column)


# Разделяем на разные ячейки значения, записанные через "/".
for line in lines[1 : len(lines)]:
    if "/" in line[0]:
        no_dash = line[0].split("/")
        del line[0]
        line.insert(0, no_dash[0])
        line.insert(1, no_dash[1])
    else:
        line.insert(1,"0")


# Создаём для каждой колонки таблицы словарь.
column1 = {}
column2 = {}
column3 = {}
column4 = {}
column5 = {}
column6 = {}

for line in lines[1 : len(lines)]:
    try:
        column1[float(line[0])] = line
        column2[float(line[1])] = line
        column3[float(line[2])] = line
        column4[float(line[3])] = line
        column5[float(line[4])] = line
        column6[float(line[5])] = line
    except:
        pass


# Делаем списки из ключей словарей, чтобы их отсортировать.
list_keys1 = list()
list_keys2 = list()
list_keys3 = list()
list_keys4 = list()
list_keys5 = list()
list_keys6 = list()

for key in column1.keys():
    list_keys1.append(key)
list_keys1.sort()
for key in column2.keys():
    list_keys2.append(key)
list_keys2.sort()
for key in column3.keys():
    list_keys3.append(key)
list_keys3.sort()
for key in column4.keys():
    list_keys4.append(key)
list_keys4.sort()
for key in column5.keys():
    list_keys5.append(key)
list_keys5.sort()
for key in column6.keys():
    list_keys6.append(key)
list_keys6.sort()


# Делаем названия столбцов для будущих таблиц. Они должны быть уникальными, поэтому добавляем перед названием порядковый номер.
names = list()
col_num = 1
for column in lines[0]:
    new_name = str(col_num) + "_" + column
    names.append(new_name)
    col_num = col_num + 1


# Выведем строки с наибольшими значениями в каждом из числовых столбцов.
my_table1 = PrettyTable()
my_table1.field_names = names
for i in list_keys1[len(list_keys1) - 3 :]:
    my_table1.add_row(column1[i])
print("Победители в первой колонке:")
print(my_table1)

my_table2 = PrettyTable()
my_table2.field_names = names
for i in list_keys2[len(list_keys2) - 3 :]:
    my_table2.add_row(column2[i])
print("\nПобедители во второй колонке:")
print(my_table2)

my_table3 = PrettyTable()
my_table3.field_names = names
for i in list_keys3[len(list_keys3) - 3 :]:
    my_table3.add_row(column3[i])
print("\nПобедители в третьей колонке:")
print(my_table3)

my_table4 = PrettyTable()
my_table4.field_names = names
for i in list_keys4[len(list_keys4) - 3:]:
    my_table4.add_row(column4[i])
print("\nПобедители в четвёртой колонке:")
print(my_table4)

my_table5 = PrettyTable()
my_table5.field_names = names
for i in list_keys5[len(list_keys5) - 3:]:
    my_table5.add_row(column5[i])
print("\nПобедители в пятой колонке:")
print(my_table5)

my_table6 = PrettyTable()
my_table6.field_names = names
for i in list_keys6[len(list_keys6) - 3:]:
    my_table6.add_row(column6[i])
print("\nПобедители в шестой колонке:")
print(my_table6)