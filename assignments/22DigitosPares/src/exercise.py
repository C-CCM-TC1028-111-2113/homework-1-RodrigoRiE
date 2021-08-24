def main():
    #escribe tu código abajo de esta línea
    def pares_impares(number):
      even_num = 0
      odd_num = 0
      while(number > 0):
        if number % 2 == 0:
          even_num += 1
        else:
          odd_num += 1
        number = number // 10
      return odd_num
 
    num = int(input("Enter your number: "))
    print("Pares: ",pares_impares(num))
    pass


if __name__ == '__main__':
    main()
