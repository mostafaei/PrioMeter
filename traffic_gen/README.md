# Traffic Generater
This directory consists of scripts to generate traffic for PrioMeter experiments.

## Usage

`python2 traffic_gen_euroP4.py -h` for help.

Example:
`python2 traffic_gen_euroP4.py -c WebSearch_distribution.txt -n 320 -l 0.3 -b 100G -p 8 -t 0.1` generates traffic according to the web search flow size distribution with 8 different priority groups, for 320 hosts, at 30% network load with 100Gbps host bandwidth for 0.1 seconds.

The generate traffic can be directly used by the simulation.

## Traffic format
The first line is the number of flows.

Each line after that is a flow: `<source host> <dest host> <priority group> <dest port number> <flow size (bytes)> <start time (seconds)>`
