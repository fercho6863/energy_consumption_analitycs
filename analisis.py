
import os.path
import plotly.graph_objects as go
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime



# ADQUIRIR DATOS DE IMAGENES AUTOMÁTICAS
#
#
#

# ADECUAR, LIMPIAR DATOS

file = os.listdir("FOTOS")

dir = os.getcwd() + "\\FOTOS"
os.chdir(dir)

date_create_photo = {}
dict_datos = []
nombre_archivo = []
fecha_total = []
fecha_foto = []
hora_foto = []
diferencia_vlr_dias = []


value_KWh = [
        496398,
        496398,
        496398,
        496447,
        496505,
        496512,
        496525,
        496548,
        496576,
        496598,
        496625,
        496647,
        496670,
        496711,
        496731,
        496789,
        496828,
        496828,
        496835,
        496837,
        496837,
        496852,
        496854,
        476876,
        496919,
        496919,
        496946,
        496977,
        496977,
        497009,
        497026,
        497051,
        497071,
        497098,
        497174,
        497197,
        497200,
        497209,
        497237,
        497262,
        497289,
        497312,
        497345,
        497377,
        497393,
        497422,
        497427,
        497458,
        497461,
        497539,
        497543,
        497589,
        497593,
        497655,
        497657,
        497687,
        497705,
        497732,
        497766,
        497786,
        497801,
        497827,
        497845,
        497894,
        497911,
        497972,
        497973,
        498005,
        498009,
        498034,
        498052,
        498080,
        498105,
        498133,
        498149,
        498191,
        498195,
        498245,
        498249,
        498261,
        498345,
        498399,
        498424,
        498447,
        496709,
        496709,
]

for i in file:
    # open the image
    image = Image.open(i)
    
    # extracting the exif metadata
    exifdata = image.getexif()
    
    # looping through all the tags present in exifdata
    for tagid in exifdata:
        
        # getting the tag name instead of tag id
        tagname = TAGS.get(tagid, tagid)
    
        # passing the tagid to get its respective value
        value = exifdata.get(tagid)
        
        # printing the final result
        print(f"{tagname:25}: {value}")

        if tagname == "DateTime":
            date_create_photo[i] = value

for files in file:
    fecha = date_create_photo.get(files, "Fecha no encontrada")
    valor_KWh = value_KWh[file.index(files)]

    archivo_dict = {
        "nombre_archivo": files,
        "fecha":fecha,
        "value_KWs": valor_KWh
    }

    dict_datos.append(archivo_dict)


# IMPRIMIR Y MOSTRAR LOS VALORES POR ITEMS ESPECÍFICOS
for dato in dict_datos:
    nombre_archivo.append(dato['nombre_archivo'])
    fecha_total.append(dato['fecha'])


    # Hacer algo con los valores
    #print(f"Nombre de archivo: {nombre_archivo}")
    #print(f"Fecha: {fecha}")
    #print(f"Value_KWs: {value_KWs}")
    #print("----")


# SEPARAR HORA DE FECHA
for fecha_hora in fecha_total:
    partes = fecha_hora.split(' ')

    if len(partes) == 2:
        fecha = partes[0]
        hora = partes[1]

        fecha_foto.append(fecha)
        hora_foto.append(hora)


# ------------------------------------------------------------------------------------------------------------------------------------------------ #
# CALCULOS INTERMEDIOS PARA PRESENTACIÓN DE INFORMACIÓN
# ------------------------------------------------------------------------------------------------------------------------------------------------ #


for i in range(1,len(value_KWh)):
    diferencia = value_KWh[i] - value_KWh[i-1]
    diferencia_vlr_dias.append(diferencia)


# ------------------------------------------------------------------------------------------------------------------------------------------------ #
# GRAFICAR DATOS DE VARIABLES
# ------------------------------------------------------------------------------------------------------------------------------------------------ #

# Create figure
fig = go.Figure()

len(diferencia_vlr_dias)

fig.add_trace(go.Scatter(x=list(fecha_total), y=list(value_KWh)))
#fig.add_trace(
#    go.Histogram(x=list(fecha_total), y=list(value_KWh)))

# Set title
fig.update_layout(
    title_text="Time series with range slider and selectors"
)

# Add range slider
fig.update_layout(
    xaxis=dict(

        rangeselector=dict(
            buttons=list([
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)

fig.show()





