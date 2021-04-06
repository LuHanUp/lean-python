print("hello\tworld")  # \t为一个制表符，通常一个制表符是4个空格(也就是占用4个字符)
print("helloooo\tworld")  # 为什么这里输出的空格比上面输出的多 是因为o占用了一个字符 所以上面的语句只会输出3个字符的位置，而这一行oooo占用了四个字符，所以\t就会重新开一个制表符来进行占位
print("hello\nworld")  # n---->newline的首字符表示换行
print("hello\rworld")  # world会将hello进行覆盖，\r表示光标回车 就会在w的位置回到h的位置进行书写 就会覆盖hello单词
print("hello\bworld")  # \b是退一个字符，会导致o会被w覆盖
print("老师说：\"大家好\"")

# 原字符，不希望字符串汇总的转义字符起作用，就使用原字符，就是在字符串之前加上r/R
print(r"hello\tworld")
