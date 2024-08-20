# Starlink Analysis
![starlink](/assets/starlink.png?raw=true "Starlink")

This project orchestrates a holistic comparison and assessment of the reliability and performance attributes intrinsic to Wi-Fi, Ethernet, and Starlink networks within the domain of computer networks. It is comprised of three interconnected stages: meticulous data collection using traceroute and speedtest tools, comprehensive data analysis, and visualization of outcomes to foster an encompassing comparison. This solution seeks to provide clarity by gathering empirical data, conducting systematic data analysis, validate inferences through comparative evaluation, and provide actionable insights to improve network performance in future work.

## About this project
This project aimed to compare the reliability and throughput of Wi-Fi, Ethernet, and [Starlink](https://www.starlink.com/) networks using a multifaceted approach encompassing traceroute, ping, and speedtests. In addition to this, third-party gRPC scripts are used to gather and compare Starlink's results. The objective was to understand the performance variations among these networks and assess their suitability for diverse use cases. For clarification, Starlink is a global, satellite-powered, internet service engineered by [SpaceX](https://www.spacex.com/) whose metrics will be scrutinized in this evaluation against current common network solutions (e.g., Ethernet and Wi-Fi).

Through meticulous data collection using traceroute and speedtest tools over a 24-hour time period, followed by in-depth analysis leveraging Python libraries, the project successfully gathered and processed several network performance metrics. Additionally, the integration of gRPC scripts from an external repository provided insights into the networks' behavior under specific communication patterns.

## Installation
Install the "pip" package manager [pip](https://pip.pypa.io/en/stable/) here if needed.

```bash
pip install python3
pip install speedtest-cli
```

## gRPC Scripts
gRPC scripts used to gather Starlink data, as a workaround for Starlink's API being private, is found [here](https://github.com/sparky8512/starlink-grpc-tools).

Follow steps as needed to install dependencies and manipulate its scripts through its respective repo.

## Data Collection
```bash
./consistent-speedtest.sh         # Collects network speeds using speedtest-cli
python3 bash_collectByHour.py     # Collects traceroute & ping data for ethernet & wifi
python3 gRPC_collectByHour.py     # Collects traceroute & ping data for Starlink via gRPC script
python3 gRPC_collectStatistics.py # Collects statistics every hour via gRPC script
```

## Data Cleaning
```bash
python3 ethernet_ping.py # Cleans Ethernet ping data
python3 wifi_ping.py     # Cleans WiFi ping data
```

