#!/usr/bin/env python3

# python imports
import csv
from datetime import date
import json

# third-party imports
from esridump.dumper import EsriDumper


TARGET_LAYER = "http://gismaps.oaklandca.gov/oaklandgis/rest/services/callforservice_2015_FC/FeatureServer/0"


def get_raw_data(target):
    response = EsriDumper(target)

    return response


def write_raw(data, location):
    with open(location, "w+") as f:
        json.dump(data, f, indent=4)


#  TODO: match the existing csv; all the data is there in the response just waiting for us 
# def process_raw_data(feature):
#     yield json.dumps(feature)


def write_to_csv(data, location):
    fieldnames = [
        "type",
        "geometry",
        "properties"
    ]

    with open(location, "w") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for row in data:
            writer.writerow({
                "type": row["type"],
                "geometry": row["geometry"],
                "properties": row["properties"]
            })


def run_the_jewels(target, location_raw, location_csv):
    raw = get_raw_data(target)
    # custom type in response isn't directly serializable;
    # also only want to hit the target endpoint once
    raw_as_list = list(raw)
    write_raw(raw_as_list, location_raw)

    # processed = (process_raw_data(feature) for feature in raw_as_list)
    write_to_csv(raw_as_list, location_csv)


if __name__ == "__main__":
    stub_filename = "oakland_calls_for_service"
    filename_raw = f"raw/{stub_filename}-{date.today()}"
    filename_csv = f"csv/{stub_filename}-{date.today()}"

    run_the_jewels(TARGET_LAYER, filename_raw, filename_csv)
