import pandas as pd
import plotly.express as px
import argparse
from datetime import datetime


def plot_call_volume(csv_file, start_date, end_date, write_html, write_json):
    """
    Plots the Simultaneously Calls over time within a specified date range.

    Parameters:
    - csv_file (str): Path to the CSV file containing call data.
    - start_date (str): The start date of the date range (format: YYYY-MM-DD).
    - end_date (str): The end date of the date range (format: YYYY-MM-DD).
    - write_html (str): Path to save the HTML file.
    - write_json (str): Path to save the JSON file.
    """
    # Load the CSV data
    data = pd.read_csv(csv_file, parse_dates=["start_time", "end_time"])

    # Filter the data based on the specified date range
    filtered_data = data[(data["start_time"] >= start_date) & (data["end_time"] <= end_date)]

    # Create a DataFrame to store filtered call start and end times
    calls = pd.DataFrame({"Start": filtered_data["start_time"], "End": filtered_data["end_time"]})

    # Create a list of unique timestamps for call start and end
    time_table = pd.DataFrame({"Time": pd.concat([calls["Start"], calls["End"]]).unique()}).sort_values("Time").reset_index(drop=True)

    # Use vectorized operations to count the number of simultaneously calls at each unique timestamp
    time_table["Volume"] = time_table["Time"].apply(lambda t: ((calls["Start"] <= t) & (calls["End"] > t)).sum())

    # Export the result to result.csv
    time_table.to_csv("result.csv", index=False)

    # Load the result.csv for visualization
    result_data = pd.read_csv("result.csv", parse_dates=["Time"])

    # Plot the volume over time using Plotly
    fig = px.line(result_data, x="Time", y="Volume", title="Simultaneously Calls Over Time", labels={"Time": "Time", "Volume": "Number of Simultaneously Calls"})
    
    # Save the chart to HTML and JSON if the file paths are provided
    if write_html:
        fig.write_html(write_html)
    if write_json:
        fig.write_json(write_json)
    
    # Display the chart
    fig.show()


if __name__ == "__main__":
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Plot Simultaneously Calls over a specified date range.")
    
    # Define the arguments
    parser.add_argument('--csv', type=str, default="cl_calls.csv", help='Path to the CSV file containing call data (default: cl_calls.csv)')
    parser.add_argument('--from', dest='start_date', type=str, default=f"{datetime.now().year}-01-01", help='The start date of the date range (format: YYYY-MM-DD, default: start of current year)')
    parser.add_argument('--to', dest='end_date', type=str, default=f"{datetime.now().year}-12-31", help='The end date of the date range (format: YYYY-MM-DD, default: end of current year)')
    parser.add_argument('--write_html', type=str, default="chart.html", help='File path to save the HTML output (default: chart.html)')
    parser.add_argument('--write_json', type=str, default="chart.json", help='File path to save the JSON output (default: chart.json)')

    # Parse the arguments
    args = parser.parse_args()
    
    # Call the function with the parsed arguments
    plot_call_volume(args.csv, args.start_date, args.end_date, args.write_html, args.write_json)
