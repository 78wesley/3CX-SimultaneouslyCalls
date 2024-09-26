# 3CX Simultaneously Calls Graph

This Python script visualizes call volume over a specified time range by processing a CSV file with call start and end times. It generates an interactive HTML chart and exports the data in JSON format.

## How to Run

Ensure you are using a Linux environment or a Linux-compatible shell.

### First Setup

1. **Create a virtual environment & required dependencies:**
    ```bash
    sh create_venv.sh
    ```
2. **Activate the virtual environment:**
    ```bash
    source .venv/bin/activate
    ```

## Usage

Run the script from the command line with optional arguments. If no arguments are provided, it defaults to using `cl_calls.csv` and processes data for the current year (from January 1st to December 31st).

 **To receive the `cl_calls.csv` download a backup of the 3CX server and search for the file.**

### Command Line Arguments

- `--csv`: Path to the CSV file containing call data (default: `cl_calls.csv`).
- `--from`: Start date for filtering the call data (format: `YYYY-MM-DD`, default: start of the current year).
- `--to`: End date for filtering the call data (format: `YYYY-MM-DD`, default: end of the current year).
- `--write_html`: Path to save the HTML chart (default: `chart.html`).
- `--write_json`: Path to save the JSON data (default: `chart.json`).

### CSV File Format

The CSV file should have the following structure:

- **start_time**: The start time of the call (format: `YYYY-MM-DD HH:MM:SS`).
- **end_time**: The end time of the call (format: `YYYY-MM-DD HH:MM:SS`).

### Example Commands

#### Basic Usage (Defaults)

To run the script with default settings (current year, `cl_calls.csv`):

```bash
python main.py
```

This will:
- Read from `cl_calls.csv`.
- Filter the data for the current year (January 1st to December 31st).
- Save the chart to `chart.html` and the data to `chart.json` in the current directory.

#### Custom Date Range and Output Files

To use a custom CSV file, date range, and output paths:

```bash
python main.py --csv "custom_calls.csv" --from "2024-08-01" --to "2024-12-31" --write_html "my_chart.html" --write_json "my_chart.json"
```

This will:
- Read from `custom_calls.csv`.
- Filter the data between August 1st, 2024, and December 31st, 2024.
- Save the chart to `my_chart.html` and the data to `my_chart.json`.

### Output Files

- **`chart.html`**: An interactive HTML file with a line graph visualizing the number of active calls over time.
- **`chart.json`**: A JSON file containing the data and chart configuration for further use.

## Example Workflow

1. **Prepare the CSV file**: Ensure the CSV (e.g., `cl_calls.csv`) has the necessary `start_time` and `end_time` columns.
2. **Run the script**: Specify the CSV file and desired date range.
3. **View the chart**: Open the generated `chart.html` in a web browser to interact with the visualized call volume or open the one time link that is given in the console.