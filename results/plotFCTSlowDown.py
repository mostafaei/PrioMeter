#!/usr/bin/python
import subprocess
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from matplotlib import ticker
from matplotlib.pyplot import cm 
import numpy as np
import pylab
import random, math
from math import exp,ceil,log
import sys
import os.path
from os import path
import numpy as np
from utils import *


#matplotlib.rcParams['ps.useafm'] = True
#matplotlib.rcParams['pdf.use14corefonts'] = True
#matplotlib.rcParams['text.usetex'] = True
# matplotlib.rcParams['pdf.fonttype'] = 42
# matplotlib.rcParams['ps.fonttype'] = 42

midnight = "#C53E4F"
aqua = "#F46D43"
ocean = "#FDAE61"

# fig, ax = plt.subplots()    
set_paper_rcs_habib2()
# ax.grid(color='black', ls = '--',dashes=(5, 15), lw = 0.2,alpha=1)
plt.grid(color='black', ls = '--',dashes=(5, 15), lw = 0.2,alpha=1)
# plt.gcf().subplots_adjust(bottom=0.15)

# Check if the correct number of arguments is provided
if len(sys.argv) != 4:
    print("Usage: python script.py <filename>")
    sys.exit(1)

minY=int(sys.argv[2])
maxY=int(sys.argv[3])
# Get the filename from command-line argument
filename = sys.argv[1]
wb_file = 'fct_fat_wb50_b100_PG8_P4thMeter.dat'
wb_file = filename


P4thMeter_50_wb = [float(line.split()[2]) for line in open(wb_file).readlines()[0:]]     # web search
P4thMeter_95_wb = [float(line.split()[3]) for line in open(wb_file).readlines()[0:]]     # web search
P4thMeter_99_wb = [float(line.split()[4]) for line in open(wb_file).readlines()[0:]]     # web search
# PINT_50_wb = [float(line.split()[5]) for line in open(wb_file).readlines()[0:]]     # web search
# PINT_95_wb = [float(line.split()[6]) for line in open(wb_file).readlines()[0:]]     # web search
# PINT_99_wb = [float(line.split()[7]) for line in open(wb_file).readlines()[0:]]     # web search
HPCC_50_wb = [float(line.split()[5]) for line in open(wb_file).readlines()[0:]]    # web search
HPCC_95_wb = [float(line.split()[6]) for line in open(wb_file).readlines()[0:]]    # web search
HPCC_99_wb = [float(line.split()[7]) for line in open(wb_file).readlines()[0:]]    # web search

wb_x_axis = [int(line.split()[1]) for line in open(wb_file).readlines()[0:]] # wb flow sizes



plt.plot(np.linspace(0, 10, num=20),P4thMeter_50_wb, color=midnight, linestyle='-', label='PrioMeter 50',linewidth=2.0)
# plt.plot(np.linspace(0, 10, num=20),PINT_50_wb, color='blue', linestyle=':', label='HPCC(PINT) 50',linewidth=2.0)
plt.plot(np.linspace(0, 10, num=20),HPCC_50_wb, color='tab:blue', linestyle='-', label='HPCC 50',linewidth=2.0)


# plt.plot(np.linspace(0, 10, num=20),P4thMeter_95_wb, color=aqua, linestyle='-', label='P4thMeter 95',linewidth=2.0)
# plt.plot(np.linspace(0, 10, num=20),PINT_95_wb, color='blue', linestyle=':', label='HPCC(PINT) 95',linewidth=2.0)
# plt.plot(np.linspace(0, 10, num=20),HPCC_95_wb, color='red', linestyle='-', label='HPCC(INT) 95',linewidth=2.0)

plt.plot(np.linspace(0, 10, num=20),P4thMeter_99_wb, color=ocean, linestyle='-', label='PrioMeter 99',linewidth=2.0)
# plt.plot(np.linspace(0, 10, num=20),PINT_99_wb, color=midnight, linestyle=':', label='HPCC(PINT) 99',linewidth=2.0)
plt.plot(np.linspace(0, 10, num=20),HPCC_99_wb, color=aqua, linestyle=':', label='HPCC(INT) 99',linewidth=2.0)

