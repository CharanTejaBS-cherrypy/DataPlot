import plotly.express as px
from datetime import datetime
import pandas as pd

# Example Flood Data
flood_data = {
    "Date": [
        "2023-08", "2023-07", "2022-10", "2022-09", "2022-08",
        "2022-07", "2021-10", "2021-09", "2021-08", "2021-07",
        "2020-09", "2020-08", "2020-07", "2019-10", "2019-09",
        "2019-08", "2019-07", "2018-10", "2018-09", "2018-08"
    ],
    "Location": [
        "Kerala", "Assam", "Uttarakhand", "Kolkata", "Gujarat",
        "Mumbai", "Bengaluru", "Chennai, India", "Hyderabad", "Delhi",
        "Sri Lanka", "Nepal", "Bangladesh", "Pakistan", "Myanmar",
        "Thailand", "Cambodia", "Vietnam", "Laos", "Malaysia"
    ],
    "Flood_Intensity": [
        80, 75, 85, 70, 60,
        90, 65, 50, 55, 60,
        95, 80, 70, 85, 90,
        75, 80, 65, 70, 60
    ],
       "Annotation_Adjustment": [
        20, -20, -20, -20, 20,
        -20, 20, 20, 20, -20,
        -20, 20, 20, -20, -20,
        20, -20, 20, -20, 20
    ]
}

# Convert date strings to datetime objects
flood_data["Date"] = [datetime.strptime(date, "%Y-%m") for date in flood_data["Date"]]

# Create a DataFrame
df_flood = pd.DataFrame(flood_data)

# Create the Plotly Express figure
fig_flood = px.line(df_flood, x='Date', y='Flood_Intensity', markers=True, title='Flood Intensities Over Time (with Locations)')

# Add annotations for each location below the dots
for i, row in df_flood.iterrows():
    fig_flood.add_annotation(
        x=row['Date'],
        y=row['Flood_Intensity'],
        text=row['Location'],
        showarrow=True,
        arrowhead=1,
        ax=0,
        ay=row['Annotation_Adjustment'] 
    )

# Update layout for better readability
fig_flood.update_layout(
    title='Flood Intensities Over Time (with Locations)',
    xaxis_title='Date',
    yaxis_title='Flood Intensity',
    xaxis=dict(
        tickformat='%Y-%m',
        tickangle=45,
        dtick="M6"  # Display dates every 6 months
    ),
    yaxis=dict(range=[0, max(df_flood['Flood_Intensity']) + 10]),  # Adjust based on your data
    template='plotly_white',
    height=600,
    width=1000,
    font_size=10
)

# Save the figure as an HTML file
fig_flood.write_html("graphs/flood_intensity_plot.html")

# Alternatively, you can display the figure in a Jupyter notebook or web app
# fig_flood.show()
