import re
import sys
import matplotlib.pyplot as plt
from utils import *
# Define the colors

vio = "#8B008B"
midnight = "#C53E4F"
aqua = "#F46D43"
ocean = "#FDAE61"
wave = "#66C2A5"
wave2 = "#86C2A5"
stone = "#ABDDA4"
foam = "#3288BD"

set_paper_rcs_habib()

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: python script.py <filename>")
    sys.exit(1)

# Get the filename from command-line argument
filename = sys.argv[1]

# Dictionary to store extracted values for each PG
pg_rates = {}

# List to store the sumRate values
sumrate_values = []

# Read the text file line by line
with open(filename, 'r') as file:
    for line in file:
        # Process each line here
        # You can use regular expressions to extract the required information
        match_pg_rate = re.search(r'PG:(\d+) , rate: ([\d.]+) Gbps', line)
        match_sumrate = re.search(r'SumRate on endhost .* : ([\d.]+) Gbps', line)
        match_timer = re.search(r'Timer: (\d+) microsecond', line)  # Match Timer values
        
        
        if match_pg_rate:
            pg = int(match_pg_rate.group(1))
            rate = float(match_pg_rate.group(2))
            pg_rates.setdefault(pg, []).append(rate)
        
        if match_sumrate:
            sumrate = float(match_sumrate.group(1))
            sumrate_values.append(sumrate)

# Create a time array for x-axis
time_points = list(range(len(sumrate_values)))

# Plot the stacked area plot with specified colors
plt.stackplot(time_points, [pg_rates.get(pg, [0] * len(sumrate_values)) for pg in range(8)],
              colors=[vio, midnight, aqua, ocean, wave, wave2, stone, foam],
              labels=[f"PG {pg}" for pg in range(8)])
# plt.plot(time_points, sumrate_values, label="SumRate", color='tab:red', linestyle='--')

plt.xlabel("Time")
plt.ylabel("Rate (Gbps)")
# plt.title("Stacked Area Plot for Priority Groups and SumRate")
# Place the legend exactly on top of the plot
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.25), ncol=4)

plt.tight_layout()
# plt.show()

plt.savefig('%s.pdf'%filename.replace('.txt',''),format="pdf", bbox_inches='tight', pad_inches=0.05)
plt.close()