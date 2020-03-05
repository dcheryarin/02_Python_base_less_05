result = {}
with open("exercise6.txt", encoding="utf-8") as f_obj:
    for line in f_obj:
        subject_name = line.split(':')[0]
        hours_string = line.split()[1:]
        #        print(subject_name)
        #        print(hours_string)
        result[subject_name] = 0
        hour_sum = 0
        for hours in hours_string:
            hour = hours.split('(')[0]
            if hour != '—':
                hour_sum += int(hour)
        #        print(hour_sum)
        result[subject_name] += hour_sum
print(result)
