import turtle
import math

# Ekranı oluştur
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Dünya ve Ay Animasyonu")

# Güneş'i oluştur
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(2, 2)

# Dünya'yı oluştur
earth = turtle.Turtle()
earth.shape("circle")
earth.color("blue")
earth.penup()

# Ay'ı oluştur
moon = turtle.Turtle()
moon.shape("circle")
moon.color("gray")
moon.shapesize(0.5, 0.5)
moon.penup()

# Animasyon döngüsü
angle = 0
while True:
    # Dünya'nın Güneş etrafında dönüşü
    earth_x = 200 * math.cos(math.radians(angle))
    earth_y = 300 * math.sin(math.radians(angle))
    earth.goto(earth_x, earth_y)

    # Ay'ın Dünya etrafında dönüşü
    moon_x = earth_x + 50 * math.cos(math.radians(12 * angle))
    moon_y = earth_y + 40 * math.sin(math.radians(12 * angle))
    moon.goto(moon_x, moon_y)

    angle += 1
    screen.update()

turtle.done()
