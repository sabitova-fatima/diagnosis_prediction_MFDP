from dash import Dash, dcc, Output, Input
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
mytext = dcc.Markdown(children="")
myinput = dbc.Input(value="# Hello")

app.layout = dbc.Container([mytext, myinput])

# callbackk decorator
@app.callback(
    Output(mytext, component_property='children'),
    Input(myinput, component_property='value')
)

# callback function
def update_title(user_input):
    return(user_input)

if __name__=='__main__':
    app.run_server(port=8051)