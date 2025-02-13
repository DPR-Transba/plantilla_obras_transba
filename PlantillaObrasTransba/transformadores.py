import psse34
import psspy

_i = psspy.getdefaultint()
_f = psspy.getdefaultreal()
_s = psspy.getdefaultchar()


def crea_trafo_3w(ibus, jbus, kbus, ckt, nombre, sbs12, nomv1, nomv2, nomv3, x12, x23, x31, ntp, rma1, rmi1, rate1, rate2, rate3, xglim):
    """
    Crea un transformador de tres devanados en PSS®E.

    Parámetros::
    ibus (int): Número de barra del devanado primario.
    jbus (int): Número de barra del devanado secundario.
    kbus (int): Número de barra del devanado terciario.
    ckt (str): Identificador del circuito.
    nombre (str): Nombre del transformador.
    sbs12 (float): Potencia base del transformador en MVA.
    nomv1 (float): Tensión nominal del devanado primario en kV.
    nomv2 (float): Tensión nominal del devanado secundario en kV.
    nomv3 (float): Tensión nominal del devanado terciario en kV.
    x12 (float): Impedancia entre primario y secundario (p.u.).
    x23 (float): Impedancia entre secundario y terciario (p.u.).
    x31 (float): Impedancia entre terciario y primario (p.u.).
    ntp (int): Número de taps en el devanado primario.
    rma1 (float): Límite superior del tap en p.u.
    rmi1 (float): Límite inferior del tap en p.u.
    rate1 (float): Capacidad del devanado primario en MVA.
    rate2 (float): Capacidad del devanado secundario en MVA.
    rate3 (float): Capacidad del devanado terciario en MVA.
    xglim (float): Impedancia limitadora en secundario para secuencia de cero en ohms.
    
    Ejemplo:
    
    crea_trafo_3w(2252, 225231, 225291, "2", "JU", **TRAFO_30_30_30)
    """
    psspy.three_wnd_imped_data_4  (ibus, jbus, kbus, ckt, [10, 0, 0, 0, 2, 2, 1, 1, 2, ibus, jbus, kbus], [0.0, x12, 0.0, x23, 0.0, x31, sbs12, sbs12, sbs12, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0], 'TBA_T'+ ckt +nombre)
    psspy.three_wnd_winding_data_5(ibus, jbus, kbus, ckt, 1, [ntp, 0, jbus, 0, 1, 1], [nomv1, nomv1, 0.0, rma1, rmi1, 1.05, 0.95, 0.0, 0.0, 0.0], [rate1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    psspy.three_wnd_winding_data_5(ibus, jbus, kbus, ckt, 2, [33, 0, 0, 0, 1, 0], [nomv2, nomv2, 0.0, 1.1, 0.9, 1.1, 0.9, 0.0, 0.0, 0.0], [rate2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    psspy.three_wnd_winding_data_5(ibus, jbus, kbus, ckt, 3, [33, 0, 0, 0, 1, 0], [nomv3, nomv3, 0.0, 1.1, 0.9, 1.1, 0.9, 0.0, 0.0, 0.0], [rate3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    psspy.seq_three_winding_data_3(ibus, jbus, kbus, ckt, [2, 3, 12], [0.0, 0.0, 0.0, x12, 0.0, xglim, 0.0, x23, 0.0, 0.0, 0.0, x31, 0.0, 0.0])


def crea_trafo_2w(ibus, jbus, ckt, nombre, sbs, nomv1, nomv2, x, x0, ntp, rma1, rmi1, rate, vg):
    """
    Crea un transformador de dos devanados en PSS®E.

    Parametros:
    ibus (int): Número de barra del devanado primario.
    jbus (int): Número de barra del devanado secundario.
    ckt (str): Identificador del circuito.
    nombre (str): Nombre del transformador.
    sbs (float): Potencia base del transformador en MVA.
    nomv1 (float): Tensión nominal del devanado primario en kV.
    nomv2 (float): Tensión nominal del devanado secundario en kV.
    x (float): Impedancia entre primario y secundario (p.u.).
    x0 (float): Impedancia en secuencia de cero (p.u.).
    ntp (int): Número de taps en el devanado primario.
    rma1 (float): Límite superior del tap en p.u.
    rmi1 (float): Límite inferior del tap en p.u.
    rate (float): Capacidad nominal del transformador en MVA.
    vg (str): Grupo vectorial del transformador (ej. "DY", "YD").

    crea_trafo_2w(601, 550, "2", "", **TRAFO_V150_VESTAS)        
    """
    psspy.two_winding_data_6(ibus, jbus, ckt, [1, ibus, _i, 0, 0, 0, ntp, 0, ibus, 0, 0, 1, 0, 2, 2, 1], [0.0, x, sbs, nomv1, nomv1, 0.0, nomv2, nomv2, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, rma1, rmi1, 1.1, 0.9, 0.0, 0.0, 0.0], [rate, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], nombre)    

    if vg.lower() == "dy":
        cc = 13
    elif vg.lower() == "yd":
        cc = 12
    else:
        cc = 12
    psspy.seq_two_winding_data_3(ibus, jbus, ckt, [cc, 2, 2], [0.0, 0.0, 0.0, x0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])


def crea_reactor_zig_zag(ibus, jbus, ckt, codigo, ohms=11):
    """
    Crea un reactor zig-zag en PSS®E.

    Parametros:
    ibus (int): Número de la barra primaria.
    jbus (int): Número de la barra secundaria.
    ckt (str): Identificador del circuito.
    codigo (str): Código identificador del reactor.
    ohms (float): Impedancia del reactor en ohmios.


    Ejemplo:
    crea_reactor_zig_zag(225291, 225201, "1", "JU", 2.0)
    """
    ierr, ubase = psspy.busdat(ibus, "BASE")
    zbase = ubase ** 2 / psspy.sysmva()    
    psspy.two_winding_data_6(ibus, jbus, ckt, namear='TBA_RNT{}{}'.format(ckt, codigo))
    psspy.seq_two_winding_data_3(ibus, jbus, ckt, [2, 1, 1], [0.0, 0.0, 0.0, ohms/zbase, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
