import dash
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Hello, World!')
])

if __name__ == '__main__':
    # I change the debug to False otherwise too slow
    app.run_server(debug=False, port=8051)

