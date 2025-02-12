#!/bin/bash

mkdir map_outputs

for zipfile in /data/Twitter\ dataset/geoTwitter20*.zip; do
    nohup python3 map.py --input_path "$zipfile" --output_folder map_outputs &
done
