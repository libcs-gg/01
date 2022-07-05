aa="她们\"闭上了\"眼睛\\或者没有看见?" # 注意：单引号和双引号都只能用于单行情况，如果换行则报错
bb= 'I\'ll be a good person' #
hh='这里有个双引号\"\b请补'# \b表示将光标的位置回退一位
dd= "这里有个双引号\"\n我忘了！"
ee=" 这里有个双引号\"\r不错哦" #\r表示将光标的位置回退到本行的开头位置
ff= '这里有个双引号\t \" \t请补'#\t表示4个空格
t = 12
print('%s,%s,\n %s,%d'%(aa,bb,dd,t))



# % 格式化：str % ()
print('%s%d'%('数字：',0))
print('%d，%d'%(0,1))
print('%d，%d，%d'%(0,1,0))

name1 = 'Python'
print('I am learning %s'% name1)  # 注：当只跟一个数据时，%后可不加括号，format()一定要有。


# format()格式化函数：str.format()
print('\n{}{}'.format('数字：',0))  # 优势1：不用担心用错类型码。
print('{}，{}'.format(0,1))  # 不设置指定位置时，默认按顺序对应。
print('{1}，{0}'.format(0,1))  # 优势2：当设置指定位置时，按指定的对应。
print('{0}，{1}，{0}'.format(0,1))  # 优势3：可多次调用format后的数据。

name2 =  'Python基础语法'
tt = True
print('我正在学{}'.format(name2))  # format()函数也接受通过参数传入数据。
print('我正在学{},{},{}'.format(name2,2021,tt))  # format()函数也接受通过参数传入数据。
