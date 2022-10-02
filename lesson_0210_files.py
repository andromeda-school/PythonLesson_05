
# Программа, которая принимает имя
#   и выводит "Привет, ИМЯ !"
#
# def func_hello(name):
#     print("Hello", name, "!")
#
#
# func_hello("Anton")
# func_hello("Stepan")

# Урок №5.  Файлы,
#               которые слишком скучные,
#                   чтобы их проходить.

f = open('text.txt', 'w')
f.write('Hello World!')
f.close()

f = open('numbers.txt', 'r')
data = f.read()
f.close()
print(data.split(' '))

data = data.replace('\n', '').split(' ')
print(data)

# for i in range(len(data)):
#     data[i] = int(data[i])
#
# print(data)

# f = open('tmp.txt', 'r')
# data = f.read()
# f.close()
# print(data, '\n')
#
# keys = [
#     data.split('\n')[0].split(' ')[0],
#     data.split('\n')[1].split(' ')[0]
# ]
# values = [
#     int(data.split('\n')[0].split(' ')[1]),
#     int(data.split('\n')[1].split(' ')[1])
# ]
#
# print(keys[0], ":", values[0])
# print(keys[1], ":", values[1])



