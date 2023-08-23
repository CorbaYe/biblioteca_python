listIsb = []
listNombre = []
listAutor = []
listPaginas = []
listExistencias = []

import os

def fntLimpiar():
    global totalE
    totalE = 0
    os.system('cls' if os.name == 'nt' else 'clear')
    print('<<< SISTEMA DE BIBLIOTECA - YEISON >>>')
    print('Autor: Yeison Cordoba')
    for i in range(0,len(listExistencias)):
        totalE += listExistencias[i]
    print('Cantidad de ejemplares: ',totalE, '\n')

def fntRegistrar(isbn,nombre,autor,paginas):
    if isbn != '' and nombre != '' and  autor != '' and paginas != '':
        listIsb.append(isbn)
        listNombre.append(nombre)
        listAutor.append(autor)
        listPaginas.append(paginas)
        listExistencias.append(0)
        print('El libro ', nombre, ' ha sido registrado con éxito')
        enter = input('<ENTER>')
    else:
        enter = input('\nDebe ingresar todos los datos <ENTER>')

def fntConsultar(isbn):
    if isbn!= '':
        sw = False
        for i in range(0,len(listIsb)):
            if isbn == listIsb[i]:
                sw = True
                pos = i
                break
        if sw == False:
            enter = input('\nEl ISBN ingresado no existe <ENTER>')
        else:
            print('ISBN...........................', listIsb[pos])
            print('Nombre.........................', listNombre[pos])
            print('Autor..........................', listAutor[pos])
            print('Paginas........................', listPaginas[pos])
            print('Existencias....................', listExistencias[pos])
            enter = input('\nFin de registros <ENTER>')
    else:
        enter = input('\nDebe ingresar el ISBN <ENTER>')

def fntMenu(inic):
    while inic == True:
        fntLimpiar()
        print('<<< MENÚ PRINCIPAL >>>')
        print('1. Registrar')
        print('2. Consultar')
        print('3. Inventario')
        print('4. informe')
        print('5. Salir')

        opcion = int(input('Opcion -> '))

        if opcion == 1:
            fntLimpiar()
            isbn = input('Ingrese el ISBN del libro: ')
            nm = input('Ingrese el nombre del libro: ')
            at = input('Ingrese el autor del libro: ')
            pg = input('Ingrese la cantidad de paginas del libro: ')
            fntRegistrar(isbn,nm,at,pg)
        elif opcion == 2:
            fntLimpiar()
            isbn = input('Ingrese el ISBN del libro: ')
            fntConsultar(isbn)
        elif opcion == 3:
            fntInventario()
        elif opcion == 4:
            fntInforme()
        elif opcion == 5:
            inic = False
        else:
            enter = input('Opcion incorrecta <ENTER>')

fntMenu(True)