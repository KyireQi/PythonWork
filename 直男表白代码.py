confession = 'Honey I Love You'

message = ""
for char in confession :
    number = ord(char)
    message += hex(number)[2:] #'0x49'去掉的0x
print(message)

answer = ""
i = 0
while i < len(message):
    s = message[i : i + 2]
    a = int(s,base = 16)
    answer += chr(a)
    i = i + 2
print(answer)