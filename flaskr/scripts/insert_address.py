from cmath import isnan
import pandas as pd
import numpy as np
from iteration_utilities import unique_everseen

# Cargo una lista de dataframes por cada hoja en el archivo
dataframes = pd.read_excel(
    'static/excel/CPdescarga.xls',
    sheet_name=None,
    converters={'d_codigo': str, 'd_CP': str, 'c_estado': str, 'c_oficina': str,
                'c_tipo_asenta': str, 'c_mnpio': str, 'id_asenta_cpcons': str, 'c_cve_ciudad': str}
)


def get_estados_excel():
    # estados = set()
    estados = []

    # Recorro cada uno de los sheets
    for key in dataframes:
        if key == 'Nota':
            continue

        dt = dataframes[key]

        for _, row in dt.iterrows():
            estado = row['d_estado']
            clave_estado = row['c_estado']
            estados.append({"estado": estado, "clave_estado": clave_estado})
        # estados_dt = dt['d_estado'].unique()

        # estados.update(estados_dt)

    # return sorted(estados)
    return list(unique_everseen(estados))


def get_ciudades_excel():
    ciudades = []

    for key in dataframes:
        if key == 'Nota':
            continue

        dt = dataframes[key]

        for _, row in dt.iterrows():
            ciudad = row['d_ciudad']
            clave_ciudad = row['c_cve_ciudad']
            
            if type(ciudad) == float and type(clave_ciudad) == float and (isnan(ciudad) and isnan(clave_ciudad)):
                continue
            
            ciudades.append({"ciudad": ciudad, "clave_ciudad": clave_ciudad})

    return list(unique_everseen(ciudades))


def get_municipios_excel():
    municipios = []

    for key in dataframes:
        if key == 'Nota':
            continue

        dt = dataframes[key]

        for _, row in dt.iterrows():
            municipio = row['D_mnpio']
            estado = row['d_estado']
            clave_municipio = row['c_mnpio']
            municipios.append(
                {"municipio": municipio, "estado": estado, "clave_municipio": clave_municipio})

    return list(unique_everseen(municipios))


def get_asentamientos_excel():
    asentamientos = []

    for key in dataframes:
        if key == 'Nota':
            continue

        dt = dataframes[key]

        for _, row in dt.iterrows():
            codigo_postal = row['d_codigo']
            asentamiento = row['d_asenta']
            tipo_asentamiento = row['d_tipo_asenta']
            c_tipo_asenta = row['c_tipo_asenta']
            ciudad = row['d_ciudad']
            clave_ciudad = row['c_cve_ciudad']
            id_asentamiento = row['id_asenta_cpcons']
            descripcion_zona = row['d_zona']
            estado = row['d_estado']
            municipio = row['D_mnpio']
            clave_municipio = row['c_mnpio']

            asentamientos.append({
                "codigo_postal": codigo_postal,
                "nombre_asentamiento": asentamiento,
                "tipo_asentamiento": tipo_asentamiento,
                "clave_tipo_asentamiento": c_tipo_asenta,
                "identificador_asentamiento": id_asentamiento,
                "descripcion_zona": descripcion_zona,
                "estado": estado,
                "municipio": municipio,
                "clave_municipio": clave_municipio,
                "ciudad": "" if type(ciudad) == float and isnan(ciudad) else ciudad,
                "clave_ciudad": "" if type(clave_ciudad) == float and isnan(clave_ciudad) else clave_ciudad
            })

    return asentamientos
