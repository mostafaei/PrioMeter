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

timer=[]
# Read the text file line by line
with open(filename, 'r') as file:
    for line in file:
        # Process each line here
        # You can use regular expressions to extract the required information
        match_pg_rate = re.search(r'PG:(\d+) , rate: ([\d.]+) Gbps', line)
        match_sumrate = re.search(r'.* SumRate on endhost .* : ([\d.]+) Gbps', line)
        match_timer = re.search(r'Time: (\d+)', line)  # Match Timer values
        
        
        if match_pg_rate:
            pg = int(match_pg_rate.group(1))
            rate = float(match_pg_rate.group(2))
            pg_rates.setdefault(pg, []).append(rate)
        if match_timer:
            time = int(match_timer.group(1)) - 2000000
            timer.append(time)
        if match_sumrate:
            sumrate = float(match_sumrate.group(1))
            sumrate_values.append(sumrate)

# Create a time array for x-axis
time_points = list(range(len(sumrate_values)))

fig, ax = plt.subplots()
# Plot the stacked area plot with specified colors
plt.stackplot(time_points, [pg_rates.get(pg, [0] * len(sumrate_values)) for pg in range(8)],
              colors=[vio, midnight, aqua, ocean, wave, wave2, stone, foam],
              labels=[f"PG {pg+1}" for pg in range(8)])
# plt.plot(time_points, sumrate_values, label="SumRate", color='tab:red', linestyle='--')


# Calculate the x-axis positions for 10 ticks
num_ticks = 8
x_positions = np.linspace(0, len(time_points) - 1, num_ticks, dtype=int)

# # Calculate the step size for the x-axis ticks
# num_ticks = 5  # Adjust the number of ticks as needed
step = len(timer) // (num_ticks - 1) if len(timer) > num_ticks else 1
# Generate x_ticks based on the step size
x_ticks = timer[::step]
# print(type(x_ticks))

plt.ylim(0,100)
ax.set_yticklabels(range(0,120,20))
x_tick_labels=[]
for i in range(len(x_ticks)):
    x_tick_labels.append(x_ticks[i])
# Set the custom x-tick positions and labels
ax.set_xticks(x_positions)
ax.set_xticklabels(x_tick_labels)

# Rotate the x-tick labels for better visibility (optional)
plt.xticks(rotation=30)




# # x_tick_labels = [str(x) for x in x_ticks]

# # Set custom x-axis ticks and labels
# # plt.xticks(x_ticks, x_tick_labels)

# plt.xticks(x_tick_labels)

plt.xlabel("Time (us)")
plt.ylabel("Rate (Gbps)")
# plt.title("Stacked Area Plot for Priority Groups and SumRate")
# Place the legend exactly on top of the plot
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.25), ncol=4)

plt.tight_layout()
# plt.show()

plt.savefig('%s.pdf'%filename.replace('.txt',''),format="pdf", bbox_inches='tight', pad_inches=0.05)
plt.close()