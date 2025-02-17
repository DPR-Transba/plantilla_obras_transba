# VALORES TIPICOS DE EQUIPAMIENTO DE TRANSBA PARA PSSE
# 
# Los datos de estaciones fueron extraidos de INTRANET > GERENCIA DE INGENIERIA > DOCUMENTOS DE EQUIPOS
# https://drive.google.com/drive/folders/13qQ_FNPxs99hewsdfMp0iHdr9w3OxDKn
#
# Los datos de PPEE fueron extraidos en funcion de diversos EEE1 y EEE2.


# AREAS ========================================================================
AREA_CENTRO = {
    "area": 5,
    "zone": 21,
}

AREA_ATLANTICA = {
    "area": 5,
    "zone": 22,
}

AREA_NORTE = {
    "area": 5,
    "zone": 23,
}

AREA_SUR = {
    "area": 5,
    "zone": 24,
}

# TENSIONES NOMINALES ----------------------------------------------------------
TENSIONES_NOMINALES = [500, 220, 132, 66, 33, 13.2]

# TRANSFORMADORES ==============================================================
# Transformadores 15 MVA -------------------------------------------------------
TRAFO_15_15_15 = {
    "x12": 0.11,
    "x23": 0.06,
    "x31": 0.18,
    "sbs12": 15,
    "rate1": 15,
    "rate2": 15,
    "rate3": 15,
    "nomv1": 132,
    "nomv2": 34.5,
    "nomv3": 13.8,
    "ntp": 21,
    "rma1": 148.5,
    "rmi1": 115.5,
    "xglim": 4.0,
}

TRAFO_15_10_15 = {
    "x12": 0.11,
    "x23": 0.06,
    "x31": 0.18,
    "sbs12": 15,
    "rate1": 15,
    "rate2": 10,
    "rate3": 15,
    "nomv1": 132,
    "nomv2": 34.5,
    "nomv3": 13.8,
    "ntp": 21,
    "rma1": 148.5,
    "rmi1": 115.5,
    "xglim": 4.0,
}

# Transformadores 30 MVA -------------------------------------------------------
TRAFO_30_30_30 = {
    "x12": 0.11,
    "x23": 0.06,
    "x31": 0.18,
    "sbs12": 30,
    "rate1": 30,
    "rate2": 30,
    "rate3": 30,
    "nomv1": 132,
    "nomv2": 34.5,
    "nomv3": 13.8,
    "ntp": 21,
    "rma1": 148.5,
    "rmi1": 115.5,
    "xglim": 2.0,
}

TRAFO_30_20_30 = {
    "x12": 0.11,
    "x23": 0.06,
    "x31": 0.18,
    "sbs12": 30,
    "rate1": 30,
    "rate2": 20,
    "rate3": 30,
    "nomv1": 132,
    "nomv2": 34.5,
    "nomv3": 13.8,
    "ntp": 21,
    "rma1": 148.5,
    "rmi1": 115.5,
    "xglim": 2.0,
}

TRAFO_30_30_20 = {
    "x12": 0.11,
    "x23": 0.06,
    "x31": 0.18,
    "sbs12": 30,
    "rate1": 30,
    "rate2": 20,
    "rate3": 30,
    "nomv1": 132,
    "nomv2": 34.5,
    "nomv3": 13.8,
    "ntp": 21,
    "rma1": 148.5,
    "rmi1": 115.5,
    "xglim": 2.0,
}

# Transformadores 40 MVA -------------------------------------------------------
TRAFO_40_40_40 = {
    "x12": 0.11,
    "x23": 0.06,
    "x31": 0.18,
    "sbs12": 40,
    "rate1": 40,
    "rate2": 40,
    "rate3": 40,
    "nomv1": 132,
    "nomv2": 34.5,
    "nomv3": 13.8,
    "ntp": 21,
    "rma1": 148.5,
    "rmi1": 115.5,
    "xglim": 2.0,
}

TRAFO_40_40_15 = {
    "x12": 0.11,
    "x23": 0.06,
    "x31": 0.18,
    "sbs12": 40,
    "rate1": 40,
    "rate2": 40,
    "rate3": 15,
    "nomv1": 132,
    "nomv2": 34.5,
    "nomv3": 13.8,
    "ntp": 21,
    "rma1": 148.5,
    "rmi1": 115.5,
    "xglim": 2.0,
}

TRAFO_40_30_40 = {
    "x12": 0.11,
    "x23": 0.06,
    "x31": 0.18,
    "sbs12": 40,
    "rate1": 40,
    "rate2": 30,
    "rate3": 40,
    "nomv1": 132,
    "nomv2": 34.5,
    "nomv3": 13.8,
    "ntp": 21,
    "rma1": 148.5,
    "rmi1": 115.5,
    "xglim": 2.0,
}

# TRAFO 44 MVA -----------------------------------------------------------------
TRAFO_44_44_15 = {
    "x12": 0.11,
    "x23": 0.06,
    "x31": 0.18,
    "sbs12": 44,
    "rate1": 44,
    "rate2": 44,
    "rate3": 15,
    "nomv1": 132,
    "nomv2": 34.5,
    "nomv3": 13.8,
    "ntp": 21,
    "rma1": 145.2,
    "rmi1": 118.8,
    "xglim": 2.0,
}