# plt.ylim([1,17])
# max_value=max(max(HPCC_99_wb),max(P4thMeter_99_wb))
# yticks = [round(max_value * i / 6) for i in range(7)]
# plt.yticks(np.arange(1,18,2.5))
# ax.set_xticks(range(1,11))
# ax.set_xticklabels([str(x) if x < 1000 else str(int(x/1000. + .5)) + 'K' if x < 1000.**2 else str(int(x/1000.**2 + .5)) + 'M' for x in wb_x_axis[1::2]])
plt.xticks(range(1, 11),
           [str(x) if x < 1000 else str(int(x/1000. + .5)) + 'K' if x < 1000.**2 else str(int(x/1000.**2 + .5)) + 'M' for x in wb_x_axis[1::2]], rotation=30)

tick_interval = (maxY - minY) / 5  # Adjust the division for the number of ticks you want


# Generate custom y-ticks
custom_y_ticks = np.arange(minY, maxY + tick_interval, tick_interval)
plt.yticks(custom_y_ticks)


plt.legend(loc='upper left',prop={'size':10},ncol=1)
plt.tick_params(axis='both', which='major')
plt.tick_params(axis='y', which='major')
plt.ylabel(r'Slowdown')    
plt.xlabel('Flow Size [Bytes]')
#plt.xlim([0, maxPkts])
plt.tight_layout()
plt.savefig(filename+'.pdf',format="pdf", bbox_inches='tight', pad_inches=0.05)
# plt.savefig('web_search_l50_PG8.png')

# plt.clf()
# fig, ax = plt.subplots(figsize=(10,7)) 
# fig, ax = plt.subplots() 
# ax.grid(color='black', ls = '--',dashes=(5, 15), lw = 0.2,alpha=1)
# # plt.gcf().subplots_adjust(bottom=0.15)

# plt.ylim([1,8])
# plt.plot(np.linspace(0, 10, num=20),P4thMeter_95_fb, color='teal', linestyle='-', label='P4thMeter 95',linewidth=4.0)

# plt.plot(np.linspace(0, 10, num=20),HPCC_95_fb, color='red', linestyle='-', label='HPCC(INT) 95',linewidth=4.0)
# plt.plot(np.linspace(0, 10, num=20),PINT_95_fb, color='blue', linestyle='-', label='HPCC(PINT) 95',linewidth=4.0)

# plt.plot(np.linspace(0, 10, num=20),P4thMeter_99_fb, color='teal', linestyle='-.', label='P4thMeter 99',linewidth=4.0)

# plt.plot(np.linspace(0, 10, num=20),HPCC_99_fb, color='red', linestyle='--', label='HPCC(INT) 99',linewidth=4.0)
# plt.plot(np.linspace(0, 10, num=20),PINT_99_fb, color='blue', linestyle=':', label='HPCC(PINT) 99',linewidth=4.0)

# #plt.xticks(np.arange(len(wb_x_axis)), wb_x_axis)
# #ax.set_xticks(np.linspace(wb_x_axis[0], wb_x_axis[-1], num=20))
# ax.set_xticks(range(1,11))
# ax.set_xticklabels([str(x) if x < 1000 else str(int(x/1000. + .5)) + 'K' if x < 1000.**2 else str(int(x/1000.**2 + .5)) + 'M' for x in fb_x_axis[1::2]])


# plt.legend(loc='upper left',prop={'size':16},ncol=2)
# plt.tick_params(axis='both', which='major', labelsize=20)
# plt.tick_params(axis='y', which='major', labelsize=20)
# plt.ylabel(r'Slowdown', fontsize=20)    
# plt.xlabel('Flow Size [Bytes]', fontsize=20)
# #plt.show()
# plt.tight_layout()
# plt.savefig('facebook_l30_95-99p.pdf')
# plt.savefig('facebook_l30_95-99p.png')
# exit()


