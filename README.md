# Indian Agriculture Dashboard
This project creates an interactive dashboard using Streamlit to explore Indian agriculture data. It allows users to visualize various aspects of crop production across different states.

## Features:
Data Selection: Users can choose a specific state and crop to focus on.
Summary: The dashboard displays a summary of the selected data, including the state, crop, and total number of records.
Visualizations:
Bar chart: Area under cultivation by district
Pie chart: Share of production by season
Line plot: Average yield over the years
Scatter plot: Yield vs. Production (Top 10 districts)
- Running the Project:
Prerequisites: Ensure you have Python (version 3.9 or later) and the following libraries installed:

. pandas
. streamlit
. seaborn
. matplotlib
You can install them using pip install pandas streamlit seaborn matplotlib.

Clone the repository: If you've obtained the code through a version control system like Git, clone the repository to your local machine.

Data: The dashboard expects a CSV file named India Agriculture Crop Production.csv containing relevant agriculture data. Make sure this file is in the same directory as your Python script.

Run the script: Execute the main Python script (e.g., main.py) using python main.py in your terminal. This will launch the Streamlit app in your web browser, typically at http://localhost:8501.

## Usage:
Use the dropdowns in the sidebar to select a state and a crop.
The summary and visualizations will update based on your selections.
Explore the different visualizations to gain insights into agriculture production patterns.