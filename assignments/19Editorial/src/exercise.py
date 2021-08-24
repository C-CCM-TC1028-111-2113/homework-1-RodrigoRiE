def main():
    #escribe tu código abajo de esta línea
    import math
    def calc_editorial(pal):
      pag = math.ceil(pal / 450)
      tot = (pag * 60)*0.9
      return tot

    pal = int(input("Give me the amount of words: "))
    print("El costo de la publicación es:",calc_editorial(pal))
    pass


if __name__ == '__main__':
    main()
