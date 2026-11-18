for row in range(1, 10):
    # print(f'{row}行')
    for item in range(1,row + 1):
        # num = item * row
        print(f"{item}*{row}={item * row}",end="\t")
    print("\n")