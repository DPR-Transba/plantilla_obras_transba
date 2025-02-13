import psse34
import psspy

def crea_generador_eolico(gbus, identifier, pmax, pmin, qmax, qmin, mbase, rsource, xsource, icc):
    """
    Crea un generador eólico en un sistema de potencia utilizando PSSE.

    Parámetros:
    gbus (int): Identificador de la barra donde se conectará el generador.
    identifier (str): Identificador del generador.
    pmax (float): Potencia activa máxima del generador (MW).
    pmin (float): Potencia activa mínima del generador (MW).
    qmax (float): Potencia reactiva máxima del generador (MVAR).
    qmin (float): Potencia reactiva mínima del generador (MVAR).
    mbase (float): Base de potencia del generador (MVA).
    rsource (float): Resistencia interna de la fuente equivalente del generador (pu).
    xsource (float): Reactancia interna de la fuente equivalente del generador  (pu).
    icc (float): Corriente de cortocircuito del generador (pu).

    Ejemplo de uso:
    crea_generador_eolico(2706, "1", 100.0, 10.0, 50.0, -50.0, 120.0, 0.005, 0.1, 1.5)
    """
    psspy.plant_data(gbus, [gbus], [1.00, 100.0])
    psspy.machine_data_2(gbus, identifier, [1, 11, 0, 0, 0, 1], [0.5 * pmax, 0, qmax, qmin, pmax, pmin, mbase, rsource, xsource, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
    psspy.seq_ncs_flt_cntrb_data(gbus, identifier, 1, [0.0], [icc * 1j])
