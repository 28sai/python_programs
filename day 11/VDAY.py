for i in range(5):
    for j in range(26):
        if (j==0 or j==3 or j==11 or j==16) or (i==0 and (j!=1 and j!=2 and j!=4 and j!=5 and j!=6 and j!=8 and j!=9 and j!=10 and j!=14 and j!=15 and j!=19 and j!=20 and j!=22 and j!=23 and j!=24))or (i==1 and (j!=1 and j!=2 and j!=4 and j!=5 and j!=7 and j!=9 and j!=10 and j!=12 and j!=13 and j!=15 and j!=17 and j!=20 and j!=18 and j!=23 and j!=21 and j!=25))or (i==2 and (j!=4 and j!=10 and j!=14 and j!=15 and j!=19 and j!=20 and j!=21 and j!=22 and j!=24 and j!=25)or (i==3 and (j!=1 and j!=2 and j!=4 and j!=6 and j!=7 and j!=8 and j!=10 and j!=12 and j!=13 and j!=14 and j!=15 and j!=17 and j!=19 and j!=18 and j!=20 and j!=21 and j!=22 and j!=24 and j!=25)) or (i==4 and(j!=1 and j!=2 and j!=4 and j!=6 and j!=7 and j!=8 and j!=10 and j!=12 and j!=13 and j!=14 and j!=15 and j!=7 and j!=18 and j!=19 and j!=20 and j!=21 and j!=22 and j!=24 and j!=25))):
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n")
for i in range(5):
    for j in range(55):
        if j==12 or j==17 or j==22 or j==26 or j==30 or j==36 or j==40 or j==44 or j==46 or(i==0 and (j!=1 and j!=2 and j!=3 and j!=5 and j!=6 and j!=7 and j!=9 and j!=10 and j!=11 and j!=13 and j!=14 and j!=15 and j!=16 and j!=21 and j!=23 and j!=24 and j!=25 and j!=27 and j!=33 and j!=39 and j!=41 and j!=42 and j!=43 and j!=45 and j!=50 and j!=51 and j!=54))or(i==1 and (j!=1 and j!=2 and j!=3 and j!=5 and j!=6 and j!=8 and j!=10 and j!=11  and j!=13 and j!=14 and j!=15 and j!=16 and j!=18 and j!=19 and j!=20 and j!=21 and j!=24 and j!=25 and j!=27 and j!=28 and j!=29 and j!=31 and j!=32 and j!=33 and j!=34 and j!=35 and j!=37 and j!=38 and j!=39 and j!=42 and j!=43 and j!=45 and j!=47 and j!=48 and j!=49 and j!=50 and j!=52 and j!=53 and j!=54))or(i==2 and (j!=1 and j!=2 and j!=3 and j!=5 and j!=11 and j!=13 and j!=14 and j!=15 and j!=16 and j!=21 and j!=23 and j!=25 and j!=27 and j!=28 and j!=29 and j!=31 and j!=32 and j!=33 and j!=34 and j!=35 and j!=37 and j!=38 and j!=39 and j!=41 and j!=43 and j!=45 and j!=50 and j!=51 and j!=54))or(i==3 and (j!=0 and j!=2 and j!=4 and j!=5 and j!=7 and j!=8 and j!=9 and j!=11  and j!=13 and j!=14 and j!=15 and j!=16 and j!=18 and j!=19 and j!=20 and j!=21 and j!=23 and j!=24 and j!=27 and j!=28 and j!=29 and j!=31 and j!=32 and j!=33 and j!=34 and j!=35 and j!=37 and j!=38 and j!=39 and j!=41 and j!=42 and j!=45 and j!=47 and j!=48 and j!=49 and j!=50 and j!=51 and j!=52 and j!=53))or(i==4 and (j!=0 and j!=1 and j!=3 and j!=4 and j!=5 and j!=7 and j!=8 and j!=9 and j!=11  and j!=16 and j!=21 and j!=23 and j!=24 and j!=25 and j!=27 and j!=28 and j!=29 and j!=31 and j!=32 and j!=33 and j!=39 and j!=41 and j!=42 and j!=43 and j!=45 and j!=50)):
            print("*",end='')
        else:
            print(end=" ")
    print()
print("\n")
for i in range(5):
    for j in range(16):
        if j==0 or (i==0 and (j!=3 and j!=4 and j!=5 and j!=6 and j!=8 and j!=9 and j!=10 and j!=12 and j!=13 and j!=14)) or (i==1 and (j!=1 and j!=2 and j!=4 and j!=5 and j!=7 and j!=9 and j!=10 and j!=11 and j!=13 and j!=15))or (i==2 and (j!=1 and j!=2 and j!=4 and j!=10 and j!=11 and j!=12 and j!=14 and j!=15))or (i==3 and (j!=1 and j!=2 and j!=4 and j!=6 and j!=7 and j!=8 and j!=10 and j!=11 and j!=12 and j!=14 and j!=15))or (i==4 and (j!=3 and j!=4 and j!=6 and j!=7 and j!=8 and j!=10 and j!=11 and j!=12 and j!=14 and j!=15)):
            print("*",end='')
        else:
            print(end=' ')
    print()
print("\n")
import turtle


pen = turtle.Turtle()


def curve():
	for i in range(200):

		
		pen.right(1)
		pen.forward(1)


def heart():


	pen.fillcolor('red')


	pen.begin_fill()


	pen.left(140)
	pen.forward(113)


	curve()
	pen.left(120)


	curve()


	pen.forward(112)

	pen.end_fill()


def txt():

	pen.up()


	pen.setpos(-68, 95)


	pen.down()

	
	pen.color('lightgreen')


	pen.write(" I LOVE U MITHRA", font=("Verdana", 12, "bold"))



heart()


txt()


pen.ht()

