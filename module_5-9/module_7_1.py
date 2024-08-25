class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self, file_nam='products.txt'):
        self.__file_name = file_nam

    def get_products(self):
        file = open(self.__file_name, 'r')
        read_file = file.read()
        file.close()
        return read_file

    def add(self, *products):
        file = open(self.__file_name, 'a')
        for product in products:
            if product.name in self.get_products():
                print(f'Продукт {product.name}  уже есть в магазине')
            else:
                file.write(f'\n{product}')
                # \n слева так как если в файле изначально что то будет, то первый продукт криво встанет
        file.close()

    def clear(self):
        file = open(self.__file_name, 'w')  # для очистки файла
        file.close()


if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__
    # если надо очистить файл
    # s1.clear()
    s1.add(p1, p2, p3)

    print(s1.get_products())
