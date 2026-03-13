print("Bienvenido a Riwistore") #mensaje de bienvenida
from inventario import obtener_input_valido #importacion del inventario

def costo_total(precio, cantidad): #variable definida
    return precio * cantidad

total_general = 0
continuar = "si" #condicional para continuar el ciclo

while continuar.lower() == "si":
    nombre = input("Ingresar nombre de producto: ").strip()
    precio = obtener_input_valido("Ingresar Precio: ", float)
    cantidad = obtener_input_valido("Ingresar cantidad del producto: ", int)
    
    subtotal = costo_total(precio, cantidad)
    total_general += subtotal  # ← Acumulado de los productos aquí
    
    print(f"Producto: {nombre}")
    print(f"Precio unitario: ${precio:.2f}")
    print(f"Cantidad: {cantidad}")
    print(f"Subtotal: ${subtotal:.2f}\n")
    
    # mostrar resumen de la compra
    continuar = input("¿Deseas agregar otro artículo? (si/no): ") #condicional ejecutandose

print(f"Total general a pagar: ${total_general:.2f}")  # ← Muestra del total.
