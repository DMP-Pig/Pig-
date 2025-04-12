xiao_biao = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
             'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', " ", ',', '，', '.', '!', ":", '(', ')', '_', '-', "’", '?',';','/','0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
wenjianming = input("请输入文件名：")
f = open(wenjianming + ".txt", "r")
key = int(input('请输入密钥(数字):'))
data = f.read(-1)


array = data.split("~")

jieguo = ""
for i in array:
    jieguo += (str(xiao_biao[int(i) - 1 - key]))
print(jieguo)
f.close()
