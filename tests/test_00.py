import psse34
import psspy
import plantilla_obras_transba
from plantilla_obras_transba import (
    AREA_ATLANTICA,
    TRAFO_110_110_40,
    TRAFO_NORDEX_163_57,
    AERO_NORDEX_163_57,
    TRAFO_30_20_30,
)

psspy.psseinit()

def test_00():
    psspy.newcase_2()

    COLECTOR = {
        "r": 0.00399,  # PU
        "x": 0.00430,  # PU
        "b": 0.01669,  # PU
    }
    plantilla_obras_transba.crea_PPEE(
        2871,
        2770,
        "ARMONIA",
        "VATLEO01",
        AREA_ATLANTICA,
        TRAFO_110_110_40,
        COLECTOR,
        18 * [TRAFO_NORDEX_163_57],
        18 * [AERO_NORDEX_163_57],
    )
    assert psspy.busexs(287131) == 0
    assert psspy.busexs(287132) == 0
    assert psspy.busexs(287191) == 0
    assert psspy.busexs(2871) == 0
    assert psspy.busexs(2770) == 0


def test_01():
    psspy.newcase_2()
    plantilla_obras_transba.crea_estacion(
        2423, "G.BELGRANO", "GBE", AREA_ATLANTICA, 2 * [TRAFO_30_20_30]
    )

    assert psspy.busexs(2423) == 0
    assert psspy.busexs(242331) == 0
    assert psspy.busexs(242332) == 0
    assert psspy.busexs(242391) == 0
    assert psspy.busexs(242392) == 0
    assert psspy.busexs(242301) == 0
    assert psspy.busexs(242302) == 0
