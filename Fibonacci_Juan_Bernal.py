#Juan Diego Bernal Lopez   C.C. 1000156844
#El programa no corre en paginas como google colab debido a que estas mismas no ofrecen soporte para ventanas externas, por ende para ejecutar el codigo es necesario hacerlo en un editor de texto como pycharm o vscode, que admiten modulos como tkinter
#ejemplo ammonite y su relacion con la serie de fibonacci
#El programa solicita al usuario cuantos cuadrados desea tener su ammonite. La forma de un amonite se puede aproximar a la serie de fibonacci debido a que por ejemplo
#el primer cuadrado del amonnite puede ser de 0.25 x 0.25 mm e ir creciendo por la forma f(n)=f(n-1)+f(n-2)
#Por ende, el programa inicia con un tamaño inicial de 0.25 mm y si el usuario indica por ejemplo que quiere saber el tamaño de cada cuadrado que compone un ammonite de 13 cuadrados, el programa indica estos valores.
#Importamos la libreria turtle que permite la programacion orientada a objetos
import turtle
#creamos un objeto con nombre tortuga y se le asigna un valor de 2 a su tamaño de linea
tortuga = turtle.Turtle()
tortuga.pensize(2)
#ahora creamos una funcion que dibuje un cuadrado equilatero con el parametro lado que debe ser ingresado
#Cabe destacar que el tamaño del lado se multiplica por 100 debido a que al momento de ejecutar si se deja con el valor inicial de 0.25, es muy pequeño y no se observa bien la grafica
def cuadrado(lado):
    tortuga.color('red')
    tortuga.pendown()
    for i in range(4):
        tortuga.forward(lado*100)
        tortuga.left(90)
    tortuga.penup()
#creamos una funcion que llame a la funcion cuadrado y a su vez dibuje el circulo que une las diagonales del circulo
def cuadradoycirculo(lado):
    cuadrado(lado)
    tortuga.color('black')
    tortuga.pendown()
    tortuga.circle(lado*100, 90)
#inicializamos la lista fibo con dos elementos, que seran los dos primeros cuadrados, y luego con la funcion fibonacci seguiremos creando la lista con los elementos que faltan para llegar a los n elementos que indico el usuario
fibo = [0.25,0.25]
def fibonacci(n):
    numeronuevo = 0
    for i in range(2,n):
        numeronuevo = fibo[i-2]+fibo[i-1]
        fibo.append(numeronuevo)
#preguntamos al usuario por la cantidad de cuadros que desea que tenga el ammonite
n = int(input('Ingrese la cantidad de cuadrados que desea que tenga el ammonite: '))
#ejecutamos la funcion fibonacci con n como parametro
fibonacci(n)
#imprimimos en pantaña el tamaño de cada cuadro
mensaje ='El tamaño respectivo de cada cuadrado que compone al ammonite es de: '
for i in range(len(fibo)):
    mensaje += str(fibo[i])+ ' mm, '
print(mensaje[:-2])
#Indicamos la condicion inicial de la tortuga
tortuga.penup()
#Ejecutamos el for loop que pintara el ammonite
for i in fibo:
    cuadradoycirculo(i)
#El comando turtle.exitonclick() se usa para que la imagen generada quede visible hasta que el usuario oprima cualquier parte de la pantalla
turtle.exitonclick()