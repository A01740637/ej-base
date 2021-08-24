def equivalente(horas, minutos, segundos):
    minutosAsegundos = minutos * 60
    horasAsegundos = horas * 3600
    totalsegundos = segundos + minutosAsegundos + horasAsegundos
    return totalsegundos

def main():
    #escribe tu código abajo de esta línea
    pass
    print(equivalente(2,20,8))

if __name__=='__main__':
    main()
