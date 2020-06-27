def say_myself(name, age, man=True):
    print("이름 : %s" %name)
    print("나이 : %d" %age)
    if man:
        print("남자")
    else:
        print("여자")

say_myself("도라에몽",25)
dictionary = { 
	
	"level":"1",
        "hp":"100",
	"items":["대나무헬리콥터","빅라이트","어디로든 문 "],
        "skill":"펀치"
       
	
}

 
print("level :",dictionary["level"])
print("hp :",dictionary["hp"]) 
print("items :",dictionary["items"]) 
print("items[0] :",dictionary["items"][0]) 
print("skill :",dictionary ["skill"])


from random import *
 
i = randint(1, 3) 

j = randint(1, 3)


print ("도라에몽님 반갑습니다. 도라에몽으로 게임을 시작합니다.")
print ("길을 가다가 퉁퉁이를 만났습니다.")
b = input("1. 싸운다 2. 도망간다 ")
int_b = int(b)
if int_b == 1:
    print("퉁퉁이에게 싸움을 건다.")
    input()
else:
    print("도망갈려는데 퉁퉁이가 발을걸어서 넘어뜨려서 눈탱이밤탱이를 만들고 졌습니다.")
if int_b == 1:
    if i>j:
        print("퉁퉁이 명치를 한방을 때려 게임승리")
    else:
        print("퉁퉁이에게 한방을 줄려다가 퉁퉁이가 피해서 되려 맞아서 졌습니다.")

try:
    print(5/0)
except:
    print('다이')

