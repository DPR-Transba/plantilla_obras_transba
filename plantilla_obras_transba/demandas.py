import psse34
import psspy

_i = psspy.getdefaultint()
_f = psspy.getdefaultreal()
_s = psspy.getdefaultchar()


def crea_demanda(ibus, id="1"):
    """ """
    psspy.load_data_5(ibus, id, [1, _i, _i, 1, 1, 0, 0])


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

        # Retira el porcentaje de demandas
        psspy.bsys(0, 0, [_f, _f], 0, [], len(ibus), ibus, 0, [], 0, [])
        ierr, (id_arr,) = psspy.aloadchar(0, 1, "ID")
        ierr, (
            number_arr,
            scale_arr,
        ) = psspy.aloadint(0, 1, ["NUMBER", "SCALE"])
        ierr, (slod,) = psspy.aloadcplx(0, 1, "MVAACT")

        s_total = 0
        for num, identifier, scale, slod in zip(number_arr, id_arr, scale_arr, slod):
            if not scale:
                continue
            ierr, slod = psspy.loddt2(num, identifier, "MVA", "ACT")
            s_total += slod
            nuevo_slod = slod * (1 - porcentaje)
            psspy.load_data_5(
                num, identifier, realar1=nuevo_slod.real, realar2=nuevo_slod.imag
            )

        # Pone el porecentaje extraido en nuevas demandas
        psspy.bsys(0, 0, [_f, _f], 0, [], len(jbus), jbus, 0, [], 0, [])
        ierr, (id_arr,) = psspy.aloadchar(0, 1, "ID")
        ierr, (
            number_arr,
            scale_arr,
        ) = psspy.aloadint(0, 1, ["NUMBER", "SCALE"])
        ierr, (slod,) = psspy.aloadcplx(0, 1, "MVAACT")

        len_demandas_escalables = sum(scale_arr)
        for num, identifier, scale, slod in zip(number_arr, id_arr, scale_arr, slod):
            if not scale:
                continue
            ierr, slod = psspy.loddt2(num, identifier, "MVA", "ACT")
            nuevo_slod = slod + porcentaje * s_total / len_demandas_escalables
            psspy.load_data_5(
                num, identifier, realar1=nuevo_slod.real, realar2=nuevo_slod.imag
            )


def balancea_demandas(*ibus):
    """
    Balancea la demanda entre los buses especificados.

    Parámetros:
    *ibus (int): Lista de buses en los que se balanceará la demanda.

    Ejemplo:
    balancea_demanda(225291, 225292)
    """
    mueve_demandas(list(ibus), list(ibus), 1)
