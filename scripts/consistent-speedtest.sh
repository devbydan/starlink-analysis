#!/bin/bash

# File to store results
OUTPUT_FILE="Starlink_SpeedTest_Results.txt"

# Number of minutes to run the test
MINUTES=1440 #(since there are 1440 minutes in 24 hours)

# Interval between tests in seconds (60 seconds = 1 minute)
INTERVAL=60

for ((i=1; i<=MINUTES; i++))
do
    echo "Running speedtest for Minute $i..."
    # Run the speedtest and store the results in a variable
    result=$(speedtest --secure --json)
    # Check if the result is valid JSON
    if echo "$result" | jq empty > /dev/null 2>&1; then
        # If the result is valid JSON, parse it to extract the download and upload speeds in Mb/s, and the ping in milliseconds
        download=$(echo $result | jq '.download / 1000000')
        upload=$(echo $result | jq '.upload / 1000000')
        ping=$(echo $result | jq '.ping')
        # Append the results to the output file
        echo "Minute $i: $download Mb/s download, $upload Mb/s upload, $ping ms ping" >> $OUTPUT_FILE
    else
        # If the result is not valid JSON, print an error message
        echo "Minute $i: Error running speedtest" >> $OUTPUT_FILE
    fi
    echo "Speedtest complete. Waiting for next test..."
    # Wait for the next test
    sleep $INTERVAL
done
echo "All tests complete."
