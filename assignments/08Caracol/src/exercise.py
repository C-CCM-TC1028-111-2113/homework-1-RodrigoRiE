def main():
    #escribe tu código abajo de esta línea
    def caracol (minu):
        seg = minu * 60
        car = 0.57 * seg
        return car

    minu = int(input("Give me the minutes: "))
    print("The distance traveled by the snail: ",caracol(minu))
    pass

if __name__ == '__main__':
    main()
