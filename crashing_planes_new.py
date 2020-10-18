import random
import tkinter as tk

from math import cos, sin, pi
from time import sleep, time
from numpy import arange


if __name__ == "__main__":
    while True:
        try:
            user_value = input("Сколько самолётов запустим?")
            if int(user_value) > 0:
                number_of_planes = int(user_value)
                break
            elif int(user_value) <= 0:
                print ("Надо ввести положительное число.")
        except ValueError:
                print ("Надо ввести положительное число.")


# Описываем самолёт как класс.  
class Plane(object):
    def __init__ (self, number, x_position, y_position, new_x_position, new_y_position, speed, direction, colour):
        self.number = number
        self.x_position = x_position
        self.y_position = y_position
        self.new_x_position = new_x_position
        self.new_y_position = new_y_position
        self.speed = speed
        self.direction = direction
        self.colour = colour

    def __str__ (self):
        return "cамолёт №{}, старое положение {}, {}, новое положение {},{}, скорость {}, направление {}".format(self.number,self.x_position, self.y_position, self.new_x_position, self.new_y_position,self.speed,self.direction)

    # Функция, описывающая перемещение самолёта на каждом ходе.  
    def fly(self):
        # Вычисляем новое положение.  
        self.x_position = self.new_x_position
        self.y_position = self.new_y_position
        self.new_x_position = round(self.x_position + self.speed * cos(self.direction * pi / 180), 2)
        self.new_y_position = round(self.y_position + self.speed * sin(self.direction * pi / 180), 2)

        # Меняем направление и скорость случайным образом.  
        self.direction = self.direction + random.randrange(-15, 16)
        self.speed = random.choice(speed_random)

    # Функция для определения вылета за пределы поля.  
    def out(self):
        if self.new_x_position > 5000 or self.new_y_position > 5000 or self.new_x_position < 0 or self.new_y_position < 0:
            return True
        else:
            return False
    
    # Визуализация полёта самолёта. Поскольку мне надо, чтобы всё поместилось на экране, рисуем в масштабе 1 к 10. Все значения для визуализации делим на 10.  
    def visual(self):
        # Рисуем вектор, где начальная точка – это предыдущее положение, а конечная точка – новое положение.  
        canvas.create_line(self.x_position/10, self.y_position/10, self.new_x_position/10, self.new_y_position/10, fill = self.colour, arrow="last", tag = "visual_plane")

        # Создаём текстовую метку с номером самолёта, которая будет отображаться рядом с ним.  
        if self.new_x_position > self.x_position:
            if self.new_x_position >= 4900:
                text_x = self.new_x_position / 10 - 15
            else:
                text_x = self.new_x_position / 10 + 10
        else:
            if self.new_x_position <= 100:
                text_x = self.new_x_position / 10 + 15
            else:
                text_x = self.new_x_position / 10 - 10

        if self.new_y_position/10 > self.y_position:
            if self.new_y_position >= 4900:
                text_y = self.new_y_position / 10 - 15
            else:
                text_y = (self.new_y_position + 100) / 10 + 10
        else:
            if self.new_y_position <= 100:
                text_y = self.new_y_position / 10 + 15
            else:
                text_y = self.new_y_position / 10 - 10
        canvas.create_text(text_x, text_y, text = self.number,fill = self.colour, tag = "visual_plane")

    # Функция для определения столкновения двух самолётов.  
    # Задаём точки для отрезков, отображающих путь двух самолётов за ход.
    def crash(self, other):
        x1_1 = self.x_position
        x1_2 = self.new_x_position
        y1_1 = self.y_position
        y1_2 = self.new_y_position
        x2_1 = other.x_position
        x2_2 = other.new_x_position
        y2_1 = other.y_position
        y2_2 = other.new_y_position
        
        # Если вторая координата по оси ОХ меньше первой, меняем точки местами.
        if x1_2 < x1_1:
            x1_1, x1_2 = x1_2, x1_1
            y1_1, y1_2 = y1_2, y1_1
        if x2_2 < x2_1:
            x2_1, x2_2 = x2_2, x2_1
            y2_1, y2_2 = y2_2, y2_1

        # Проверяем отрезки на наличие обших координат по оси ОХ. Если таких нет, пересечения тоже нет.
        if x1_2 < x2_1 or x2_2 < x1_1:
            return False
        
        # Проверям частный случай, когда оба отрезка вертикальны.
        elif x1_1 == x1_2 and x2_1 == x2_2:
            if x1_1 == x2_1:
                if max (y1_1, y1_2) < min(y2_1, y2_2) or max(y2_1, y2_2) < min(y1_1, y1_2):
                    return False
                else:
                    return True
        # Проверяем частный случай, когда первый отрезок вертикален, а второй нет.
        else:
            if x1_1 == x1_2:
                cross_x = x1_1
                k2 = (y2_1 - y2_2) / (x2_1 - x2_2)
                b2 = y2_1 - k2 * x2_1
                cross_y = k2* cross_x + b2
                if cross_y >= min(y1_1, y1_2) and cross_y <= max(y1_1, y1_2):
                    return True
                else:
                    return False
            # Проверяем частный случай, когда второй отрезок вертикален, а первый нет.
            elif x2_1 == x2_2:
                cross_x = x2_1
                k1 = (y1_1 - y1_2) / (x1_1 - x1_2)
                b1 = y1_1 - k1 * x1_1
                cross_y = k1 * cross_x + b1
                if cross_y >= min(y2_1, y2_2) and cross_y <= max(y2_1, y2_2):
                    return True
                else:
                    return False
            # Проверяем общий случай. Рассчитываем недостающие переменные для формулы прямой.
            else:
                k1 = (y1_1 - y1_2) / (x1_1 - x1_2)
                k2 = (y2_1 - y2_2) / (x2_1 - x2_2)
                b1 = y1_1 - k1 * x1_1
                b2 = y2_1 - k2 * x2_1
                # Если совпадает коэффициент k, значит прямые параллельны.
                if k1 == k2:
                    return False
                # Находим точку пересечения прямых и проверяем, принадлежит ли эта точка одному из отрезков.
                else:
                    cross_x = (b2 - b1) / (k1 - k2)
                    cross_y = k1 * cross_x + b1
                    if cross_x >= min(x1_1, x2_1) and cross_x <= min (x1_2, x2_2):
                        return True
                    else:
                        return False


