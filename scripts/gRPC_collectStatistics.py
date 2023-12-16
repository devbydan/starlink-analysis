import os
import time

# Duration for which the script should run (24 hours)
end_time = time.time() + 60*60*24 #60*60*24 # seconds * minutes * hours -> 24 hours 60*60*24 -> 24 hrs

# Start hour counter
hour_counter = 1

while time.time() < end_time:
    # Open files to store the output of tracert and ping for the current hour
    with open(f'gRPC_stats-hour-{hour_counter}.txt', 'w') as f_starlinkScript, open(f'PING_hour-{hour_counter}.txt', 'w') as f_ping:
        # Time when the current hour ends
        hour_end_time = time.time() + 60*60

        while time.time() < hour_end_time:
            # Run tracert and write the output to tracert_hour_counter.txt
            starlinkScript = os.popen('python3 dish_grpc_text.py -t 60 -o 60 ping_drop').read()
            f_starlinkScript.write(starlinkScript)

            # Sleep for a minute before the next iteration
            time.sleep(60)

    # Increment the hour counter
    hour_counter += 1
