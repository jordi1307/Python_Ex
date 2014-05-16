__author__ = 'jor'
import Items.aplicacion


def menus(num_menu):
    menu = "C:\\Users\jor\Desktop\DAM\DAM2\phyton\Python\proyecto-pycharm\Python_Ex"
    if num_menu == "1":
        menu += "\menus\menu1.txt"
        mostra_fiche(menu)
    if num_menu == "2":
        menu += "\menus\menu2.txt"
        mostra_fiche(menu)
    else:
        print("fin")


def mostra_fiche(ruta):
    print(ruta)
    with open(ruta, mode='r', encoding='utf-8') as contingut:
        for linea in contingut:
            print(linea.rstrip())


def carrega_fiche(ruta):
    fiche = []
    with open(ruta, mode='r', encoding='utf-8') as carrega:
        linea = carrega.read().splitlines(":")
        fiche.append(linea)
    return fiche


def crea_array_appis():
    fiche = carrega_fiche(
        "C:\\Users\jor\Desktop\DAM\DAM2\phyton\Python\proyecto-pycharm\Python_Ex\BBDD\\aplicaciones.txt")
    for linea in fiche:
        app = Items.aplicacion.Aplicacion(linea[0], linea[1], linea[2], linea[3], linea[4], linea[5], linea[6],
                                          linea[7],
                                          linea[8])
        arrayApps = {app.posicion(): app}
        #si sale la misma posicion se re esciben no lo e controlado

    return arrayApps


def fucion_mostra(arrayApps):
    for key in arrayApps.keys():
        print(str(arrayApps[key].To_setring_seif()))


        #  nombre,
        # proveedor,
        # fecha_publicacion,
        # precio,
        # numero_de_descargas,
        # numero_de_puntuaciones_obtenidas,
        # puntuacions,
        # numero_de_comentarios
