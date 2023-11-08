# Per Periority Data Rate Measurement in Data Plane

This repository contains the code used in PrioMeter (EuroP4 2023)
It is based on NS-3 version 3.17 and built on top of [HPCC-PINT](https://github.com/ProbabilisticINT/HPCC-PINT).

### Build
`bash build.sh`

### Experiment config
Please see `mix/config.txt` for example. 

`mix/config_doc.txt` is a explanation of the example (texts in {..} are explanations).

`mix/fat.txt` is the topology used in HPCC and HPCC-PINT papers for the evaluation, and for large-scale simulation, we use the same topology. However, other experiments have been carried out on a dumbbell topology.

### Run
The direct command to run is:
`./waf --run 'scratch/third mix/config.txt'`

To run PrioMeter with a 1000 ns threshold for the measurement window, please try:
`python run.py --cc PrioMeter --trace flow --bw 100 --topo topology --prioMeter_thr 1000`

