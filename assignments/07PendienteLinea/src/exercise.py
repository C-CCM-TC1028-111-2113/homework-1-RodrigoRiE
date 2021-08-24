def main():
    #escribe tu código abajo de esta línea
    def slope(x1, y1, x2, y2):
        m = (y2-y1)/(x2-x1)
        return m
    
    #Lee los datos
    x1 = float(input("Give me x1: "))
    y1 = float(input("Give me y1: "))
    x2 = float(input("Give me x2: "))
    y2 = float(input("Give me y2: "))
    #muetra el resultado
    print("The slope is: ",slope(x1, y1, x2, y2))
    pass


if __name__ == '__main__':
    main()
