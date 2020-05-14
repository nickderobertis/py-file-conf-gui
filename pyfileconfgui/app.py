import dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash('pyfileconf', external_stylesheets=external_stylesheets)
server = app.server