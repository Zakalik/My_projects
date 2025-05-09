spisok = []

def add_product(product):
    list.append(product)
    print(f"Товар '{product}' добавлен в список.")

def show_products():
    if not list:
        print("Список товаров пуст.")
    else:
        print("Список товаров:")
        for index, product in enumerate(list, start=1):
            print(f"{index}. {product}")

def remove_product(product):
    if product in list:
        list.remove(product)
        print(f"Товар '{product}' удалён.")
    else:
        print(f"Товар '{product}' не найден в списке.")

def exit():
    print("Выход из программы.")
    quit()



def start():
    print("Добро пожаловать в магазин!")
    print("Выберите действие:")
    print("1. Добавить товар")
    print("2. Показать все товары")
    print("3. Удалить товар")
    print("4. Выйти")
    print( )
    choice = input("Ваш выбор: ")
    if choice == "1":
        product = input("Введите название товара: ")
        add_product(product)
        start()
    elif choice == "2":
        show_products()
        start()
    elif choice == "3":
        product = input("Введите название товара который вы хотите удалить: ")
        remove_product(product)
        start()
    elif choice == "4":
        exit()
    else:
        print("Неверный выбор. Попробуйте снова.")
        start()

start()