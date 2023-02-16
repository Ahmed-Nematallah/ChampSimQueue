#!/usr/bin/python3

import subprocess
import os, sys, time, datetime
import re, ast

from champsim_run_commons import *

script_header = """#!/bin/bash
#SBATCH -A p2017001
#SBATCH --time 16:00:0
#SBATCH --requeue"""
"""#SBATCH --error=/dev/nul"""
"""#SBATCH --output=/dev/nul"""

if not results_dir in os.listdir("/"):
	os.makedirs(results_dir, exist_ok=True)

try:
	for f in os.listdir(temp_script_dir):
		os.remove(os.path.join(temp_script_dir, f))
except OSError:
	pass
os.makedirs(temp_script_dir, exist_ok=True)

# try:
# 	for f in os.listdir(individual_results_dir):
# 		os.remove(os.path.join(individual_results_dir, f))
# except OSError:
# 	pass
os.makedirs(individual_results_dir, exist_ok=True)

script_count = 0

print_index = 0
script_limit = 6900

for t in tests_to_run:
	for i in configurations:
		for merged_files in test_files[tests.index(t)]:
			if str(i[0]) not in replacement_algorithms:
				print("ERROR: unknown replacment algorithm " + str(i[0]))
				exit(1)

			if ((print_index * script_limit) <= script_count <= ((print_index + 1) * script_limit)):
				current_script = open(temp_script_dir + "/script" + str(script_count) + ".sh", "w")

				current_script.write(script_header)

				current_script.write("\n\n")

				current_script.write(executables[replacement_algorithms.index(str(i[0]))][conf] + " " + 
										"-warmup_instructions" + " " + 
										str(warmup_inst) + " " + 
										"-simulation_instructions" + " " + 
										str(sim_inst) + " " + 
										"-queue_length" + " " + 
										str(i[3]) + " " + 
										"-queue_cycles" + " " + 
										str(i[4]) + " " + 
										("-implement_queue" if i[1] == 1 else "") + " " + 
										("-serial_queue" if i[2] == 1 else "") + " " + 
										"-traces" + " " + 
										merged_files[0] + " " + 
										" > " + individual_results_dir + "/" + 
										(merged_files[0].replace("/", "").replace(".", "") + "-" + str(i[0]) + "-" + str(i[1]) + "-" + str(i[2]) + "-" + str(i[3]) + "-" + str(i[4])) + 
										"-result.txt" + 
										"\n")

				current_script.close()

			script_count += 1
