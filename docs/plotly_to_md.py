import plotly.offline as plotly
import plotly.graph_objs as go


def to_md(self):
    html = '<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>'
    html += "<div>"
    html += plotly.plot(self, output_type='div', include_plotlyjs=False, show_link=False)
    html += "</div>"

    return html


get_ipython().display_formatter.formatters["text/html"].for_type(go.Figure, to_md)
