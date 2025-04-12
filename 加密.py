wenjianming = input("请输入文件名：")
data = list(input("明文:"))
key = int(input('请输入密钥(数字):'))
f = open(wenjianming + ".txt", "a")
xiao_biao = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
             'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', " ", ',', '，', '.', '!', ":", '(', ')', '_', '-', "’", '?',';','/','0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

needToAdd = False
for i in data:
    if needToAdd: 
        f.write("~")
    f.write(str(xiao_biao.index(i)+1+key))
    needToAdd = True
    #print(i)
print("加密完成")
f.close()