# Это функция для случайного выбора цвета самолёта.  
def plane_colour():
    hex_digits = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    digit_array = []
    for m in range(6):
        digit_array.append(hex_digits[random.randint(0,15)])
    joined_digits = ''.join(digit_array)
    colour = '#' + joined_digits
    return colour

pos_random = arange(1, 5000, 0.1)
dir_random = range(1, 360, 1)
speed_random = range(300, 1001, 100)
planes = list()

# Создаём окно визуализации.  
# Поскольку я хочу, чтобы всё поместилось на экране, отображение будет в масштабе 1 к 10.
root = tk.Tk()
root.title("Полетаем?")
root.attributes("-topmost", True)
#root.attributes("-fullscreen", True)
canvas = tk.Canvas(width = 500, height = 500,bg="white") 
canvas.pack()

# Рисуем сетку.  
for g in range(0, 500, 50):
    canvas.create_line(0, g, 500, g, fill="#A0A0A0")
    canvas.create_line(g, 0, g, 500, fill="#A0A0A0")
    canvas.create_text(g+15, 10, text = g * 10, fill="#A0A0A0", justify="left")
    if g > 0:
        canvas.create_text(15, g+10, text = g * 10, fill="#A0A0A0", justify="left")
    canvas.update()


# Рисуем обратный отсчёт.
for c in range(3,0,-1):
    countdown = canvas.create_text(250,250,text=c,fill="red",font=("arial", 50))
    canvas.update()
    sleep(1)
    canvas.delete(countdown)
countdown = canvas.create_text(250, 250, text="полетели!", fill="red",font=("arial", 50))
canvas.update()
sleep(1)
canvas.delete(countdown)


# Создаём самолёты в том количестве, которое получили от пользователя.  
for i in range(1, number_of_planes+1):
    a = Plane(i, round(random.choice(pos_random), 2), round(random.choice(pos_random), 2), 0, 0, random.choice(speed_random), random.choice(dir_random), plane_colour())
    # Сразу добавляем новые координаты с учётом направления. Это нужно, чтобы до начала движения самолёты отображались как стрелки.
    a.new_x_position = a.x_position + round(1 * cos(a.direction * pi / 180), 2)
    a.new_y_position = a.y_position + round(1 * sin(a.direction * pi / 180), 2)
    planes.append(a)

count = 1       # Номер хода.

while True:
    t = time()        # Фиксируем время начала хода

    # Очищаем экран и рисуем текущее состояние.  
    canvas.delete("count")
    canvas.create_text(460, 490, text = "ход № {}".format(count), tag = "count")
    canvas.delete("visual_plane")
    
    for vis in planes:
        vis.visual()
    canvas.update()
    canvas.delete("message")


    print("Ход №{}".format(count))
    for f in planes:
        f.fly()

    # Берём каждый самолёт в списке и проверяем, не покинул ли он поле.  
    text_y = 30
    for off in planes:
        if off.out() is True:
            planes.remove(off)
            #canvas.delete("message")
            canvas.create_text(30, text_y, text="Cамолёт №{} покинул поле".format(off.number), fill="red",  tag = "message", anchor = "w")
            print("{} покинул поле.".format(off))
            text_y = text_y + 20
            print(text_y)


    # Берём каждый самолёт в списке и проверяем на столкновение с каждым последующим из списка.  
    for cr in planes:
        current_plane = cr
        current_plane_index = planes.index(cr)
        for an in planes[current_plane_index+1:number_of_planes]:
            if current_plane.crash(an) is True:
                another_plane = an
                another_plane_index = planes.index(an)
                # canvas.delete("message")
                canvas.create_text(30, text_y, text="Cтолкнулись самолёты №{} и №{}".format(cr.number, an.number), justify = "left", fill="red",tag = "message", anchor = "w")
                print("Cтолкнулись {} и {}.".format(current_plane, another_plane))
                del planes[another_plane_index]
                del planes[current_plane_index]
                text_y = text_y + 20
                break
    
    tn = time()            # Фиксируем время завершения хода.
    
    # Для большей равномерности выполнения, если с начала цикла прошло меньше 3 секунд, выжидаем, пока не пройдут 3 секунды. Иначе – сразу продолжаем.  
    if int(t - tn) < 2:
        sleep(2 - int(t - tn))

    count = count + 1

    # Если список самолётов опустел, то и мы завершаем.  
    if len(planes) == 0:
        break

canvas.delete("visual_plane")
canvas.update()
sleep(3)
canvas.delete("message")
canvas.create_text (250,250,text="самолётов\nбольше\nне осталось", font = ("arial", 30), fill="red", justify = "center")
canvas.update()
print("самолётов больше не осталось")
sleep(5)