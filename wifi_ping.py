import re

def parse_ping_output(output):
    sent_match = re.search(r'Packets: Sent = (\d+)', output)
    received_match = re.search(r'Received = (\d+)', output)
    lost_match = re.search(r'Lost = (\d+) \((\d+)% loss\)', output)
    min_match = re.findall(r'Minimum = (\d+)ms', output)
    max_match = re.findall(r'Maximum = (\d+)ms', output)
    avg_match = re.findall(r'Average = (\d+)ms', output)

    sent = int(sent_match.group(1))
    received = int(received_match.group(1))
    lost = int(lost_match.group(1))
    min_times = [int(time) for time in min_match]
    max_times = [int(time) for time in max_match]
    avg_times = [int(time) for time in avg_match]

    return {
        'Sent': sent,
        'Received': received,
        'Lost': lost,
        'MinTimes': min_times,
        'MaxTimes': max_times,
        'AvgTimes': avg_times
    }

output_file = 'wifi_ping_fixed_all_hours.txt'

with open(output_file, 'w') as out_file:
    for hour in range(1,25):
        file_name = f'ping_hour-{hour}.txt'
        out_file.write(f"Hour {hour}:\n")
        try:
            with open(file_name, 'r') as file:
                ping_output = file.read()

            iterations = ping_output.split('Ping statistics for ')[1:]

            total_sent = 0
            total_received = 0
            total_lost = 0
            all_min_times = []
            all_max_times = []
            all_avg_times = []

            for iteration in iterations:
                parsed_data = parse_ping_output(iteration)

                total_sent += parsed_data['Sent']
                total_received += parsed_data['Received']
                total_lost += parsed_data['Lost']
                all_min_times.extend(parsed_data['MinTimes'])
                all_max_times.extend(parsed_data['MaxTimes'])
                all_avg_times.extend(parsed_data['AvgTimes'])

            if total_sent > 0:  # Avoid division by zero
                avg_min = sum(all_min_times) / len(all_min_times)
                avg_max = sum(all_max_times) / len(all_max_times)
                avg_avg = sum(all_avg_times) / len(all_avg_times)

                out_file.write(f"Total Packets: Sent = {total_sent}, Received = {total_received}, Lost = {total_lost}\n")
                out_file.write(f"Average of Minimum RTT: {avg_min}ms, Maximum RTT: {avg_max}ms, Average RTT: {avg_avg}ms\n\n")
            else:
                out_file.write(f"No data found for Hour {hour}.\n\n")
        except FileNotFoundError:
            out_file.write(f"File {file_name} not found.\n\n")

print(f"Output written to {output_file}")
