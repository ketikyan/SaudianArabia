import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
import plotly
import plotly.graph_objs as go
import pandas as pd
import numpy as np

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]
app = dash.Dash(external_stylesheets = external_stylesheets)

app.layout = html.Div([
    html.Div([html.Br()], style={"margin": "20px"}),

    html.Div([html.Label("Saudian Arabia Hotels", style={"font-size": "38px", 'color': 'blue', 'text-align': 'center'})], className='ten columns'),
    html.Div([html.Br()], style={"margin": "60px"}),
    html.Div([
        html.Br(),
        html.Div([html.Label("Title", style={"font-size": "24px"})], className='one columns'),
        html.Div([dcc.Dropdown(id='social_media_dropdown_input',
                         options = [
                         {'label': 'Mr.', 'value': 'Mr.'},
                         {'label': 'Mrs', 'value': 'Mrs'},
                         {'label': 'Miss', 'value': 'Miss'},
                         {'label': 'Ms.', 'value': 'Ms.'}
                        ], value = 'Mr.')
                ], className='two columns'),
        html.Div([dcc.Input(type = "text", value = 'e.g. John', id='name_input')], className='four columns'),
        html.Button(id = 'submit', n_clicks = 0, children = 'Submit')
    ], className='row'),

    html.Div([html.Br()], style={"margin": "20px"}),
    html.Div(id='text_output', style={"font-size": "22px"}),
    html.Div([html.Br()], style={"margin": "40px"}),
    html.Div([
        html.Div([html.Label("Description:", style={"font-size": "22px"})], className='two columns'),
        html.Div([html.Label("It is about data of 1025 hotels in Saudi Arabian. So the data has 1025 rows and 21 features and (Name, City, Price, Star_Rating, Property_Demand, Property_id, Customers_Rating, Customers_Review, Type_of_room, reservations_Payment, Canelation, Max_persons, Bed_type, Tax, Review_title, Credit_card , Breakfst_included, Longitude_x, Latitude_y, Link.", style={"font-size": "12px"})], className='ten columns'),
    ], className='container'),

    html.Div([html.Br()], style={"margin": "40px"}),

    html.Label("Next two plots are showing missing values.", style={"font-size": "22px", "color": "black"}),
    html.Div([html.Br()], style={"margin": "20px"}),
    html.Div([
        html.Img(src="assets/assets/nulls1.png", width="650px", height="500px"),
        html.Div([html.Br()], style={"margin": "40px"}),
        html.Img(src="assets/assets/nulls2.png", width="650px", height="500px"),
    ],  className='row'),
    html.Div([html.Br()], style={"margin": "40px"}),
    html.Label("Correlation Matrix.", style={"font-size": "22px", "color": "black"}),
    html.Div([html.Br()], style={"margin": "10px"}),
    html.Div([
        html.Label("red: uncorrelated", style={"font-size": "16px", "color": "red"}),
        html.Div([html.Br()], style={"margin": "10px"}),
        html.Label("blue: correlated", style={"font-size": "16px", "color": "blue"}),
    ], className='row'),
    html.Br(),
    html.Img(src="assets/assets/corrMatrix.png", width="650px", height="500px"),
    html.Div([html.Br()], style={"margin": "20px"}),
    html.Label("We see that there is high dependency between 'Customers_Review'-'Customers_Rating', 'Review_title'-'Customers_Rating', 'Review_title'-'Customers_Review', which is expectable. Also 'Cancelation'-'reservations_Payment' high correlated.", style={"font-size": "18px", "color": "black"}),
    html.Div([html.Br()], style={"margin": "40px"}),
    html.Div([
        html.Label("Change Histogram here", style={"font-size": "22px", "color": "black"}),
        html.Div([dcc.Dropdown(id='feature_histogram_dropdown_input',
                         options = [
                         {'label': 'Customers Rating', 'value': 'Customers Rating'},
                         {'label': 'Star Rating', 'value': 'Star Rating'},
                         {'label': 'Property ID', 'value': 'Property ID'},
                         {'label': 'Longitude_x', 'value': 'Longitude_x'},
                         {'label': 'Latitude_y', 'value': 'Latitude_y'},
                        ], value = 'Customers Rating')
            ], className='two columns'),
    ], className='row'),

    html.Div([
        html.Img(id='image1', width="450px", height="500px"),
        html.Div([html.Br()], style={"margin": "40px"}),
    ], className='row'),
    html.Div([html.Br()], style={"margin": "40px"}),
    html.Div([
        html.Label("Frequency table for cities", style={"font-size": "16px", "color": "black"}),
        html.Img(src="assets/assets/cities.png", width="350px", height="500px"),
        html.Div([html.Br()], style={"margin": "20px"})
    ], className='row'),
    html.Div([html.Br()], style={"margin": "20px"}),
    html.Label("So the greatest amount of hotels is in city Riyadh.", style={"font-size": "16px", "color": "black"}),
    html.Div([html.Br()], style={"margin": "40px"}),
], className='container')


def get_text(t1, t2):
    return 'Hello ' + t2 + ' ' +t1 + '. Welcome to our page!'

@app.callback(
        Output(component_id='text_output', component_property='children'),
        Input(component_id='submit', component_property='n_clicks'),
        State(component_id='name_input', component_property='value'),
        State(component_id='social_media_dropdown_input', component_property='value')
)

def update_text_output(clicks, input_1, input_2):
    return get_text(input_1, input_2)

@app.callback(
    Output(component_id='image1', component_property='src'),
    Input(component_id='feature_histogram_dropdown_input', component_property='value')
)
def update_images(selected_image):
    if selected_image == 'Customers Rating':
        image1_src = "assets/assets/Customers_Rating.png"
    elif selected_image == 'Star Rating':
        image1_src = "assets/assets/Star_Rating.png"
    elif selected_image == 'Property ID':
        image1_src = "assets/assets/Property_id.png"
    elif selected_image == 'Longitude_x':
        image1_src = "assets/assets/Longitude_x.png"
    elif selected_image == 'Latitude_y':
        image1_src = "assets/assets/Latitude_y.png"
    else:
        image1_src = None

    return image1_src
if __name__ == '__main__':
    app.run_server(debug = True)