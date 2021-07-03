import numpy as np
class Matriz:
    def __init__(self):
        pass

    @staticmethod
    def matrices(cantidad):
        lista = []
        for i in range(cantidad):
            a = int(input("Ingrese el numero filas de la matriz #{0}: ".format(i+1)))
            b = int(input("Ingrese el numero columnas de la matriz #{0}: ".format(i+1)))
            lista.append(np.zeros((a,b),dtype=np.int16))
        return lista
    
    @staticmethod
    def llenar_matrices(matriz,a,b):
        for i in range(a):
            for j in range(b):
                matriz[i][j] = input(f"Ingrese un numero para la fila {i+1} y columna {j+1}: ")  
        return matriz

    @staticmethod
    def dimensiones(matriz):
        filas = matriz.shape[0]
        columnas = matriz.shape[1]
        return filas, columnas

    @staticmethod
    def suma_matrices(matriz1,matriz2):
        if matriz1.shape == matriz2.shape:
            suma = matriz1 + matriz2
            return f"""La matriz resultante es:
{suma}"""
        else:
            return "Las dimensiones de las matrices no son iguales."

def main():
    print("Este programa realiza varias opciones relacionadas con matrices. Seleccione una opcion:")
    valido = True
    matriz1 = []
    matriz2 = []
    while valido:
      print("""
        Opciones:
        1. Crear las matrices nulas
        2. Llenar las matrices
        3. Mostrar contenido de las matrices
        4. Determinar la dimension de una de las matrices
        5. Sumar las matrices
        """)
      opcion = str(input(""))
      if opcion == "1":
        cantidad = input("¿Cuantas matrices desea crear? Minimo: 1, Maximo: 2 --> ")
        if cantidad == "1" or cantidad == "2":
          if cantidad == "2":
            a = Matriz.matrices(2)
            matriz1 = a[0]
            matriz2 = a[1]
          else:
            a = Matriz.matrices(1)
            matriz1 = a[0]
        else:
          print("La opcion ingresada no es valida")
        salir = input("¿Desea volver al menu de opciones?(S/N) default = N --> ").upper()
        if salir == "S":
          pass
        else: 
          valido = False
      elif opcion == "2":
        booleano = True
        while booleano:
          opcion = input("¿Desea llenar la matriz 1 o la matriz 2? ")
          if opcion == "1":
            if len(matriz1) == 0:
              print("No has creado la matriz 1")
            else:
              matriz1 = Matriz.llenar_matrices(matriz1,matriz1.shape[0], matriz1.shape[1])
            booleano2 = True
            while booleano2:
              opcion1 = input("¿Desea llenar otra matriz?(S/N) ")
              if opcion1  == "S":
                booleano2 = False
              elif opcion1 == "N":
                booleano2 = False
                booleano = False
              else: 
                print("La opcion no es valida")  
          elif opcion == "2":
            if len(matriz2) == 0:
              print("No has creado la matriz 2")
            else:
              matriz2 = Matriz.llenar_matrices(matriz2,matriz2.shape[0], matriz2.shape[1])
            booleano2 = True
            while booleano2:
              opcion1 = input("¿Desea llenar otra matriz?(S/N) ")
              if opcion1  == "S":
                booleano2 = False
              elif opcion1 == "N":
                booleano2 = False
                booleano = False
              else: 
                print("La opcion no es valida")
          else:
            print("La opcion ingresada no es valida")
        salir = input("¿Desea volver al menu de opciones?(S/N) default = N --> ").upper()
        if salir == "S":
          pass
        else: 
          valido = False
      elif opcion == "3":
        if len(matriz1) == 0 and len(matriz2) == 0:
          print("No ha creado ninguna matriz")
        elif len(matriz1) == 0:
          print("No has creado la matriz 1")
          print("La matriz 2 es: \n", matriz2)
        elif len(matriz2) == 0:
          print("La matriz 1 es: \n", matriz1)
          print("No has creado la matriz 2")
        else:
          print("La matriz 1 es: \n", matriz1)
          print("La matriz 2 es: \n", matriz2)
        salir = input("¿Desea volver al menu de opciones?(S/N) default = N --> ").upper()
        if salir == "S":
          pass
        else: 
          valido = False
      elif opcion == "4":
        booleano = True
        while booleano:
          opcion = input("¿Desea saber las dimensiones de la matriz 1 o la matriz 2? ")
          if opcion == "1":
            if len(matriz1) == 0:
              print("No has creado la matriz 1")
            else:
              filas_matriz1,columnas_matriz1 = Matriz.dimensiones(matriz1)
              print(f"La matriz 1 tiene {filas_matriz1} filas y {columnas_matriz1} columnas")
              booleano2 = True
              while booleano2:
                opcion1 = input("¿Desea saber las dimensiones de otra matriz?(S/N) ").upper()
                if opcion1  == "S":
                  booleano2 = False
                elif opcion1 == "N":
                  booleano2 = False
                  booleano = False
                  salir = input("¿Desea volver al menu de opciones?(S/N) default = N --> ").upper()
                  if salir == "S":
                    booleano2 = False
                    booleano = False
                else: 
                  print("La opcion no es valida")
                  salir = input("¿Desea volver al menu de opciones?(S/N) default = N --> ").upper()
                  if salir == "S":
                    booleano2 = False
                    booleano = False
              else:
                valido = False
          elif opcion == "2":
            if len(matriz2) == 0:
              print("No has creado la matriz 2")
            else:
              filas_matriz2,columnas_matriz2 = Matriz.dimensiones(matriz2)
              print(f"La matriz 2 tiene {filas_matriz2} filas y {columnas_matriz2} columnas")
              booleano2 = True
              while booleano2:
                opcion1 = input("¿Desea saber las dimensiones de otra matriz?(S/N) ").upper()
                if opcion1  == "S":
                  booleano2 = False
                elif opcion1 == "N":
                  booleano2 = False
                  booleano = False
                  salir = input("¿Desea volver al menu de opciones?(S/N) default = N --> ").upper()
                  if salir == "S":
                    booleano2 = False
                    booleano = False
                else: 
                  print("La opcion no es valida")
                  salir = input("¿Desea volver al menu de opciones?(S/N) default = N --> ").upper()
                  if salir == "S":
                    booleano2 = False
                    booleano = False
              else:
                valido = False
          else:
            print("La opcion ingresada no es valida")

      elif opcion == "5":
        if len(matriz1) == 0 or len(matriz2) == 0:
          print("No has creado una de las matrices. No es posible realizar la suma")
        else: 
          print(Matriz.suma_matrices(matriz1,matriz2))
        salir = input("¿Desea volver al menu de opciones?(S/N) default = N --> ").upper()
        if salir == "S":
          pass
        else:
          valido = False
      else:
        print("La opcion ingresada no es valida")
        salir = input("¿Desea volver al menu de opciones?(S/N) default = N --> ").upper()
        if salir == "S":
          pass
        else: 
          valido = False
        
main()