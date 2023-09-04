
temp1 = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
temp2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 20, 20]
check = []
for n, m in zip(temp1, temp2):
    if m - 5.0 <= n <= m + 5.0:
        check.append(0)
    else:
        check.append(1)
print(check)
if len(check) > 2:
    yepCOCK = round((check.count(1) / len(check))*100)
    print("percentage", yepCOCK)
else:
    print('list too short')
if yepCOCK > 80:
    print("YOU ARE WASTING WATER")
else:
    print("NO WATER WASTE DETECTED")
