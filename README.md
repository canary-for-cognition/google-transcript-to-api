# google-transcript-to-api

This repository contains the script that takes the output of the Google transcript API and converts it to the format used by the CANARY group.
## How to use this script
All you need as input is a directory containing the Google transcripts. The script will create a new directory in the current path called "csv_outputs/" and will export the CSV format there.

Example call: 
```python
python google_api_to_canary_csv.py {GOOGLE_TRANSCRIPT_DIRECTORY}
```
