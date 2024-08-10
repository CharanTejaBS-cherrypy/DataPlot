import plotly.express as px
from datetime import datetime
import pandas as pd

# Example Hurricane Data
hurricane_data = {
    "Date": [
        "2023-10", "2023-09", "2022-05", "2022-04", "2021-11",
        "2021-09", "2020-12", "2020-11", "2020-10", "2019-11",
        "2019-09", "2018-09", "2018-05", "2017-10", "2017-08",
        "2016-12", "2016-10", "2015-11", "2015-10", "2014-11"
    ],
    "Location": [
        "Tamil Nadu", "Kerala", "Bangladesh", "Myanmar", "Sri Lanka",
        "Andaman ", "Maldives", "Sri Lanka", "West Bengal", "Myanmar",
        "Bangladesh", "Tamil Nadu", "Andaman ", "Sri Lanka", "Bangladesh",
        "Myanmar", "Thailand", "Kerala", "Sri Lanka", "Maldives"
    ],
    "Hurricane_Intensity": [
        120, 100, 110, 130, 140,
        115, 105, 120, 110, 125,
        130, 140, 115, 100, 110,
        120, 130, 140, 115, 120
    ],
    "Annotation_Adjustment": [
        -20, 20, 20, -20, -20,
        -20, 20, -20, -20, 20,
        -20, -20, -20, 20, -20,
        30, -25, -20, 15, 30
    ]
}

# Convert date strings to datetime objects
hurricane_data["Date"] = [datetime.strptime(date, "%Y-%m") for date in hurricane_data["Date"]]

# Create a DataFrame
df_hurricane = pd.DataFrame(hurricane_data)

# Create the Plotly Express figure
fig_hurricane = px.line(df_hurricane, x='Date', y='Hurricane_Intensity', markers=True, title='Hurricane Intensities Over Time ')

# Add annotations with custom ay values for each point
for i, row in df_hurricane.iterrows():
    fig_hurricane.add_annotation(
        x=row['Date'],
        y=row['Hurricane_Intensity'],
        text=row['Location'],
        showarrow=True,
        arrowhead=1,
        ax=0,
        ay=row['Annotation_Adjustment']  # Use different ay for each annotation
    )

# Update layout for better readability
fig_hurricane.update_layout(
    title='Hurricane Intensities Over Time (with Locations)',
    xaxis_title='Date',
    yaxis_title='Hurricane Intensity',
    xaxis=dict(
        tickformat='%Y-%m',
        tickangle=45,
        dtick="M6"  # Display dates every 6 months
    ),
    yaxis=dict(range=[0, max(df_hurricane['Hurricane_Intensity']) + 20]),  # Adjust based on your data
    template='plotly_white',
    height=600,
    width=1000,
    font_size=10
)

# Save the figure as an HTML file
fig_hurricane.write_html("graphs/hurricane_intensity_plot.html")

# Alternatively, you can display the figure in a Jupyter notebook or web app
# fig_hurricane.show()
