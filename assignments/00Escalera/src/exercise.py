import math 
def main():
    Altura = float(input('Altura de la casa: '))
    Angulo = int(input('Angulo en grados: '))

    radianes = math.radians(Angulo)

    Largo = round(Altura / math.sin(radianes))

    print(f'Largo de la escalera: {Largo}')



if __name__ == '__main__':
    main()
