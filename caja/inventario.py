def obtener_input_valido(mensaje, tipo): #funcion para evitar error
    valor_correcto = False
    while not valor_correcto:
        entrada = input(mensaje)
        try:
            valor = tipo(entrada)
            valor_correcto = True
            return valor
        except ValueError:
            print("Error: Ingresa un valor válido.") #garantiza que un error no cierre el programa.
