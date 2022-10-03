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
    ciudades = set()

    for key in dataframes:
        if key == 'Nota':
            continue

        dt = dataframes[key]
        ciudades_dt = dt['d_ciudad'].unique()

        ciudades.update(ciudades_dt)

    return sorted(ciudades)


def get_municipios_excel():
    municipios = []

    for key in dataframes:
        if key == 'Nota':
            continue

        dt = dataframes[key]

        for _, row in dt.iterrows():
            municipio = row['D_mnpio']
            estado = row['d_estado']
            municipios.append({"municipio": municipio, "estado": estado})

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
            id_asentamiento = row['id_asenta_cpcons']
            descripcion_zona = row['d_zona']
            municipio = row['D_mnpio']
            ciudad = row['d_ciudad']

            asentamientos.append({
                "codigo_postal": codigo_postal,
                "nombre_asentamiento": asentamiento,
                "tipo_asentamiento": tipo_asentamiento,
                "clave_tipo_asentamiento": c_tipo_asenta,
                "identificador_asentamiento": id_asentamiento,
                "descripcion_zona": descripcion_zona,
                "municipio": municipio,
                "ciudad": ciudad
            })

    return asentamientos
