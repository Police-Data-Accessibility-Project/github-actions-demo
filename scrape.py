#!/usr/bin/env python3

# python imports
import csv
from datetime import date
import json

# third-party imports
from esridump.dumper import EsriDumper


TARGET_LAYER = "http://gismaps.oaklandca.gov/oaklandgis/rest/services/callforservice_2015_FC/FeatureServer/0"


def get_raw_data():
    response = EsriDumper(TARGET_LAYER)

    return response


def write_raw(data):
    stub_filepath = "raw/oakland_calls_for_service"
    filepath = f"{stub_filepath}-{date.today()}"
    with open(filepath, "w+") as f:
        json.dump(data, f, indent=4)


#  TODO: match the existing csv; all the data is there in the response just waiting for us 
# def process_raw_data(feature):
#     yield json.dumps(feature)


def write_to_csv(data):
    fieldnames = [
        "type",
        "geometry",
        "properties"
    ]

    filename_stub = "csv/oakland_calls_for_service"
    filename = f"{filename_stub}-{date.today()}"

    with open(filename, "w") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for row in data:
            writer.writerow({
                "type": row["type"],
                "geometry": row["geometry"],
                "properties": row["properties"]
            })


def run_the_jewels():
    raw = get_raw_data()
    # custom type in response isn't directly serializable;
    # also only want to hit the target endpoint once
    raw_as_list = list(raw)
    write_raw(raw_as_list)

    # processed = (process_raw_data(feature) for feature in raw_as_list)
    write_to_csv(raw_as_list)
    