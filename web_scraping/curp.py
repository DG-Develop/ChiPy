from time import sleep
import pandas as pd
from sel import scrap_curp


# Cargo una lista de dataframes por cada hoja en el archivo
dataframes = pd.read_excel(
    'static/excel/CurpContratos.xlsx',
    sheet_name=None,
    converters={'CURP': str}
)

data_process = {}
curp_invalid = {}

count_passed = 0
count_invalid = 0

for key in dataframes:
    i = 0    
    dt = dataframes[key]

    for _, row in dt.iterrows():
        if i > 100:
            break
        
        curp = row['CURP']
        
        sleep(55)
        
        # Validador
        try:
            data, not_passed = scrap_curp(curp)
            
            if len(data) > 0:
                count_passed += 1
            
            if len(not_passed) > 0:
                count_invalid += 1
            
            for clave, valor in data.items():
                if clave in data_process:
                    data_process[clave].append(valor)
                else:
                    data_process.update({clave: [valor]})
                
            for clave, valor in not_passed.items():
                
                if clave in curp_invalid:
                    curp_invalid[clave].append(valor)
                else:
                    curp_invalid.update({clave: [valor]})
                    
            print("Pasados: " + str(count_passed))
            print("Invalidos: " + str(count_invalid))
            
            i += 1
        except Exception:
            not_passed = {'curp': curp, 'observacion' : 'error selenium'}
            
            count_invalid += 1
            
            for clave, valor in not_passed.items():
                if clave in curp_invalid:
                    curp_invalid[clave].append(valor)
                else:
                    curp_invalid.update({clave: [valor]})
                
            print("Pasados: " + str(count_passed))
            print("Invalidos: " + str(count_invalid))
            
            i += 1
            
            continue


if len(data_process) != 0:
    df = pd.DataFrame(data_process)

    writer = pd.ExcelWriter('static/excel/Curps Validadas RENAPO.xlsx', engine='xlsxwriter')

    df.to_excel(writer, sheet_name='Validados')

    writer.save()
    
if len(curp_invalid) != 0:
    # print(curp_invalid)
    df = pd.DataFrame(curp_invalid)

    writer = pd.ExcelWriter('static/excel/Curps Invalidos RENAPO.xlsx', engine='xlsxwriter')

    df.to_excel(writer, sheet_name='Invalidos')

    writer.save()