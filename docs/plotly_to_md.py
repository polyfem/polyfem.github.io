import meshplot


def mp_to_md(self):
    return ""
    # return self.to_html()

get_ipython().display_formatter.formatters["text/html"].for_type(meshplot.Viewer, mp_to_md)
