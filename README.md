# Geo Data Processor

## About the project

Geo Data Processor is a Python application for processing and analyzing spatial location data stored in CSV files.

The application validates input data, checks coordinate ranges and removes duplicate locations. Valid records are converted into spatial geometries and stored in a GeoDataFrame using the EPSG:4326 coordinate reference system. The data is then transformed to EPSG:2180 to enable distance calculations in meters.

The user can select a reference location and specify a maximum distance. The application finds locations within the given range and exports the results to a GeoJSON file, which can be opened and analyzed in GIS software such as QGIS.

## Features

- Load location data from a CSV file
- Validate coordinate ranges and remove duplicate locations
- Convert location data into spatial geometries and store them in a GeoDataFrame using EPSG:4326
- Transform spatial data to EPSG:2180 for distance calculations in meters
- Find locations within a user-defined distance
- Export search results to a GeoJSON file

## Technologies

- **Python** - core application logic
- **GeoPandas** - spatial data processing and GeoDataFrame operations
- **Shapely** - creation and handling of point geometries
- **pytest** - automated testing
- **Git** - version control
- **CSV / csv.DictReader** - input data loading
- **pathlib** - file and directory path handling

## Project Structure

```text
geo_data_processor/
├── data/
│   ├── locations.csv
│   └── processed/          # Generated GeoJSON output files
├── tests/
│   ├── test_exporters.py
│   ├── test_loader.py
│   ├── test_processor.py
│   └── test_validators.py
├── exporters.py            # GeoJSON export
├── geometry.py             # Spatial geometry and GeoDataFrame creation
├── loader.py               # CSV data loading
├── main.py                 # Application entry point and workflow
├── processor.py            # Duplicate removal and spatial search
├── validators.py           # Input data validation
├── requirements.txt        # Python dependencies
├── .gitignore
└── README.md
```

## How It Works

1. The application loads location data from a CSV file.
2. Invalid records and duplicate locations are removed.
3. Valid location data is converted into Point geometries and stored in a GeoDataFrame using EPSG:4326.
4. The spatial data is transformed to EPSG:2180 to enable distance calculations in meters.
5. The user selects a reference location and specifies a maximum distance.
6. The application finds locations within the specified distance from the reference point.
7. The results are transformed back to EPSG:4326 and exported to a GeoJSON file.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/patrykpl96/geo_data_processor.git
cd geo_data_processor
```

2. Create a virtual environment:

```bash
python -m venv .venv
```

3. Activate the virtual environment:

macOS / Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python main.py
```

The application asks the user to enter a reference location and a maximum distance in meters. It then finds and displays all locations within the specified distance.

The search results are also exported to:

```text
data/processed/search_results.geojson
```

The generated GeoJSON file can be opened and inspected in GIS software such as QGIS.

## Tests

Run all automated tests using:

```bash
python -m pytest
```

The test suite covers input validation, CSV loading, duplicate removal, location lookup, distance-based filtering and GeoJSON export.

