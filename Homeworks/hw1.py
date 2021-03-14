oddnumbers = [1,3,5,7,9]
evennumbers = [2,4,6,8]
oddnumbers.extend(evennumbers)
new_list = [i*2 for i in oddnumbers]
new_list.sort()
for k in new_list:
    print(f'Value: {k}, Type: {type(k)}')