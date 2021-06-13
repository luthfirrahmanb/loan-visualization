import plotly.graph_objs as go
from data import dfTips

listGoFunc = {
    'bar': go.Bar,
    'violin': go.Violin,
    'box': go.Box
}

def getPlot(jenis, xCategory):
    return [
        listGoFunc[jenis](
            x=dfTips[xCategory],
            y=dfTips['property value'],
            text=dfTips['purpose'],
            opacity=0.7,
            name='property value',
            marker=dict(color='blue'),
            legendgroup = 'property value'
        ),
        listGoFunc[jenis](
            x=dfTips[xCategory],
            y=dfTips['payments'],
            text=dfTips['purpose'],
            opacity=0.7,
            name='payments',
            marker=dict(color='orange'),
            legendgroup = 'payments'
        )
    ]