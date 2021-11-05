import pandas as pd
import datetime
import dateutil.relativedelta
pd.set_option('display.max_columns', 1000)
pd.set_option('display.max_rows', 1000)
pd.set_option('display.width', 2000)

# df_julio = pd.read_csv("sla5_base_julio.csv")
#
# df_agosto = pd.read_csv("sla5_base_agosto.csv", sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
#
# #Seleccionar columnas que coinciden
# cols_iguales = set(df_julio.columns) & set(df_agosto.columns)
# df_final = pd.concat([df_julio.loc[:,sorted(list(cols_iguales))], df_agosto.loc[:,sorted(list(cols_iguales))]])
# list_cols_iguales = ["_".join(c.split()) for c in list(df_final.columns)]
# df_final.columns = list_cols_iguales
# df_final = df_final.loc[:,sorted(df_final.columns)]
# df_final = df_final.drop(["nombreCliente", "abogado", "MEDICIÓN_AVANCE_JULIO", "COD_JULIO"], axis=1)
# df_final.to_csv("datos_sla5.csv", index=False, header=True, encoding='utf-8')

#### LIMPIEZA DATOS SLA 4
cols_sla4 = [
    'fechaAnalisis'
    , 'identificacionCliente'
    , 'operacion'
    , 'tipoRequerimiento'
    , 'estadoRequerimiento'
    , 'DEMANDA'
    , 'DEMANDA SI/NO'
    , 'DEMANDA PRESENTADA A TIEMPO SI/NO'
    , 'CUMPLIMIENTO SLA'
    , 'KPI REPROCESO PURO'
]

#Julio 2021
df_sla4_202107 = pd.read_excel("SLAS - KPIS JULIO/FLUJO DE DOCUMENTOS/SLAs - KPIs TIEMPO DE DEMANDA.xlsx"
                               ,sheet_name="REPORTE_FLUJO_DOCUMENTO", header=1)

df_sla4_202107['fechaAnalisis'] = pd.to_datetime(df_sla4_202107['fechaAnalisis']
                                                 , infer_datetime_format=True
                                                 ,unit="s")

df_sla4_202107['identificacionCliente'] = df_sla4_202107['identificacionCliente'].astype(str).apply(lambda x: x.zfill(16))
df_sla4_202107 = df_sla4_202107.drop(5725,axis=0)
df_sla4_202107 = df_sla4_202107[df_sla4_202107["REC AB"]==1]
df_sla4_202107 = df_sla4_202107[cols_sla4]

# #Agosto 2021
df_sla4_202108 = pd.read_excel("SLAS - KPIS AGOSTO/FLUJO DE DOCUMENTOS/SLAs - KPIs TIEMPO DE DEMANDA.xlsx"
                                ,sheet_name="REPORTE_FLUJO_DOCUMENTO", header=1)
df_sla4_202108['fechaAnalisis'] = pd.to_datetime(df_sla4_202108['fechaAnalisis']
                                                 , infer_datetime_format=True
                                                 ,unit="s")
df_sla4_202108['identificacionCliente'] = df_sla4_202108['identificacionCliente'].astype(str).apply(lambda x: x.zfill(16))
df_sla4_202108['operacion'] = df_sla4_202108['operacion'].astype(str).apply(lambda x: x.zfill(16))
df_sla4_202108 = df_sla4_202108.dropna(subset=['fechaRecepcionAbogadoLegal'],axis=0)
df_sla4_202108["fechaAnalisis"] = df_sla4_202108["fechaAnalisis"].apply(lambda x: x-dateutil.relativedelta.relativedelta(months=1))
df_sla4_202108 = df_sla4_202108[cols_sla4]

# #Septiembre 2021
df_sla4_202109 = pd.read_excel("SLAS - KPIS SEPTIEMBRE/FLUJO DE DOCUMENTOS/SLAs - KPIs TIEMPO DE DEMANDA 202109.xlsx"
                                ,sheet_name="Reporte_OPERACION_FLUJO_DOCUMEN", header=0)
df_sla4_202109['fechaAnalisis'] = pd.to_datetime(df_sla4_202109['fechaAnalisis']
                                                 , infer_datetime_format=True
                                                 ,unit="s")
df_sla4_202109['identificacionCliente'] = df_sla4_202109['identificacionCliente'].astype(str).apply(lambda x: x.zfill(16))
df_sla4_202109['operacion'] = df_sla4_202109['operacion'].astype(str).apply(lambda x: x.zfill(16))
df_sla4_202109 = df_sla4_202109[df_sla4_202109["CANCELADOS"]=="NO"]
df_sla4_202109 = df_sla4_202109[df_sla4_202109['OP UNICA']== 0]
df_sla4_202109 = df_sla4_202109.dropna(subset=['fechaRecepcionAbogadoLegal'],axis=0)
df_sla4_202109 = df_sla4_202109[~df_sla4_202109["tipoRequerimiento"].isin(["PLAN PILOTO", "UGCE", "CORRECCION", "ACTUALIZACION"])]
df_sla4_202109["fechaAnalisis"] = df_sla4_202109["fechaAnalisis"].apply(lambda x: x-dateutil.relativedelta.relativedelta(months=1))

df_sla4_202109 = df_sla4_202109[cols_sla4]

df_final_sla4 = pd.concat([df_sla4_202107, df_sla4_202108, df_sla4_202109], axis=0)
df_final_sla4.to_csv("datos_sla4.csv", index=False, header=True, encoding='utf-8')


