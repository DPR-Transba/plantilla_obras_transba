import psse34
import psspy
from math import sqrt


def crea_linea(ibus, jbus, ckt, length, name, r, x, b, r0, x0, b0, limitante, conductor, ti_origen, ti_destino, op_origen, op_destino):
    """
    Crea una línea de transmisión en el sistema de potencia utilizando PSSE.

    Parámetros:
    ibus (int): Identificador de la barra de origen.
    jbus (int): Identificador de la barra de destino.
    ckt (str): Identificador del circuito.
    length (float): Longitud de la línea en kilómetros.
    name (str): Nombre identificador de la línea.
    r (float): Resistencia positiva por unidad de longitud (ohm/km).
    x (float): Reactancia positiva por unidad de longitud (ohm/km).
    b (float): Susceptancia positiva por unidad de longitud (ohm/km).
    r0 (float): Resistencia de secuencia cero por unidad de longitud (ohm/km).
    x0 (float): Reactancia de secuencia cero por unidad de longitud (ohm/km).
    b0 (float): Susceptancia de secuencia cero por unidad de longitud (ohm/km).
    limitante (float): Corriente límite de la línea en A.
    conductor (float): Capacidad del conductor en A.
    ti_origen (float): Ajuste del TI en A en el extremo de origen.
    ti_destino (float): Ajuste del TI en A en el extremo de destino.
    op_origen (float): Onda portadora en A en el extremo de origen.
    op_destino (float): Onda portadora en A en el extremo de destino.

    NOTA: El extremo de origen es ibus y el de destino es jbus.

    Ejemplo de uso:
    LINEA_AL_300_50 = {
        "r": 0.1,
        "x": 0.4,
        "b": 3.2,
        "r0": 0.3,
        "x0": 1.2,
        "b0": 1.1,
        "limitante": 1000,
        "conductor": 900,
        "ti_origen": 600,
        "ti_destino": 600,
        "op_origen": 1,
        "op_destino": 1
    }

    crea_linea(2000, 2200, "1", 120, "1JURF1", **LINEA_AL_300_50)
    """
    
    ierr, ubase = psspy.busdat(ibus, "BASE")
    zbase = ubase ** 2 / psspy.sysmva()

    r *= length / zbase
    x *= length / zbase
    b *= length * zbase * 1e-6

    r0 *= length / zbase
    x0 *= length / zbase
    b0 *= length * zbase * 1e-6

    limitante  *= sqrt(3) * ubase / 1000
    conductor  *= sqrt(3) * ubase / 1000
    ti_origen  *= sqrt(3) * ubase / 1000
    ti_destino *= sqrt(3) * ubase / 1000
    op_origen  *= sqrt(3) * ubase / 1000
    op_destino *= sqrt(3) * ubase / 1000

    psspy.branch_data_3(ibus, jbus, ckt, [1, 1, 10, 0, 0, 0], [r, x, b, 0.0, 0.0, 0.0, 0.0, length, 1.0, 0.0, 0.0, 0.0],[limitante, 0.0, conductor, ti_origen, ti_destino, op_origen, op_destino, 0.0, 0.0, 0.0, 0.0, 0.0], "TBA_" + name)
    psspy.seq_branch_data_3(ibus, jbus, ckt, 0,[r0, x0, b0, 0, 0, 0, 0, 0])




