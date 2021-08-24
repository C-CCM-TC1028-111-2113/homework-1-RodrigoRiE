def main():
    #escribe tu código abajo de esta línea
    def calc_cuenta(saldo,ing,eg,che):
      tot_che = che * 13
      tot  = (saldo + ing - eg -tot_che)
      inte = tot * 0.075
      tot_m_int = tot - inte
      return tot_m_int

    sal = float(input("Saldo anterior: "))
    ing = float(input("Ingresos: "))
    eg = float(input("Egresos: "))
    che = float(input("Cheques: "))
    print("El saldo final de la cuenta es:",calc_cuenta(sal,ing,eg,che))

    pass

if __name__ == '__main__':
    main()
