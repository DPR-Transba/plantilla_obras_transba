import psse34
import psspy

from .transformadores import crea_trafo_2w, crea_trafo_3w, crea_reactor_zig_zag
from .generadores import crea_generador_eolico


def crea_estacion(ibus, nombre, codigo, area, trafos):
    """    
    Crea una estación de demanda con sus transformadores y reactores asociados.
    
    Parámetros:
    ibus (int): Identificador del bus principal.
    nombre (str): Nombre de la estación.
    codigo (str): Código identificador de la estación segun TOS02.
    area (dict): Diccionario con información de área y zona.
    trafos (list): Lista de diccionario con configuraciones de transformadores.

    Ejemplo:
    crea_estacion(2252, "JUNIN", "JU", AREA_SUR, [TRAFO_44_44_15] * 2)
    mueve_demanda()
    """

    if psspy.busexs(ibus) == 1:
        psspy.bus_data_4(ibus, 0, [1, area["area"], area["zone"], 1], [132.0, 1.0, 0.0, 1.05, 0.95, 1.1, 0.9], nombre)

    if isinstance(trafos, list):
        for i, trafo in enumerate(trafos, start=1):
            bus_zz =  int("{}0{}".format(ibus, i))
            bus_sec = int("{}3{}".format(ibus, i))
            bus_ter = int("{}9{}".format(ibus, i))

            psspy.bus_data_4(bus_zz, 0, [1, area["area"], area["zone"], 1], [1.00, 1.0, 0.0, 1.07, 0.93, 1.1, 0.9], "FICT.{}.ZZ".format(codigo))
            psspy.bus_data_4(bus_sec, 0, [1, area["area"], area["zone"], 1], [33.0, 1.0, 0.0, 1.07, 0.93, 1.1, 0.9], "{}.SEC.T{}".format(codigo, i))
            psspy.bus_data_4(bus_ter, 0, [1, area["area"], area["zone"], 1], [13.2, 1.0, 0.0, 1.07, 0.93, 1.1, 0.9], "{}.TER.T{}".format(codigo, i))
            
            crea_trafo_3w(ibus, bus_sec, bus_ter, str(i), codigo,**trafo)
            crea_reactor_zig_zag(bus_ter, bus_zz, str(i), codigo, 11.0)

            psspy.load_data_5(bus_sec, "1")
            psspy.load_data_5(bus_ter, "1")


def crea_PPEE(ibus, gbus, nombre, codigo, area, trafo_estacion, colector, trafo_generador, generador):
    """
    Crea un parque de eólico. Los datos del colector deben ir en PU.
    Se pueden indicar tantos aeros como sea necesario multiplicando una lista de los mismos.
    
    Parámetros:
    ibus (int): Identificador de la barra de interconexión.
    gbus (int): Identificador de la barra del generador.
    nombre (str): Nombre del parque eólico.
    codigo (str): Código identificador del parque.
    area (dict): Diccionario con información del área y zona.
    trafo_estacion (dict): Parámetros del transformador de estación.
    colector (dict): Parámetros eléctricos del colector.
    trafo_generador (dict o list): Parámetros del transformador del generador.
    generador (dict o list): Parámetros del generador eólico.
    
    Ejemplo de uso:

    COLECTOR = {
        "r": 0.006760, # pu
        "x": 0.006300, # pu
        "b": 0.018300, # pu
    }
    crea_PPEE(2431, 2706, "TRESPICOS.S", "VICTEO01", AREA_SUR, TRAFO_120, COLECTOR, 21*[TRAFO_AERO], 21*[AERO_VESTAS])
    """

    # Crea barras
    bmt1 = int(str(ibus) + "31")
    bmt2 = int(str(ibus) + "32")
    
    codigo_corto = codigo[:-4]
    
    if isinstance(trafo_generador, list):
        tension_generador = trafo_generador[0]["nomv2"]
    else:
        tension_generador = trafo_generador["nomv2"]
    
    psspy.bus_data_4(ibus, 0, [1, area["area"], area["zone"], 10], [132.0, 1.0, 0.0, 1.05, 0.95, 1.1, 0.9], nombre)
    psspy.bus_data_4(bmt1, 0, [1, area["area"], area["zone"], 11], [33, 1.0, 0.0, 1.07, 0.93, 1.1, 0.9], "{}_01".format(codigo_corto))
    psspy.bus_data_4(bmt2, 0, [1, area["area"], area["zone"], 11], [33, 1.0, 0.0, 1.07, 0.93, 1.1, 0.9], "{}_02".format(codigo_corto))
    psspy.bus_data_4(gbus, 0, [2, area["area"], area["zone"], 11], [tension_generador, 1.0, 0.0, 1.05, 0.95, 1.1, 0.9], codigo)
    
    # Crea trafos
    if trafo_estacion.has_key("x12"):
        bmt3 = int(str(ibus) + "91")
        psspy.bus_data_4(bmt3, 0, [1, area["area"], area["zone"], 11], [13.2, 1.0, 0.0, 1.07, 0.93, 1.1, 0.9], "{}_03".format(codigo_corto))
        crea_trafo_3w(ibus, bmt1, bmt3,"1", "", **trafo_estacion)        
    else:
        crea_trafo_2w(ibus, bmt1, "1", "", **trafo_estacion)
 
    if isinstance(trafo_generador, list):
        trafo_generador_ajustado = trafo_generador[0].copy()        
        trafo_generador_ajustado["sbs"]  = trafo_generador[0].get("sbs")  * len(trafo_generador)
        trafo_generador_ajustado["rate"] = trafo_generador[0].get("rate") * len(trafo_generador)        
        crea_trafo_2w(bmt2, gbus, "1", "", **trafo_generador_ajustado)
    else:
        crea_trafo_2w(ibus, bmt1, "1", "", **trafo_generador)

    # Crea generador
    if isinstance(trafo_generador, list):
        generador_ajustado = generador[0].copy()        
        generador_ajustado["pmax"]  = generador[0].get("pmax")  * len(generador)
        generador_ajustado["qmax"]  = generador[0].get("qmax")  * len(generador)        
        generador_ajustado["qmin"]  = generador[0].get("qmin")  * len(generador)        
        generador_ajustado["mbase"] = generador[0].get("mbase") * len(generador)        
        crea_generador_eolico(gbus, "1", **generador_ajustado)
    else:
        crea_generador_eolico(gbus, "1", **generador)

    # Crea colector
    r = colector["r"]
    x = colector["x"]
    b = colector["b"]
    psspy.branch_data_3(bmt1, bmt2, '1', [1, 1, 11, 0, 0, 0], [r, x, b, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0, 0, 0])


