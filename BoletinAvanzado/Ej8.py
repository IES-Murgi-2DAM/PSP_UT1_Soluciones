tienda_a = {"manzanas", "naranjas", "plátanos", "leche"}
tienda_b = {"plátanos", "leche", "pan", "huevos"}

# Para calcular la intersección de los productos disponibles en ambas tiendas, podemos usar el operador de
# intersección (&) o el método intersection() de los conjuntos.
def productos_comunes(tienda1, tienda2):
    return tienda1 & tienda2  # También se puede usar tienda1.intersection(tienda2)

# Para calcular los productos exclusivos de cada tienda, podemos usar el operador de diferencia (-) o el método
# difference() de los conjuntos. Devolveremos una tupla con dos conjuntos: el primero con los productos exclusivos de la
# primera tienda y el segundo con los productos exclusivos de la segunda tienda.
def productos_exclusivos(tienda1, tienda2):
    exclusivos_tienda1 = tienda1 - tienda2  # Productos en tienda1 pero no en tienda2
    exclusivos_tienda2 = tienda2 - tienda1  # Productos en tienda2 pero no en tienda1
    return exclusivos_tienda1, exclusivos_tienda2

# Para calcular todos los productos sin duplicados, podemos usar el operador de unión (|) o el método union() de los
# conjuntos.
def todos_los_productos(tienda1, tienda2):
    return tienda1 | tienda2  # También se puede usar tienda1.union(tienda2)

# Para calcular los productos que están en una tienda pero no en la otra (diferencia simétrica), podemos usar el
# operador de diferencia simétrica (^) o el método symmetric_difference() de los conjuntos.
def productos_diferencia_simetrica(tienda1, tienda2):
    return tienda1 ^ tienda2  # También se puede usar tienda1.symmetric_difference(tienda2)

if __name__ == "__main__":
    print("Productos comunes:", productos_comunes(tienda_a, tienda_b))
    exclusivos_a, exclusivos_b = productos_exclusivos(tienda_a, tienda_b)
    print("Productos exclusivos de la tienda A:", exclusivos_a)
    print("Productos exclusivos de la tienda B:", exclusivos_b)
    print("Todos los productos sin duplicados:", todos_los_productos(tienda_a, tienda_b))
    print("Productos en la tienda A pero no en la tienda B y viceversa (diferencia simétrica):",
          productos_diferencia_simetrica(tienda_a, tienda_b))