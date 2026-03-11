print("Bienvenido a Riwistore")

def calcular_total(precio, cantidad):
    precio = float(precio)
    cantidad = int(cantidad)
    return precio * cantidad

total_general = 0

continuar = "si"  # Para que entre al bucle la primera vez

while continuar.lower() == "si":
    nombre = input("Ingresar nombre de producto: ")
    precio = input("Ingresar Precio: ")
    cantidad = input("Ingresar cantidad del producto: ")
    
    subtotal = calcular_total(precio, cantidad)
    total_general += subtotal
    
    print(f"Producto: {nombre}, Subtotal: {subtotal}")
    
    continuar = input("¿Deseas agregar otro artículo? (si/no): ")

print(f"Total general a pagar: {total_general}")
