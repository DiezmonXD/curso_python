def faltan_pruebas():
    pruebas_totales = 12
    pruebas_pasadas = input('¿Cuántas pruebas as pasado?')
    diferencia = pruebas_totales - int (pruebas_pasadas)
    diferencia = str (diferencia)
    return ' Te faltan por pasar un total de ' + diferencia + ' pruebas '
