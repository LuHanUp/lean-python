import string as string

# 字符串加密
source = "123456"
output = "abcdef"
password_table = str.maketrans(source, output)  # 生成密码本

msg = "236".translate(password_table)  # 对"236"进行加密/解密
print(msg)

source = string.printable  # 返回所有的单字符，包含特殊字符
print(source)

# 统计字符个数程序
while True:
    msg = input(">>:")
    if msg == 'exit':
        break
    int_count = 0
    space_count = 0
    str_count = 0
    special_count = 0
    for i in msg:
        if i.isdigit():
            int_count += 1
        elif i.isspace():
            space_count += 1
        elif i.isalpha():
            str_count += 1
        else:
            special_count += 1
    print(f"str count:{str_count}, int count:{int_count}, space count:{space_count}, special count:{special_count}")
