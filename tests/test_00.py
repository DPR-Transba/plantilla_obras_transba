import psse34
import psspy
import plantillaobrastransba
from plantillaobrastransba import AREA_ATLANTICA, TRAFO_110_110_40, TRAFO_NORDEX_163_57, AERO_NORDEX_163_57

psspy.psseinit()

def test_00():
    psspy.newcase_2()

COLECTOR = {
    "r": 0.00399, # PU
    "x": 0.00430, # PU
    "b": 0.01669, # PU
}
plantillaobrastransba.crea_PPEE(2871, 2770, "ARMONIA", "VATLEO01", AREA_ATLANTICA, TRAFO_110_110_40, COLECTOR, 18*[TRAFO_NORDEX_163_57], 18*[AERO_NORDEX_163_57])

    assert psspy.busexs(287131) == 0
    assert psspy.busexs(287132) == 0
    assert psspy.busexs(287191) == 0
    assert psspy.busexs(2871) == 0
    assert psspy.busexs(2770) == 0