# TRAFO 75 MVA -----------------------------------------------------------------
TRAFO_75_75_25 = {
    "x12": 0.115,
    "x23": 0.06,
    "x31": 0.20,
    "sbs12": 75,
    "rate1": 75,
    "rate2": 75,
    "rate3": 25,
    "nomv1": 132,
    "nomv2": 34.5,
    "nomv3": 13.8,
    "ntp": 21,
    "rma1": 155.25,
    "rmi1": 120.75,
    "xglim": 4.0,
}

# TRAFO 110 MVA ----------------------------------------------------------------
TRAFO_110_110_40 = {
    "x12": 0.13,
    "x23": 0.06,
    "x31": 0.21,
    "sbs12": 110,
    "rate1": 110,
    "rate2": 110,
    "rate3": 40,
    "nomv1": 132,
    "nomv2": 34.5,
    "nomv3": 13.8,
    "ntp": 21,
    "rma1": 148.5,
    "rmi1": 115.5,
    "xglim": 4.0,
}

# TRAFO 120 MVA ----------------------------------------------------------------
TRAFO_120 = {
    "x":  0.13,
    "x0": 0.11,
    "sbs"  : 120,
    "rate": 120,
    "nomv1": 138,
    "nomv2": 33,
    "ntp": 21,
    "rma1": 155.25,
    "rmi1": 120.75,
    "vg": "yd"
}

# TRAFO AERO -------------------------------------------------------------------
TRAFO_V150_VESTAS = {
    "x":  0.099,
    "x0": 0.083,
    "sbs"  : 5.3,
    "rate": 5.3,
    "nomv1": 33,
    "nomv2": 0.72,
    "ntp": 5,
    "rma1": 34.65,
    "rmi1": 31.35,
    "vg": "dy"
}

TRAFO_V162_VESTAS = {
    "x":  0.08,
    "x0": 0.08,
    "sbs"  : 7.5,
    "rate": 7.5,
    "nomv1": 33,
    "nomv2": 0.69,
    "ntp": 5,
    "rma1": 34.65,
    "rmi1": 31.35,
    "vg": "dy"
}

TRAFO_NORDEX_163_57 = {
    "x":  0.085,
    "x0": 0.085,
    "sbs"  : 6.35,
    "rate": 6.35,
    "nomv1": 34,
    "nomv2": 0.75,
    "ntp": 5,
    "rma1": 34.65,
    "rmi1": 31.35,
    "vg": "dy"
}

# GENERADORES ------------------------------------------------------------------
# Datos y unidades
# pmax:     MW 
# pmin:     MW 
# qmax:     MVAR 
# qmin:     MVAR
# mbase:    MVA
# rsource:  PU    
# xsource:  PU     
# icc:      PU 

AERO_VESTAS_V150_45 = {
    "pmax": 4.5,
    "pmin": 0,
    "qmax": 2.55,
    "qmin": -1.6,
    "mbase": 4.5,
    "rsource": 0.05,
    "xsource": 1,
    "icc": 2,
}

AERO_VESTAS_V150_42 = {
    "pmax": 4.2,
    "pmin": 0,
    "qmax": 2.55,
    "qmin": -1.6,
    "mbase": 4.2,
    "rsource": 0.05,
    "xsource": 1,
    "icc": 2,
}

AERO_VESTAS_V162_62 = {
    "pmax": 6.2,
    "pmin": 0,
    "qmax": 2.75,
    "qmin": -2.05,
    "mbase": 6.2,
    "rsource": 0.0,
    "xsource": 0.8,
    "icc": 2,
}

AERO_NORDEX_163_57 = {
    "pmax": 5.7,
    "pmin": 0,
    "qmax": 2.761,
    "qmin": -2.761,
    "mbase": 5.7,
    "rsource": 0.0,
    "xsource": 0.8,
    "icc": 4,
}


# LINEAS =======================================================================
# Datos y unidades
# r:          ohms/km
# x:          ohms/km
# b:          us/km
# r0:         ohms/km
# x0:         ohms/km
# b0:         us/km
# limitante:  A
# conductor:  A
# ti_origen:  A
# ti_destino: A
# op_origen:  A
# op_destino: A

LINEA_AL_300_50 = {
    "r"  : 0.096,
    "x"  : 0.383,
    "b"  : 2.992,
    "r0" : 0.307,
    "x0" : 1.358,
    "b0" : 1.770,
    "limitante" : 600,  
    "conductor" : 650,
    "ti_origen" : 600,
    "ti_destino": 600,
    "op_origen" : 0,
    "op_destino": 0,
}

LINEA_AL_185_30 = {
    "r"  : 0.157,
    "x"  : 0.401,
    "b"  : 2.849,
    "r0" : 0.368,
    "x0" : 1.369,
    "b0" : 1.736,
    "limitante" : 535,  
    "conductor" : 535,
    "ti_origen" : 600,
    "ti_destino": 600,
    "op_origen" : 0,
    "op_destino": 0,
}







