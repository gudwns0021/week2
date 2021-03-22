import turtle


# Turtle객체 생성
def makeTurtle(t):
    c = input("색깔 : ")
    t.color(c)
    r = input("반지름 : ")
    t.circle(r)
    m = input("이동거리 : ")
    t.forward(m)
t = turtle.Turtle()
makeTurtle(t)
turtle.mainloop() # 거북이 실행