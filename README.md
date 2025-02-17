# Plantilla de Obras de Transba

## Descripción

Estas funciones están diseñadas para estandarizar las obras de transporte para la Guía de Referencia y otros estudios particulares.

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/DPR-Transba/plantilla_obras_transba.git
   ```
2. Acceder al directorio del proyecto:
   ```bash
   cd plantilla_obras_transba
   ```
3. Configurar según los requerimientos de la obra.
   ```bash
   python.exe -m pip install .
   ```

## Pruebas de desarrollo

Para ejecutar las pruebas, usar:
   ```bash
   pytest
   ```

## Uso

### Ejemplo para la creación de un PPEE

Ejemplo de creación de un Parque de Producción de Energía Eólica (PPEE), en este caso para el PE Vientos del Atlántico:

```python
from plantilla_obras_transba import crea_PPEE, secciona_linea_con_doble_terna, LINEA_AL_300_50, TRAFO_110_110_40, TRAFO_NORDEX_163_57, AERO_NORDEX_163_57

porcentaje = 78 / (78 + 6.34)
secciona_linea_con_doble_terna(2356, 2410, "1", porcentaje, 2871, "ARMONIA", ["1ARNVG1", "1ARNVIV1"], 3.0, **LINEA_AL_300_50)
COLECTOR = {
    "r": 0.00399, # PU
    "x": 0.00430, # PU
    "b": 0.01669, # PU
}
crea_PPEE(2871, 2770, "ARMONIA", "VATLEO01", AREA_ATLANTICA, TRAFO_110_110_40, COLECTOR, 18*[TRAFO_NORDEX_163_57], 18*[AERO_NORDEX_163_57])
```

### Ejemplo de estación transformadora típica

Ejemplo de estación transformadora para el abastecimiento de la demanda:

```python
from plantilla_obras_transba import AREA_ATLANTICA, TRAFO_30_20_30, crea_estacion, crea_linea, mueve_demandas

crea_estacion(2423, "G.BELGRANO", "GBE", AREA_ATLANTICA, 2 * [TRAFO_30_20_30])
crea_linea(2423, 2263, "1", 35, "1GBE-NW1", **LINEA_AL_300_50)

mueve_demandas([222931, 222991, 222932, 222992], [242331, 242391, 242332, 242392], 0.25) # Extrae demandas de Monte
mueve_demandas([228431, 228491, 228432, 228492], [242331, 242391, 242332, 242392], 0.15) # Extrae demandas de Chascomús

mueve_demandas([242391, 242392, 242331, 242332], [242331, 242332], 1)
mueve_demandas([242331, 242332], [242391, 242392], 0.3) # Distribución de demandas 30 % en 13,2
```

## Ejemplos

Para más ejemplos, consulta el archivo [ejemplos](tests/ejemplos.py).

