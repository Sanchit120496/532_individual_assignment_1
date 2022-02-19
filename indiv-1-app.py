from dash import Dash, html, dcc, Input, Output
import altair as alt
from vega_datasets import data


# Read in global data
gapminder = data.gapminder()

# Setup app and layout/frontend
app = Dash(__name__,  external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server

app.layout = html.Div([
    html.Iframe(
        id='scatter',
        style={'border-width': '0', 'width': '100%', 'height': '400px'}),
    dcc.Dropdown(
        id='xcol-widget',
        value='life_expect',  # REQUIRED to show the plot on the first page load
        options=[{'label': col, 'value': col} for col in gapminder.columns])])

# Set up callbacks/backend
@app.callback(
    Output('scatter', 'srcDoc'),
    Input('xcol-widget', 'value'))
def plot_altair(xcol):
    chart = alt.Chart(gapminder).mark_point().encode(
        x=xcol,
        y='fertility',
        tooltip='life_expect').interactive()
    return chart.to_html()

if __name__ == '__main__':
    app.run_server(debug=True)
