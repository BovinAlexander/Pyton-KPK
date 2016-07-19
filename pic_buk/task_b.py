import turtle
import time
t = turtle.Turtle()
t.shape("turtle")
t.color("darkgreen", "yellow")
t.shapesize(2)
t.speed(20)
#углы поворота расчитываются из расчета, что черепашк смотрит вверх
n0=[1,1,1,1,1,1]#0-нет линия,1-лини,2 линия под углом,3 -нет линии под углом
u0=[0,0,2,2,0,2]#0-нет поворота,1-90 на прово,2-90 на лево,3-45 на право,4-45 на лево,5-135 на право, 6-135 на лево
n1=[1,1,2]
u1=[0,0,6]
n2=[1,2,1,1,1]
u2=[2,5,4,2,2]
n3=[0,2,1,2,1]
u3=[2,5,6,5,6]
n4=[1,1,0,1,1]
u4=[0,0,2,2,2]
n5=[1,1,1,1,0,0,0,1]
u5=[0,2,1,1,1,1,2,2]
n6=[1,1,1,1,3,1,1]
u6=[0,2,1,1,5,4,2]
n7=[0,1,2,1]
u7=[2,1,3,6]
n8=[1,1,1,1,1,1,1,1]
u8=[0,2,1,1,1,1,2,2]
n9=[1,1,1,1,1,3,1]
u9=[0,2,1,1,1,3,6]
def main():
    t.hideturtle()
    write(544,50,-100,100)
    write(1817,100,100,100)
    time.sleep(2)
def write(number=0,size=50,x=0,y=0):
    """
    Рисунт заданное число, заданного размера, в заданной позиции
    :param number: число
    :param size: размер
    :param x: кордината по горизонтали
    :param y: координата по вертикали
    :return:
    """""
    t.up()
    t.goto(x,y)
    c=number
    s=1
    sp=[]
    while c>0:
        s=c%10
        sp.append(s)
        c=c//10
        #s=s*10
    print(sp)
    sp.reverse()
    for i in sp:

        print(i)
        digit(i,size)
        t.forward(size*0.8)

    t.up()

def digit(numeral=9,size=50):
    """ Рисует цифру заданную numeral с высотой size
        контракт (договорённость):
        изначально черепашку смотри в лево
        черепаха начинает рисовать из заданной координаты
        перо оказывается поднятым по окончании функции
    """
    t.left(90)
    L1 = size/2
    L2 = (size/2)*2**0.5

    # выбор цифры
    if numeral==0:
        B = u0
        A = n0
    elif numeral==1:
        B = u1
        A = n1
    elif numeral==2:
        B = u2
        A = n2
    elif numeral==3:
        B = u3
        A = n3
    elif numeral==4:
        B = u4
        A = n4
    elif numeral==5:
        B = u5
        A = n5
    elif numeral==6:
        B = u6
        A = n6
    elif numeral==7:
        B = u7
        A = n7
    elif numeral==8:
        B = u8
        A = n8
    elif numeral==9:
        B = u9
        A = n9
        

    # рисует выбранную цифру    
    for i in range(len(A)):
        
        if B[i]==0:
            t.right(0)
        elif B[i]==1:
            t.right(90)
        elif B[i]==2:
            t.left(90)
        elif B[i]==3:
            t.right(45)
        elif B[i]==4:
            t.left(45)
        elif B[i]==5:
            t.right(135)
        elif B[i]==6:
            t.left(135)
        if A[i]==0:
            t.up()
            t.forward(L1)
        elif A[i]==1:
            t.pendown()
            t.forward(L1)
        elif A[i]==2:
            t.pendown()
            t.forward(L2)
        elif A[i]==3:
            t.up()
            t.forward(L2)
            
    A.reverse()
    B.reverse()
    t.penup()
    for i in range(len(A)):
        if A[i]<2:
            t.backward(L1)
        else:
            t.backward(L2)
        if B[i]==0:
            t.right(0)
        elif B[i]==1:
            t.left(90)
        elif B[i]==2:
            t.right(90)
        elif B[i]==3:
            t.left(45)
        elif B[i]==4:
            t.right(45)
        elif B[i]==5:
            t.left(135)
        elif B[i]==6:
            t.right(135)
        
    t.right(90)
    A.reverse()
    B.reverse()

main()

#t.left(30)
#t.right(30)
#t.forward(200)
#t.backward(200)
#t.penup()
#t.pendown()
#t.begin_fill()
#t.end_fill()
