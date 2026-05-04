my_split = date.split()

for i in my_split:

    my_date_list.append(i)

revarse_date = my_date_list[::-1]

year = int(revarse_date[0])

month = int(revarse_date[2])

day = int(revarse_date[1])

day_num = calendar.weekday(year,month,day)

my_day = []

for i in calendar.day_name[day_num] :

    my_day.append(i)

print("".join(my_day).upper())
