def media(lista_numeros):
    return sum(lista_numeros) / len(lista_numeros)

def suma_cinco(lista_numeros):
    return [n + 5 for n in lista_numeros]

def main():
    print("Probando función media")
    lista_n = [34, 44, 23, 46, 12, 24]
    media_correcta = 30.5
    assert(media(lista_n) == media_correcta)

    print("Probando funcion suma_cinco")
    lista_correcta = [39, 49, 28, 51, 17, 29]
    assert(suma_cinco(lista_n) == lista_correcta)

    print("¡Todas las pruebas se ejecutaron correctamente!")

if __name__ == '__main__':
    main()