#! /usr/bin/env python3

"""
Generate a set of map markers from CSV data.
"""

def csv_to_json(csv_file):
    """
    Read a CSV file into JSON for later processing.
    """
    pass

# is it better to create a Map class and use add/save as methods?

def add_marker_to_map(mapfile, marker):
    """
    Add a given marker to a map.
    """
    pass

def save_map(mapfile, outfile="map.kml", zipped=False):
    """
    Produce a KML file (KMZ if zipped) from the given map.
    """
    pass

def main():
    """
    Read an input CSV file into JSON, convert that into
    a list of markers and then save the file.
    """
    try:
        csv_file = ""
        json_points = csv_to_json(csv_file)
        for point in json_points:
            add_marker_to_map(mapfile, point)
        save_map(mapfile, zipped=False)
    except TypeError:
        print("This still does nothing, by the way.")

if __name__ == "__main__":
    main()
