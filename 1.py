colors = ["red", "blue"]

# print(colors)
colors[1] = "yellow"
# print(colors)

# agrego elementos, pero yo elijo la posicion
colors.insert(1, 'violet')
print(colors)

# agrega un elemento al final
# colors.extend(("violet", "white"))
# colors.insert(len(colors), 'violet') # esto es exactamente igual
# print(colors)

# elimina lo que digo
# colors.remove('red')
# print(colors)

# elimina con coordenadas
# colors.pop(2)

# colors.clear borra todo

# x = ["juan", "josefa", "matilda", "roberto", 5]
# x[2] = "bob esponja"
# print(x)

products = [
    {
        "name": 'libro',
        "precio": 24
    },
    {
        "name": 'laptop',
        "precio": 40
    }
]
print(products.name)

# python manage.py runserver 3000

# python manage.py migrate
# python manage.py makemigrations
