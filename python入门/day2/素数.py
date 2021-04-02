for i in range(2, 100 + 1):
    if i == 2:
        print(i, "是素数")
    for j in range(2, i):
        if (i % j) == 0:  # 就表明不是素数
            break
        if j + 1 == i:
            print(i, "是素数")

print("======================================================")

# 第二种写法：
for i in range(2, 100 + 1):
    isPrimeNum = True  # 假设i是一个素数
    for j in range(2, i):
        if (i % j) == 0:  # 就表明不是素数
            isPrimeNum = False  # 走到这里就表名此时的i不是一个素数
            break
    if isPrimeNum:
        print(i, "是素数")
