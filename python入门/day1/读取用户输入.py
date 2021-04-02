name = input("Please input your name:")
age = int(input("Please input your age:"))  # int函数可以将str转成一个int类型
hobbie = input("your hobbie:")
job = input("your job:")

msg = f'''
-------------{name} info--------------
name:{name}
age:{age}，wow still young , in {30 - age} years you will be 30.
hobbie:{hobbie}
job:{job}
--------------------------------------
'''
print(msg)
