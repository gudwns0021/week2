#for i in range(5):
    #print("방문을 환영합니다!")


#count = 0
#while True:
    #if count < 5:
        #print("count = ", count, "방문을 환영합니다!")
        #count += 1
    #else:
        #break
        #print("program end!")


#list = []
#list.append(1)
#list.append(2)
#list.append(6)
#list.append(3)

#list[1] = 150

#print(list)




#for i in range(1, 6):
    #print("9 *", i, "=", 9*i)


# for i in range(1, 10):
#     for j in range(1, 10):
#         print(1, "*", j, "=", j*i)

# n = int(input("정수를 입력하시오:"))
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i
#     print(fact, "i은", i, "이다.")

import turtle
t = turtle.Turtle()
t.shape("turtle")

s = turtle.textinput("", "몇각형을 원하시나?:")
n=int(s)

for i in range(n):
    t.forward(100)
    t.left(360/n)

turtle.mainloop()
turtle.bye()
