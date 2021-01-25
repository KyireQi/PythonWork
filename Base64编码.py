def init():
    for i in range(0,26):
        lis.append(chr(i + 65))
    for i in range(0,26):   
        lis.append(chr(i + 97))
    for i in range(0,10):
        lis.append(chr(i + 48))
    lis.append('+')
    lis.append('/')

lis = []
init()

def Encode():
    s = input()
    ans = ""
    res = ""
    temp = 0
    if len(s) % 3 != 0:
         temp = 3 - len(s) % 3
    for char in s:
        flg = bin(ord(char))[2:]
        flg = flg.zfill(8)
        res += flg 
    if len(res) % 6 != 0:
        res = res.ljust(6 - len(res) % 6 + len(res),'0')
    for i in range(0,len(res),6):
        ans += lis[int(res[i : i + 6],base = 2)]
    for i in range(0,temp):
        ans += '='
    return ans

def Decode():
    ans = ""
    res = ""
    deco = input()
    for char in deco:
        if char != '=':
            res += bin(lis.index(char))[2:].rjust(6,'0')
    
    for k in range(0,len(res),8):
        ans += chr(int(res[k:k + 8],base = 2))
    
    return ans

while(1):
    judge = int(input("Please Choose Your Instruction:"))
    if(judge == 3) : break
    elif(judge == 2) :
        print(Encode())
        # print(ans)
    elif(judge == 1) :
        print(Decode())