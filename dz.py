# задача № 1
def division (a, b):
    try:
        a = int(a)
        b = int(b)
        s = a / b
    except ZeroDivisionError:
        return 'нельзя делить на ноль'
    except ValueError:
        return "вводите только цифры"
    return s
a = input("number 1: ")
b = input("number 2: ")
print(division(a, b))

  #задача №2
def info(name, family, birth, city, email, tel):
    return f"Name: {name}, Surname: {family}, Birthday: {birth}, City: {city}, email: {email}, Tel: {tel}"
print(info(name = input("Введите имя: "), family = input("Введите фамилию: "),  birth  = input("Введите дату рождения: "),
       city=input("Введите город проживания: "), email  = input("Введите почту: "), tel  = input("Введите номер телефона: ")))

#задача №3
def sum_max(a, b, c):
    li = [a, b, c]
    try:
        li.remove(min(li))
        return sum(li)
    except TypeError:
        return " не число"
print(sum_max(45, 76, 9))

#задача №4.1
def my_fun(x, y):
    res = x ** y
    return res
print(my_fun(5, -3))

#4.2
def my_fun(x, y):
     try:
         x, y  = float(x), int(y)
         res = 1
         for i in range(abs(y)):
             res = res / x
         return round(res, 5)
     except ValueError:
         return "это не номер"
y1 = input("x: ")
x1 = input("y: ")
print(my_fun(y1, x1))

#задача №5
def sum():
    res = 0
    while True:
        li = input("введите числа").lower().split()
        for num in li:
            if num == 'stop':
                return res
            else:
                try:
                    res += int(num)
                except ValueError:
                    return "stop для выхода"
        print('summa = ',  res)
print(sum())

# задача №6
def int_func(*args):
    li = input('введите слова')
    print(li.title())
    return
int_func()

