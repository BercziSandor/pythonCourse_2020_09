# Altair

# https://altair-viz.github.io/index.html
# https://altair-viz.github.io/user_guide/interactions.html
# https://www.journaldev.com/47555/python-altair-tutorial
# https://github.com/altair-viz/vega_datasets

python.exe -m pip install install altair vega_datasets

#########################################################

python.exe -m pip install altair_viewer

import altair as alt

alt.renderers.enable('altair_viewer') # ezt csak egyszer kell lefuttatni

#########################################################

import altair as alt
from vega_datasets import data

print(data.list_datasets()) # kiíratjuk a demo adatcsomagok nevét

cars = data.cars.url
# cars = data.cars() # ez is jó

brush = alt.selection_interval()

chart = alt.Chart(cars).mark_point().encode(
    y='Horsepower:Q',
    color=alt.condition(brush, 'Origin:N', alt.value('lightgray'))
).properties(
    width=250,
    height=250
).add_selection(
    brush
)

chart = chart.encode(x='Acceleration:Q') | chart.encode(x='Miles_per_Gallon:Q')

#chart.show()
chart.save('example.html')

# A brush értékadó sort cseréljük le erre:

brush = alt.selection_interval(encodings=['x'])

# aztán erre:

brush = alt.selection_interval(encodings=['y'])

#########################################################
