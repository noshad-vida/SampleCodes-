import plotly
#import plotly.plotly as py
import plotly.graph_objs as go


fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0.1, 1.1, 1.2, 1.8, 2.3, 2.0, 1.7, 2.1, 1.8],
    name="Zone 1"       # this sets its legend entry
))

fig.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[3.2, 3.4, 3.8, 3.9, 2.9, 2.7, 2.5, 2.3, 2.4],
    name="Zone 2"       # this sets its legend entry
))

fig.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 0.21, 0.26, 0.9, 1.2, 1.8, 2.0, 1.8, 1.7],
    name="Zone 3"       # this sets its legend entry
))


#.layout.update()
fig.update_layout(
    #title=“Sample Title”,
    xaxis_title="<b>Time (min)</b>",
    yaxis_title="<b>Distance</b>",
    font=dict(
        
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    )
)

fig.write_image("fig1.png")
fig.show()
