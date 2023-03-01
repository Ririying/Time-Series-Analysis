import pandas as pd
from bs4 import BeautifulSoup
import plotly

df_coal_consumption = pd.read_csv('/Users/raezh1/Documents/Georgetown/ANLY560/website/Time Series/data/coal_consumption.csv', index_col=0)
df_coal_consumption2 = pd.read_csv('/Users/raezh1/Documents/Georgetown/ANLY560/website/Time Series/data/coal_consumption2.csv', index_col=0)

# Stack them together
df = pd.concat([df_coal_consumption, df_coal_consumption2], ignore_index=True)

# Get unique location values and stateDescription values
df['location'].unique()

df['stateDescription'].unique()

df_coal_consumption['sectorDescription'].unique()
# The location data has regions as well as states, so I need to filter out the states

states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida',
          'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine',
          'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska',
          'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio',
          'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas',
          'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

# Filter out 2000 data
df = df[df['period'] > 2000]

# Selecting rows based on states
df_us_total = df[df['location'] == 'US']
df = df[df['stateDescription'].isin(states)]
len(df['location'].unique())


# Adding consumption together by each state per year
df_total_consumption = df.groupby(['period', 'location'],  as_index=False)['consumption'].sum()
df_total_us = df_us_total.groupby(['period', 'location'],  as_index=False)['consumption'].sum()
# Try to create a visualization
# Change default layout
GLOBAL_LAYOUT = dict(
    font=dict(
        family='Palatino',
        size=12
    )
)

import plotly.express as px
import plotly.graph_objects as go


df_total_consumption['period'] = pd.to_datetime(df_total_consumption['period'], format='%Y').dt.year.astype(str)

df_total_consumption = df_total_consumption.sort_values("period") # Make sure you sort the time horizon column in ascending order because this column is in random order in the raw dataset

fig1 = px.choropleth(df_total_consumption,
                     locations='location',
                     locationmode="USA-states",
                     color='consumption',
                     color_continuous_scale="deep", # deep gray aggrnyl
                     scope="usa",
                     animation_frame='period',
                     labels={'consumption': 'Annual Consumption'})

# Add the state names to map
fig1.add_scattergeo(
    locations=df['location'],
    locationmode='USA-states',
    text=df['location'],
    mode='text'
)

fig1.update_layout(
    title_text='Annual Coal Consumption by State in Short Tons'
)
fig1.update_layout(GLOBAL_LAYOUT)
fig1.show(renderer="browser")

# Make a line chart
fig2 = px.line(df_total_consumption, x="period", y="consumption", color='location', template='simple_white')
fig2.update_layout(
    title_text='Annual Coal Consumption by State',
    xaxis_title="Year",
    yaxis_title="Coal Consumption in short tons",
    legend_title="Location",
)
fig2.update_traces(mode="markers+lines", hovertemplate=None)
fig2.update_layout(hovermode="x")
fig2.update_layout(GLOBAL_LAYOUT)
fig2.show(renderer="browser")

# Make a bar plot
fig3 = px.bar(df_total_consumption,
              x="period", y="consumption",
              color='location',
              template='simple_white',
              color_continuous_scale='deep')
fig3.add_trace(
    go.Scatter(x=df_total_us['period'],
               y=df_total_us['consumption'],
               mode="lines",
               line=go.scatter.Line(color="black", width=2.3),
               showlegend=True,
               name="US Total")
    )
fig3.update_layout(
    title_text='Annual Coal Consumption by State',
    xaxis_title="Year",
    yaxis_title="Coal Consumption in short tons",
    legend_title="Location",
)
fig3.update_layout(GLOBAL_LAYOUT)
fig3.show(renderer="browser")

# Make a facet wrap graph
fig4 = px.histogram(df_total_consumption,
                    template='simple_white',
                    x="period",
                    y="consumption",
                    facet_col='location',
                    facet_col_wrap=10,
                    color_discrete_sequence=['indianred'])
fig4.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))

# Update xaxis yaxis properties
for i in range(6):
    fig4.update_yaxes(title_text="Coal Consumption", row=i, col=1)

for i in range(11):
    fig4.update_xaxes(title_text="Year", row=1, col=i)

# Update title and height
fig4.update_layout(title_text="Annual Coal Consumption by State")
fig4.update_layout(GLOBAL_LAYOUT)
fig4.show(renderer="browser")

plotly.offline.plot(fig1, filename='/Users/raezh1/Documents/Georgetown/ANLY560/website/Time Series/project_images/coal_animated_map.html')
plotly.offline.plot(fig2, filename='/Users/raezh1/Documents/Georgetown/ANLY560/website/Time Series/project_images/coal_line_chart.html')
plotly.offline.plot(fig3, filename='/Users/raezh1/Documents/Georgetown/ANLY560/website/Time Series/project_images/coal_bar_chart.html')
plotly.offline.plot(fig4, filename='/Users/raezh1/Documents/Georgetown/ANLY560/website/Time Series/project_images/coal_facet_wrap.html')

df_total_us.to_csv('/Users/raezh1/Documents/Georgetown/ANLY560/website/Time Series/data/coal_us_total.csv', index=False)


