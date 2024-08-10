import pandas as pd
from datetime import datetime
import plotly.express as px

# Example Wildfire Data
wildfire_data = {
    "Date": [
        "2023-05", "2023-04", "2022-10", "2022-08", "2022-07",
        "2021-11", "2021-09", "2021-07", "2021-05", "2020-12",
        "2020-10", "2020-08", "2019-11", "2019-09", "2018-07",
        "2018-05", "2017-12", "2017-11", "2017-09", "2016-08"
    ],
    "Location": [
        "Maharashtra", "Gujarat", "Keral ", "Karnataka", "Uttarakhand",
        "Sikkim ", "Himachal Pradesh, ", "Rajasthan", "Madhya Pradesh", "Goa",
        "Puducherry", "Arunachal Pradesh", "Nepal", "Bangladesh", "Myanmar",
        "Bhutan", "China", "Pakistan", "Sri Lanka", "Thailand"
    ],
    "Area_Burned_Ha": [
        500, 450, 700, 600, 650,
        400, 300, 550, 700, 800,
        500, 450, 300, 350, 400,
        250, 600, 700, 500, 300
    ]
}

# Convert date strings to datetime objects
df_wildfire = pd.DataFrame(wildfire_data)
df_wildfire['Date'] = pd.to_datetime(df_wildfire['Date'], format="%Y-%m")

# Create the Plotly figure
fig_wildfire = px.scatter(
    df_wildfire,
    x='Date',
    y='Area_Burned_Ha',
    color='Location',
    size='Area_Burned_Ha',
    hover_name='Location',
    title='Wildfires in and Nearby India',
    labels={"Date": "Date", "Area_Burned_Ha": "Area Burned (Hectares)"},
    template='plotly_white'
)

# Annotate each point with its location
for i, row in df_wildfire.iterrows():
    fig_wildfire.add_annotation(
        x=row['Date'],
        y=row['Area_Burned_Ha'],
        text=row['Location'],
        showarrow=True,
        arrowhead=1,
        ax=0,
        ay=20
    )

# Update layout for readability
fig_wildfire.update_layout(
    title='Wildfires in and Nearby India (with Locations)',
    xaxis_title='Date',
    yaxis_title='Area Burned (Hectares)',
    xaxis=dict(
        tickformat='%Y-%m',  # Only show year and month
        tickangle=45,
        dtick="M6"  # Show dates every 6 months
    ),
    yaxis=dict(range=[0, 1000]),  # Adjust based on your data
    template='plotly_white',
    height=600,
    width=1000,
    font_size = 10
)

# Save the figure as an HTML file
fig_wildfire.write_html("graphs/wildfire_plot.html")

# Alternatively, you can directly display the figure
# fig_wildfire.show()
