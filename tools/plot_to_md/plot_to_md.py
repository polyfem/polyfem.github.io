import meshplot

first = True
meshplot.website()

def mp_to_md(self):
    global first
    if first:
        first = False
        res = self.to_html(imports=True, html_frame=False)
    else:
        res = self.to_html(imports=False, html_frame=False)

    return res


get_ipython().display_formatter.formatters["text/html"].for_type(meshplot.Viewer, mp_to_md)
