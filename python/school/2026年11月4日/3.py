for num in range(100,1000):
    hundred = num//100 #取百位数
    decade = num // 10 % 10#取十位数
    unit = num % 10#取十位数
    if (hundred ** 3) + (decade ** 3) + (unit ** 3) == num:
        print(f'发现水仙花数{num}')