def mueve_demandas(ibus, jbus, porcentaje=1):
    """
    Redistribuye la demanda eléctrica entre diferentes barras.
    
    Parámetros:
    ibus (int o list): Bus o lista de buses de origen.
    jbus (int o list): Bus o lista de buses de destino.
    porcentaje (float): Porcentaje de demanda a transferir 0 <= porcentaje <= 1.
    """
    
    if isinstance(ibus, int):
        return mueve_demandas([ibus], jbus, porcentaje)

    if isinstance(jbus, int):
        return mueve_demandas(ibus, [jbus], porcentaje)

    if isinstance(ibus, list) and isinstance(jbus, list):        
        print psspy.bsys(0,0,[_f,_f],0,[],len(ibus),ibus,0,[],0,[])
        ierr, (id_arr,) = psspy.aloadchar(0, 1, "ID")
        ierr, (number_arr, scale_arr,) = psspy.aloadint(0, 1, ["NUMBER", "SCALE"])
        ierr, (slod,) = psspy.aloadcplx(0, 1, "MVAACT")
    
        s_total = 0       
        for num, identifier, scale, slod in zip(number_arr, id_arr, scale_arr, slod):
            if not scale: continue
            ierr, slod = psspy.loddt2(num, identifier, "MVA", "ACT")            
            s_total += slod
            nuevo_slod = slod * (1 - porcentaje)
            psspy.load_data_5(num, identifier, realar1=nuevo_slod.real, realar2=nuevo_slod.imag)

        psspy.bsys(0,0,[_f,_f],0,[],len(jbus),jbus,0,[],0,[])
        ierr, (id_arr,) = psspy.aloadchar(0, 1, "ID")
        ierr, (number_arr, scale_arr,) = psspy.aloadint(0, 1, ["NUMBER", "SCALE"])
        ierr, (slod,) = psspy.aloadcplx(0, 1, "MVAACT")
    
        len_demandas_escalables = sum(scale_arr)
        for num, identifier, scale, slod in zip(number_arr, id_arr, scale_arr, slod):
            if not scale: continue
            ierr, slod = psspy.loddt2(num, identifier, "MVA", "ACT")            
            nuevo_slod = slod + porcentaje * s_total / len_demandas_escalables
            psspy.load_data_5(num, identifier, realar1=nuevo_slod.real, realar2=nuevo_slod.imag)


def balancea_demandas(*ibus):
    """
    Balancea la demanda entre los buses especificados.
    
    Parámetros:
    *ibus (int): Lista de buses en los que se balanceará la demanda.

    Ejemplo:
    balancea_demanda(225291, 225292)
    """
    mueve_demandas(list(ibus), list(ibus), 1)
