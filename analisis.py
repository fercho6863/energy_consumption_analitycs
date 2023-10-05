
import os.path
from PIL import Image
from PIL.ExifTags import TAGS

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px



# ADQUIRIR DATOS DE IMAGENES AUTOMÁTICAS
#
#
#

# ADECUAR, LIMPIAR DATOS

file = os.listdir("FOTOS")

dir = os.getcwd() + "\\FOTOS"
os.chdir(dir)

# FILE 2 CORRESPONDE A CARPETA FOTOS
# dir = os.getcwd() + "\\" + file[2]
# file[2]

date_create_photo = {}
dict_datos = []

value_KWh = [496398,
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

image = Image.open(file[0])

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


print(dict_datos)

dict_datos[0]

# ------------------------------------------------------------------------------------------------------------------------------------------------ #
# GRAFICAR DATOS DE VARIABLES
# ------------------------------------------------------------------------------------------------------------------------------------------------ #

app = dash.Dash(__name__)



# Diseño de la aplicación
app.layout = html.Div([
    html.H1('KWs vs Fecha'),
    
    # Filtro interactivo
    dcc.RangeSlider(
        id='filtro-fecha',
        min=0,
        max=len(dict_datos) - 1,
        step=1,
        marks={i: {'label': dict_datos[i]['fecha']} for i in range(len(dict_datos))},
        value=[0, len(dict_datos) - 1]
    ),
    
    # Gráfico interactivo
    dcc.Graph(id='grafico-kws-vs-fecha')
])

# Callback para actualizar el gráfico
@app.callback(
    Output('grafico-kws-vs-fecha', 'figure'),
    Input('filtro-fecha', 'value')
)
def actualizar_grafico(filtro_fecha):
    datos_filtrados = dict_datos[filtro_fecha[0]:filtro_fecha[1] + 1]
    fig = px.scatter(
        datos_filtrados,
        x='fecha',
        y='value_KWs',
        text='nombre_archivo',
        title='KW vs. Fecha con Nombre del Archivo'
    )

    fig.update_xaxes(title_text='Fecha')
    fig.update_yaxes(title_text='Valor de KWs')
    
    return fig




if __name__ == '__main__':
    app.run_server(debug=True)



