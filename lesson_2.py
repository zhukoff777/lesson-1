#exercise 1
""" a = 179
b = 197
c = (a ** 2 + b ** 2) ** 0.5
print(c) """

""" x = int(input())
y = int(input())
if x > 0 and y > 0:
	print("Первая четверть")
elif x < 0 and y > 0:
	print("Вторая четверть")
elif x < 0 and y < 0:
	print("Третья четверть")
elif x > 0 and y < 0:
	print("Четвертая четверть")
else:
	print("Точка находится на осях или в центре координат.") """

#turtles
import turtle

""" turtle.shape('arrow')
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50) """

""" turtle.shape('arrow')
turtle.fd(50)
turtle.right(90)
turtle.fd(50)
turtle.right(90)
turtle.fd(50)
turtle.right(90)
turtle.fd(50)
turtle.right(90) """

turtle.shape('arrow')
for x in range(4) :
	turtle.fd(50)
	turtle.right(90)
