import plotly.express as px
from datetime import datetime
import pandas as pd

# Data: Dates, Locations, and Magnitudes
data = {
    "Date": [
        "2023-06", "2023-03", "2022-04", "2021-04", "2021-02",
        "2020-08", "2019-06", "2019-04", "2019-03", "2018-09",
        "2018-08", "2018-01", "2017-12", "2017-11", "2017-09",
        "2017-08", "2017-06", "2016-12", "2015-04", "2015-05"
    ],
    "Location": [
        "Afghanistan", "Hindu Kush", "Assam, India", "Assam", "Tajikistan",
        "Haryana", "Sichuan, China", "Arunachal Pradesh", "Jhelum",
        "Indonesia", "Lombok, Indonesia", "Balochistan", "Iran",
        "Iraq", "Mexico", "Sichuan, China", "Greece",
        "New Guinea", "Nepal", "Nepal"
    ],
    "Magnitude": [
        6.5, 6.8, 5.9, 6.4, 6.3,
        4.9, 6.0, 5.9, 5.8, 7.5,
        6.9, 6.2, 6.0, 7.3, 7.1,
        6.5, 6.3, 7.9, 7.8, 7.3
    ]
}


data["Date"] = [datetime.strptime(date, "%Y-%m") for date in data["Date"]]


df = pd.DataFrame(data)

# Create the Plotly Express figure
fig = px.line(df, x='Date', y='Magnitude', markers=True, title='Magnitudes of Notable Recent Earthquakes (with Locations)')


for i, row in df.iterrows():
    fig.add_annotation(
        x=row['Date'],
        y=row['Magnitude'],
        text=row['Location'],
        showarrow=True,
        arrowhead=1,
        ax=0,
        ay=-30 
    )


fig.update_layout(
    xaxis_title='Date',
    yaxis_title='Magnitude',
    xaxis=dict(
        tickformat='%Y-%m',
        tickangle=45,
        dtick="M6",  # Show dates every 6 months (adjust as needed)
    ),
    yaxis=dict(range=[4, 8]),
    template='plotly_white',
    height=600,
    width=1000,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font_color='black',
    font_family='verdana',
    font_size=10
)

# Save the figure as an HTML file
fig.write_html("graphs/plotly_earthquake_plot.html")
