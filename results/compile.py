import re, sys
import matplotlib.pyplot as plt


# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: python compile.py <filename>")
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
        
        if match_pg_rate:
            pg = int(match_pg_rate.group(1))
            rate = float(match_pg_rate.group(2))
            pg_rates.setdefault(pg, []).append(rate)
        
        if match_sumrate:
            sumrate = float(match_sumrate.group(1))
            sumrate_values.append(sumrate)

# Print the extracted values for each PG
# for pg, rates in pg_rates.items():
#     print(f"PG {pg} Rates: {rates}")

# Print the sumRate values
# print(f"SumRate Values: {sumrate_values}")

# Plot the values of each PG and sumRate
# Plot the values of each PG and sumRate
for pg, rates in pg_rates.items():
    if pg == 4:
        plt.plot(rates, label=f"PG {pg}", linestyle='-', marker='o')
    elif pg == 6:
        plt.plot(rates, label=f"PG {pg}", linestyle='--', marker='s')
    else:
        plt.plot(rates, label=f"PG {pg}")
    
plt.plot(sumrate_values, label="SumRate", linestyle='-', marker='x')

plt.xlabel("Time")
plt.ylabel("Rate (Gbps)")
plt.title("Rate Variation for Priority Groups and SumRate")
plt.legend()
plt.show()