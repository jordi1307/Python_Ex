__author__ = 'jor'
import menus

seleccio = input(menus.menus(input("Inserte modelo de App a buscar 1- App Pago, 2- App Gratis\n")))

if seleccio == "1":
    menus.fucion_mostra(menus.crea_array_appis())
    #auxiliar