def secciona_linea_con_doble_terna(ibus, jbus, ckt, fraction, kbus, bus_name, lines_name, length, r, x, b, r0, x0, b0, limitante, conductor, ti_origen, ti_destino, op_origen, op_destino):
    """
    Secciona una línea de transmisión con doble terna en un nuevo nodo intermedio.
    Añade la parte de línea en DT sobre cada uno de los nuevos lados de las líneas.
    Si el nodo existe genera el corte de la línea en un dummy bus y luego las mueve.

    Parámetros:
    ibus (int): Identificador de la barra de origen.
    jbus (int): Identificador de la barra de destino.
    ckt (str): Identificador del circuito original.
    fraction (float): Fracción de la línea donde se inserta la nueva barra (0.0 - 1.0).
    kbus (int): Identificador de la nueva barra de seccionamiento.
    bus_name (str): Nombre de la nueva barra.
    lines_name (list): Lista con los nombres de las dos nuevas líneas resultantes.
    length (float): Longitud adicional agregada a las líneas en kilómetros.
    r (float): Resistencia positiva por unidad de longitud (ohm/km).
    x (float): Reactancia positiva por unidad de longitud (ohm/km).
    b (float): Susceptancia positiva por unidad de longitud (ohm/km).
    r0 (float): Resistencia de secuencia cero por unidad de longitud (ohm/km).
    x0 (float): Reactancia de secuencia cero por unidad de longitud (ohm/km).
    b0 (float): Susceptancia de secuencia cero por unidad de longitud (ohm/km).
    limitante (float): Corriente límite de la línea en A.
    conductor (float): Capacidad del conductor en A.
    ti_origen (float): Ajuste del TI en A en el extremo de origen.
    ti_destino (float): No utilizado.
    op_origen (float): Onda portadora en A en el extremo de origen.
    op_destino (float): No utilizado.

    Ejemplo de uso:

    secciona_linea_con_doble_terna(2362, 2233, "1", 0.50, 2292, "CAMPANA", ["1CAZA1", "1CACP1"], 2.0, **LINEA_AL_300_50)
    """

    # Corta la linea
    if psspy.busexs(kbus) == 0:
        print("Warning: Se corta una linea con una barra existente")
        print(
        """
        Procedimiento:
        
        (1)                     (2)                     (3)
        
        A ----------- B         A -----D----- B         A ----   ---- B
                                                              | |
               C                       C                       C
        """
        )
        psspy.ltap(ibus, jbus, ckt, fraction,999997,"DUMMY", 1.0)
        
        # Las lineas se deben mover a un circuito nuevo
        existe_linea = lambda ibus, jbus, ckt: not psspy.brnint(ibus,jbus,str(ckt),"STATUS")[0] == 2
        
        new_ckt_1 = 1
        while existe_linea(ibus, kbus, new_ckt_1):
            new_ckt_1 += 1
        new_ckt_1 = str(new_ckt_1)
        psspy.movebrn(ibus, 999997, ckt, kbus, new_ckt_1)
        
        new_ckt_2 = 1
        while existe_linea(jbus, kbus, new_ckt_2):
            new_ckt_2 += 1
        new_ckt_2 = str(new_ckt_2)
        psspy.movebrn(jbus, 999997, ckt, kbus, new_ckt_2)

        psspy.bsysinit(1)
        psspy.bsyso(1,999997)
        psspy.extr(1,0,[0,0])
    else:
        ierr, base = psspy.busdat(ibus, "BASE")
        psspy.ltap(ibus, jbus, ckt, fraction, kbus, bus_name, base)
        new_ckt_1 = new_ckt_2 = "1"

    
    # Valores que se adicionan a la linea a cortar con los parametros tipicos definidos
    ierr, ubase = psspy.busdat(ibus, "BASE")
    zbase = ubase ** 2 / psspy.sysmva()

    r *= length / zbase
    x *= length / zbase
    b *= length * zbase * 1e-6

    r0 *= length / zbase
    x0 *= length / zbase
    b0 *= length * zbase * 1e-6

    # Extiende la longitud de la linea 1    
    ierr, original_length = psspy.brndat(ibus, kbus, new_ckt_1, "LENGTH")
    ierr, rx    = psspy.brndt2(ibus, kbus, new_ckt_1, "RX")
    ierr, char  = psspy.brndat(ibus, kbus, new_ckt_1, "CHARG")
    ierr, rxz   = psspy.brndt2(ibus, kbus, new_ckt_1, "RXZ")
    ierr, charz = psspy.brndat(ibus, kbus, new_ckt_1, "CHARGZ")
    psspy.branch_chng_3(ibus, kbus, new_ckt_1, realar1=rx.real + r, realar2=rx.imag + x, realar3=char + b, realar8=original_length + length, namear=lines_name[0])
    psspy.seq_branch_data_3(ibus, kbus, new_ckt_1, realar1=rxz.real + r0, realar2=rxz.imag + x0, realar3=charz + b0)
    
    # Extiende la longitud de la linea 2
    ierr, original_length = psspy.brndat(jbus, kbus, new_ckt_2, "LENGTH")
    ierr, rx    = psspy.brndt2(jbus, kbus, new_ckt_2, "RX")
    ierr, char  = psspy.brndat(jbus, kbus, new_ckt_2, "CHARG")
    ierr, rxz   = psspy.brndt2(jbus, kbus, new_ckt_2, "RXZ")
    ierr, charz = psspy.brndat(jbus, kbus, new_ckt_2, "CHARGZ")
    psspy.branch_chng_3(jbus, kbus, new_ckt_2, realar1=rx.real + r, realar2=rx.imag + x, realar3=char + b, realar8=original_length + length, namear=lines_name[1])
    psspy.seq_branch_data_3(jbus, kbus, new_ckt_2, realar1=rxz.real + r0, realar2=rxz.imag + x0, realar3=charz + b0)
    
    
    # Ajusta los rates de las lineas
    
    
    # Ajusta los rates de la linea 2
    
    

