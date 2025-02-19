import psse34
import psspy
from constantes import (
    TENSIONES_NOMINALES,
    TENSIONES_LIMITE_SUPERIOR_NORMAL_PU,
    TENSIONES_LIMITE_INFERIOR_NORMAL_PU,
    TENSIONES_LIMITE_INFERIOR_EMERGENCIA_PU,
    TENSIONES_LIMITE_SUPERIOR_EMERGENCIA_PU,
)


def obtiene_tension_nominal(u_kv):
    """
    Devuelve la tensión nominal más cercana en PSS®E.

    Parámetros:
    u_kv (float): Valor de tensión en kV.

    Retorna:
    float: La tensión nominal más cercana en kV.

    Ejemplo:
    obtiene_tension_nominal(118.0)
    """

    diferencias = [abs(u_nom - u_kv) for u_nom in TENSIONES_NOMINALES]
    indice = min(range(len(diferencias)), key=lambda x: diferencias[x])
    return TENSIONES_NOMINALES[indice]


def codigo_de_tension_barras(u_kv):
    """
    Obtiene el código de tensión asociado a una barra en PSS®E.

    Parámetros:
    u_kv (float): Nivel de tensión en kV.

    Retorna:
    int: Código de tensión correspondiente según el mapeo predefinido.

    Notas:
    - Si el nivel de tensión no está en el mapeo, devuelve 0.
    - Los códigos de tensión están definidos según valores nominales estándar.

    Ejemplo:
    codigo_de_tension_barras(132.0)  # Retorna 1
    """
    u_nom = obtiene_tension_nominal(u_kv)
    mapeo ={   
        500 : 5,
        220 : 2,
        132 : 1,
        66  : 6,
        33  : 3,
        13.2: 9,
    }
    return mapeo.get(u_nom, 0)



def crea_barra(numero, tension, nombre, area, zone, owner=1, type=1):
    """
    Crea una barra en PSS®E.

    Parámetros:
    numero (int): Número de identificación de la barra.
    tension (float): Nivel de tensión nominal de la barra en kV.
    nombre (str): Nombre de la barra.
    area (int): Área a la que pertenece la barra.
    zone (int): Zona a la que pertenece la barra.
    owner (int, opcional): Identificación del propietario de la barra (por defecto 1).
    type (int, opcional): Tipo de barra (por defecto 1).

    Ejemplo:
    crea_barra(101, 132.0, "BARRA_101", 1, 1)
    """
    nvllo = TENSIONES_LIMITE_INFERIOR_NORMAL_PU.get(tension, 0.9)
    nvlhi = TENSIONES_LIMITE_SUPERIOR_NORMAL_PU.get(tension, 1.1)
    evllo = TENSIONES_LIMITE_INFERIOR_EMERGENCIA_PU.get(tension, 0.9)
    evlhi = TENSIONES_LIMITE_SUPERIOR_EMERGENCIA_PU.get(tension, 1.1)
    psspy.bus_data_4(
        numero,
        0,
        [type, area, zone, owner],
        [float(tension), 1.0, 0.0, nvlhi, nvllo, evlhi, evllo],
        nombre,
    )
