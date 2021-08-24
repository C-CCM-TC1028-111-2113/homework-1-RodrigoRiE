def main():
    #escribe tu código abajo de esta línea
    def calc_videojuegos(nuevos,usados):
        tot_n = nuevos * 1000
        tot_u = usados * 350
        tot = tot_n + tot_u
        return tot
    
    nuevos = int(input("Give me the new games: "))
    usados = int(input("Give me the used games: "))
    print("The cost is:",calc_videojuegos(nuevos,usados))
   pass



if __name__ == '__main__':
    main()
