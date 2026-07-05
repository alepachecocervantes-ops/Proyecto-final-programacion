# Matriz del inventario
inventario = [
    ["A001", "Mouse", 4, 10],
    ["A002", "Teclado", 15, 10],
    ["A003", "Monitor", 3, 8],
    ["A004", "Cámara", 12, 12],
    ["A005", "Parlantes", 1, 5]
]

# Función para calcular la cantidad a pedir
def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

# Título del reporte
print("==== REPORTE DE INVENTARIO ====")

# Recorrer la matriz
for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad = calcular_pedido(stock_actual, stock_minimo)

    print("--------------------------------")
    print("Código:", codigo)
    print("Artículo:", nombre)
    print("Stock actual:", stock_actual)
    print("Stock mínimo:", stock_minimo)
    print("Cantidad a pedir:", cantidad)

print("--------------------------------")
print("Fin del reporte")