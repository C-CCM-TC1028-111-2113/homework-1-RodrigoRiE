def main():
    #escribe tu código abajo de esta línea
    def calc_cmensual(men,meg,tiemp):
        suma = men + meg + tiemp
        total = suma*0.80
        return total

    men = float(input("Give me the maessajes: "))
    meg = float(input("Give me the megas: "))
    tiemp = float(input("Give me the minutes: "))

    print("The monthly cost is:",calc_cmensual(men,meg,tiemp))
    pass


if __name__ == '__main__':
    main()
