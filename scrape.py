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


def process_raw_data(feature):
    row = feature["properties"]
    yield row


def write_to_csv(data, location):
    # as these are what go into the csv, I really, really want
    # to make them more human-readable
    fieldnames = [
        "OBJECTID",
        "I_EVENTNUMBER",
        "LOCATION",
        "STREET",
        "CALL_ID",
        "CALL_DESC",
        "CALL_DATE",
        "I_MAPX",
        "I_MAPY",
        "I_STATUSID",
        "ILO_BEAT",
        "I_REPORTINGDISTRICT",
        "CALL_DATE_STR",
        "TIMEUPDATE",
        "POL_BEAT",
        "POL_DIST",
        "POL_SECT"
    ]

    with open(location, "w") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for row in data:
            row = next(row)
            writer.writerow({
                "OBJECTID": row["OBJECTID"],
                "I_EVENTNUMBER": row["I_EVENTNUMBER"],
                "LOCATION": row["LOCATION"],
                "STREET": row["STREET"],
                "CALL_ID": row["CALL_ID"],
                "CALL_DESC": row["CALL_DESC"],
                "CALL_DATE": row["CALL_DATE"],
                "I_MAPX": row["I_MAPX"],
                "I_MAPY": row["I_MAPY"],
                "I_STATUSID": row["I_STATUSID"],
                "ILO_BEAT": row["ILO_BEAT"],
                "I_REPORTINGDISTRICT": row["I_REPORTINGDISTRICT"],
                "CALL_DATE_STR": row["CALL_DATE_STR"],
                "TIMEUPDATE": row["TIMEUPDATE"],
                "POL_BEAT": row["POL_BEAT"],
                "POL_DIST": row["POL_DIST"],
                "POL_SECT": row["POL_SECT"]
            })


def run_the_jewels(target, location_raw, location_csv):
    raw = get_raw_data(target)
    # custom type in response isn't directly serializable;
    # also only want to hit the target endpoint once
    raw_as_list = list(raw)
    write_raw(raw_as_list, location_raw)

    processed = (process_raw_data(feature) for feature in raw_as_list)
    write_to_csv(processed, location_csv)


if __name__ == "__main__":
    stub_filename = "oakland_calls_for_service"
    filename_raw = f"raw/{stub_filename}-{date.today()}.json"
    filename_csv = f"csv/{stub_filename}-{date.today()}.csv"

    run_the_jewels(TARGET_LAYER, filename_raw, filename_csv)
