#!/usr/bin/python3

from cProfile import label
from math import floor, log
import subprocess
import os, sys, time, datetime
import re, ast

import zipfile
import matplotlib as mpl
from matplotlib import style
from matplotlib.markers import MarkerStyle

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

from matplotlib.backends.backend_pdf import PdfPages

from champsim_run_commons import *

horizontal_line_color = "k"
horizontal_line_style = ":"

#https://stackoverflow.com/questions/579310/formatting-long-numbers-as-strings-in-python
def human_format(number):
	number = float('{:.3g}'.format(number))
	units = ['f', 'p', 'n', 'u', 'm', '', 'K', 'M', 'G', 'T', 'P', 'E']
	k = 1000.0
	magnitude = int(floor(log(abs(number), k)))
	# return '%.2f%s' % (number / k**magnitude, units[magnitude])
	return '%.0f%s' % (number / k**magnitude, units[units.index('') + magnitude])

def human_formatter(a, b):
	return human_format(a)

def geomean(data_list):
	r = 1
	for i in data_list:
		r *= i
	r = np.power(r, 1/len(data_list))
	return r

def amean(data_list):
	r = 0
	for i in data_list:
		r += i
	r = r / len(data_list)
	return r

def plot_grouped_bars(data, bin_labels, bar_labels):
	bar_width = 4 / (len(bin_labels) * len(bar_labels) + 10)
	if (bar_width > 0.1):
		bar_width = 0.1

	bar_len = len(data)
	bin_len = len(data[0])

	positions = [np.arange(bin_len)]
	for i in range(bar_len - 1):
		positions.append([x + bar_width for x in positions[i]])
	
	for i in range(bar_len):
		plt.bar(positions[i], data[i], color=graph_colors[i % len(graph_colors)], width=bar_width, label=bar_labels[i])

	plt.xticks([r + (bar_width * ((bar_len - 1) / 2)) for r in range(bin_len)], bin_labels)
	
	data_flat = [item for sublist in data for item in sublist]
	# https://stackoverflow.com/questions/30228069/how-to-display-the-value-of-the-bar-on-each-bar-with-pyplot-barh
	# for index,data in enumerate(data_flat):
	# 	plt.text(x=index , y =data+1 , s=f"{data}" , fontdict=dict(fontsize=5), va='center')

def plot_grouped_bars_to_pdf(pdf, title, data, bin_labels, bar_labels):
	plt.yscale('linear')
	fig = plt.gcf()
	fig.set_size_inches(19.20, 10.80)
	fig.set_dpi(100)

	plot_grouped_bars(data, bin_labels, bar_labels)
	plt.title(title)
	plt.legend()
	pdf.savefig()
	plt.clf()
	plt.cla()
	plt.close()

def plot_bars_to_pdf(pdf, title, data, bar_labels):
	plt.yscale('log')
	fig = plt.gcf()
	fig.set_size_inches(38.40, 10.80)
	fig.set_dpi(100)

	p = plt.subplot(1,1,1)
	p.set_axisbelow(True)
	p.bar([x[10:] if "challenge_" in x else x for x in tests_to_run], AvgTimeDiffSameSet, log=True)
	p.grid(axis='y')

	plt.title(title)
	pdf.savefig()
	plt.clf()
	plt.cla()
	plt.close()

def plot_linear_graphs(data, text, axis=[], order=False, title="", grid=False):
	plt.yscale('linear')
	fig = plt.gcf()
	fig.set_size_inches(19.20, 10.80)
	fig.set_dpi(100)

	# Ordering the points
	for i in range(len(data)):
		d = zip(*data[i])
		d = [[a for a in b] for b in d]

		if(order):
			ord = np.argsort(d[0])
			x_d = np.array(d[0])[ord]
			y_d = np.array(d[1])[ord]
			d = [x_d, y_d]

		plt.plot(*d, label=text[i])

	if axis:
		plt.axis(axis)
	if title:
		plt.title(title)

	if grid:
		# plt.rcParams['axes.axisbelow'] = True
		plt.rc('axes', axisbelow=True)
		plt.grid()
	plt.legend()
	pdf.savefig()
	plt.clf()
	plt.cla()
	plt.close()

def plot_linear_graphs_subplot(sp_rows, sp_cols, sp_idx, data, text, axis=[None, None, None, None], order=False, title="", grid=False, x_axis_logarithmic=False, x_label=None, y_label=None, special_legend=False, add_zero_points=False, figure_size=0, plot_horizontal_line=False, hline_val=0):
	fig = plt.gcf()

	plt.rc("font", size=14)

	if (figure_size == 0):
		fig.set_size_inches(19.20, 10.80)
	elif (figure_size == 1):
		fig.set_size_inches(76.80, 10.80)
	elif (figure_size == 2):
		fig.set_size_inches(19.20, 5.40)
	fig.set_dpi(100)

	p = plt.subplot(sp_rows, sp_cols, sp_idx)

	p.set_yscale('linear')
	if (x_axis_logarithmic):
		p.set_xscale('log')
		p.xaxis.set_major_formatter(mticker.FuncFormatter(human_formatter))
	else:
		p.set_xscale('linear')

	pleg=[]

	# Ordering the points
	for i in range(len(data)):
		d = zip(*data[i])
		d = [[a for a in b] for b in d]

		if(order):
			ord = np.argsort(d[0])
			x_d = np.array(d[0])[ord]
			y_d = np.array(d[1])[ord]
			d = [x_d, y_d]

		p.plot(*d, label=text[i], color=subplot_colors[i % len(subplot_colors)], linestyle=subplot_styles[i % len(subplot_styles)])

		# pleg_t, = p.plot(*d, label=text[i], color=subplot_colors[i % len(subplot_colors)], linestyle=subplot_styles[i % len(subplot_styles)])
		# pleg.append(pleg_t)

		if (add_zero_points):
			for j in range(len(data[i])):
				if (data[i][j][0] == 0):
					p.plot(x_axis_zero_point_data, data[i][j][1], color=subplot_colors[i % len(subplot_colors)], marker='o')


	if axis:
		if axis[0] != None:
			p.axis(xmin=axis[0])
		if axis[1] != None:
			p.axis(xmax=axis[1])
		if axis[2] != None:
			p.axis(ymin=axis[2])
		if axis[3] != None:
			p.axis(ymax=axis[3])

	if title:
		p.set_title(title)

	if grid:
		# plt.rcParams['axes.axisbelow'] = True
		# p.rc('axes', axisbelow=True)
		p.grid()

	if x_label:
		p.set_xlabel(x_label)

	if ((not special_legend) or (sp_idx == 1)) and y_label:
		p.set_ylabel(y_label)

	if (not special_legend) or (sp_idx == np.ceil((sp_cols) / 2)):
		#, mode = "expand"
		p.legend(fontsize=10)
		# fig.legend(handles = pleg, ncol = len(data), bbox_to_anchor=(1.04,1))

	if (plot_horizontal_line):
		plt.axhline(y = hline_val, color = horizontal_line_color, linestyle = horizontal_line_style)

def plot_test_group(data, axis, x_label, y_label, add_zero_points, svg_name="", subtract_zero_point=False, divide_zero_point=False, tests_to_plot=None, figure_size=0, add_random_to_plot=False, random_val=[]):
	subplot_count = len(tests_to_run) if not tests_to_plot else len(tests_to_plot)
	current_subplot_index = 1

	for k in range(len(tests_to_run)):
		if (tests_to_plot):
			if not (tests_to_run[k] in tests_to_plot):
				continue
		av_age_data = []
		av_age_texts = []

		for j in replacement_policy_families:
			Average_Age_Perf = []
			original_family = ""

			if ("_SLOW" in j) or ("_FAST" in j):
				specific_family = True
				original_family = j[:-5]

			scale_by = 0

			for i in range(len(results[0])):
				if (j in configurations[i][0]) or (specific_family and (configurations[i][0] == original_family)):
					Av_Age = average_age(configurations[i])
					
					s = data[k][i]

					Average_Age_Perf.append((float(Av_Age), float(s)))

					if (Av_Age == 0):
						scale_by = s

			for i in range(len(Average_Age_Perf)):
				if (subtract_zero_point):
					Average_Age_Perf[i] = (Average_Age_Perf[i][0], (Average_Age_Perf[i][1] - scale_by))
				elif (divide_zero_point):
					Average_Age_Perf[i] = (Average_Age_Perf[i][0], (Average_Age_Perf[i][1] / scale_by - 1) * 100)

			av_age_data.append(Average_Age_Perf)
			if ("_SLOW" in j):
				av_age_texts.append(j[:-5] + " \"Late\"")
			elif ("_FAST" in j):
				av_age_texts.append(j[:-5] + " \"Early\"")
			else:
				av_age_texts.append(j)

		new_title = tests_to_run[k]
		if ("challenge_" in new_title):
			new_title = new_title[10:]
			new_title = new_title[0].capitalize() + new_title[1:]
		
		if ("GeoMean" == new_title):
			new_title = "Geometric Mean"
		if ("AMean" == new_title):
			new_title = "Arithmetic Mean"

		plot_linear_graphs_subplot(1, subplot_count, current_subplot_index, av_age_data, av_age_texts, 
								axis=axis, order=True, title=new_title, grid=True, 
								x_axis_logarithmic=True, x_label=x_label, y_label=y_label, 
								special_legend=True, add_zero_points=add_zero_points, 
								figure_size=figure_size, plot_horizontal_line=add_random_to_plot, 
								hline_val=random_val[k] if add_random_to_plot else 0)

		current_subplot_index += 1

	plt.tight_layout()
	pdf.savefig()
	if (svg_name):
		plt.savefig(svg_name, format="svg", bbox_inches='tight')
	plt.clf()
	plt.cla()
	plt.close()

def configuration_to_str(configuration):
	return str(configuration)

def print_help(file_path):
	print("Usage " + file_path + " [args]")
	print("\t-c/-u (compressed files/uncompressed files)")
	print("\t-e (execute included champsim run commons)")
	print("\t-f compressed_file_name.zip")

os.makedirs(results_data_dir, exist_ok=True)

pdf_file = results_data_dir + "Hit_ratio_results.pdf"

try:
	os.remove(pdf_file)
except OSError:
	pass

pdf = PdfPages(pdf_file)

enable_histograms = True

results = []
histograms = []

test_count = 0

use_compressed_file = True
compressed_file_name = ""
execute_included_commons_file = False
commons_file_name = "champsim_run_commons.py"

for i in range(len(sys.argv)):
	if (sys.argv[i] == "-h"):
		print_help(sys.argv[0])
		exit()
	elif (sys.argv[i] == "-c"):
		use_compressed_file = True
	elif (sys.argv[i] == "-u"):
		use_compressed_file = False
	elif (sys.argv[i] == "-e"):
		execute_included_commons_file = True
	elif (sys.argv[i] == "-f"):
		compressed_file_name = sys.argv[i + 1]
	else:
		pass

if use_compressed_file and (compressed_file_name == ""):
	compressed_file_names = os.listdir(compressed_results_dir)

	max_timestamp = -1
	for name in compressed_file_names:
		try:
			timestamp = re.findall(r"results(.*).zip", name)
		except:
			continue

		if len(timestamp) > 0:
			if int(timestamp[0]) > max_timestamp:
				max_timestamp = int(timestamp[0])

	if max_timestamp > -1:
		compressed_file_name = compressed_results_dir + "/results" + str(max_timestamp) + ".zip"

if use_compressed_file:
	try:
		compressed_file = zipfile.ZipFile(compressed_file_name)
	except:
		use_compressed_file = False

if (use_compressed_file and execute_included_commons_file):
	commons_file = compressed_file.open(commons_file_name)
	commons_file_contents = commons_file.read().decode()
	exec(commons_file_contents)
	commons_file.close()

failed_test_indexes = []

skipped_or_dropped = 0

for t in tests_to_run:
	test_result = []
	test_histograms = []
	for i in configurations:
		total_scale_sum = 0
		config_result = []
		config_histograms = []
		test_weights = []
		for merged_files in test_files[tests.index(t)]:
			internal_result = []
			internal_histograms = []
			test_weights.append(merged_files[1])
			total_scale_sum += merged_files[1]
			result = ""

			if str(i[0]) not in replacement_algorithms:
				print("ERROR: unknown replacmeent algorithm " + str(i[0]))
				exit(1)

			if (use_compressed_file == False):
				results_file_name = individual_results_dir + "/" + \
									(merged_files[0].replace("/", "").replace(".", "") + "-" + str(i[0]) + "-" + str(i[1]) + "-" + str(i[2]) + "-" + str(i[3]) + "-" + str(i[4])) + \
									"-result.txt"

				results_file = open(results_file_name, "r")

				result = results_file.read()
			else:
				results_file_name = \
									(merged_files[0].replace("/", "").replace(".", "") + "-" + str(i[0]) + "-" + str(i[1]) + "-" + str(i[2]) + "-" + str(i[3]) + "-" + str(i[4])) + \
									"-result.txt"

				results_file = compressed_file.open(results_file_name)

				result = results_file.read().decode()

			results_file.close()

			print(str(test_count) + ":\t" + results_file_name)
			test_count+=1

			if not "ChampSim completed all CPUs" in result:
				failed_test_indexes.append(test_count - 1)
				continue

			out = re.findall(r"CPU 0 cumulative IPC: (.*) instructions: (.*) cycles: (.*)", result)
			total_ipc = np.double(out[0][0])				# internal_result[0]
			total_instructions = int(out[0][1])				# internal_result[1]
			total_cycles = int(out[0][2])					# internal_result[2]

			internal_result.append(total_ipc)
			internal_result.append(total_instructions)
			internal_result.append(total_cycles)

			out = re.findall(r"""LLC TOTAL     ACCESS: (.*)  HIT: (.*)  MISS: (.*)""", result)
			llc_total_access = int(out[0][0])				# internal_result[3]
			llc_total_hit = int(out[0][1])					# internal_result[4]
			llc_total_miss = int(out[0][2])					# internal_result[5]

			internal_result.append(llc_total_access)
			internal_result.append(llc_total_hit)
			internal_result.append(llc_total_miss)

			out = re.findall(r"""LLC LOAD      ACCESS: (.*)  HIT: (.*)  MISS: (.*)""", result)
			llc_load_access = int(out[0][0])				# internal_result[6]
			llc_load_hit = int(out[0][1])					# internal_result[7]
			llc_load_miss = int(out[0][2])					# internal_result[8]

			internal_result.append(llc_load_access)
			internal_result.append(llc_load_hit)
			internal_result.append(llc_load_miss)

			out = re.findall(r"""LLC RFO       ACCESS: (.*)  HIT: (.*)  MISS: (.*)""", result)
			llc_rfo_access = int(out[0][0])					# internal_result[9]
			llc_rfo_hit = int(out[0][1])					# internal_result[10]
			llc_rfo_miss = int(out[0][2])					# internal_result[11]

			internal_result.append(llc_rfo_access)
			internal_result.append(llc_rfo_hit)
			internal_result.append(llc_rfo_miss)

			out = re.findall(r"""LLC PREFETCH  ACCESS: (.*)  HIT: (.*)  MISS: (.*)""", result)
			llc_prefetch_access = int(out[0][0])			# internal_result[12]
			llc_prefetch_hit = int(out[0][1])				# internal_result[13]
			llc_prefetch_miss = int(out[0][2])				# internal_result[14]

			internal_result.append(llc_prefetch_access)
			internal_result.append(llc_prefetch_hit)
			internal_result.append(llc_prefetch_miss)

			out = re.findall(r"""LLC WRITEBACK ACCESS: (.*)  HIT: (.*)  MISS: (.*)""", result)
			llc_writeback_access = int(out[0][0])			# internal_result[15]
			llc_writeback_hit = int(out[0][1])				# internal_result[16]
			llc_writeback_miss = int(out[0][2])				# internal_result[17]

			internal_result.append(llc_writeback_access)
			internal_result.append(llc_writeback_hit)
			internal_result.append(llc_writeback_miss)

			out = re.findall(r"""LLC PREFETCH  REQUESTED: (.*)  ISSUED: (.*)  USEFUL: (.*)  USELESS: (.*)""", result)
			llc_prefetch_requested = int(out[0][0])			# internal_result[18]
			llc_prefetch_issued = int(out[0][1])			# internal_result[19]
			llc_prefetch_useful = int(out[0][2])			# internal_result[20]
			llc_prefetch_useless = int(out[0][3])			# internal_result[21]

			internal_result.append(llc_prefetch_requested)
			internal_result.append(llc_prefetch_issued)
			internal_result.append(llc_prefetch_useful)
			internal_result.append(llc_prefetch_useless)

			out = re.findall(r"""LLC AVERAGE MISS LATENCY: (.*) cycles""", result)
			llc_average_miss_latency = float(out[0])		# internal_result[22]

			out = re.findall(r"""LLC CYCLES SPENT WITH QUEUE FULL: (.*)""", result)
			llc_cycles_queue_full = int(out[0])		# internal_result[23]

			if skipped_or_dropped == 0:
				out = re.findall(r"""LLC CYCLES WITH OPERATIONS SKIPPED: (.*)""", result)
				if (len(out) == 0): 
					skipped_or_dropped = 1
				else:
					llc_cycles_with_ops_skipped = int(out[0])		# internal_result[24]

					out = re.findall(r"""LLC TOTAL OPERATIONS SKIPPED: (.*)""", result)
					llc_total_ops_skipped = int(out[0])		# internal_result[25]
			if skipped_or_dropped == 1:
				out = re.findall(r"""LLC CYCLES WITH OPERATIONS DROPPED: (.*)""", result)
				llc_cycles_with_ops_dropped = int(out[0])		# internal_result[24]

				out = re.findall(r"""LLC TOTAL OPERATIONS DROPPED: (.*)""", result)
				llc_total_ops_dropped = int(out[0])		# internal_result[25]

			internal_result.append(llc_average_miss_latency)

			config_result.append(internal_result)

		merged_config_result = []
		merged_config_histograms = []

		for test_weights_idx in range(len(test_weights)):
			test_weights[test_weights_idx] = test_weights[test_weights_idx] / total_scale_sum

		for conf_idx in range(len(config_result[0])):
			conf_acc_sum = 0
			for val_to_sum_idx, file_scale in zip(config_result, test_weights):
				conf_acc_sum += val_to_sum_idx[conf_idx] * file_scale

			merged_config_result.append(conf_acc_sum)

		test_result.append(merged_config_result)

	results.append(test_result)

if len(failed_test_indexes) > 0:
	print("Failed Tests: ", endl="")
	print(failed_test_indexes)
	exit(0)

if (use_compressed_file):
	compressed_file.close()

results_geomean = []

# Calculate GeoMean
for i in range(len(results[0])):
	results_average_per_test = []

	for j in range(len(results[0][0])):
		data_list = []
		for k in range(len(results)):
			data_list.append(results[k][i][j])

		mean = geomean(data_list)

		results_average_per_test.append(mean)

	results_geomean.append(results_average_per_test)

# Add the geomean to the list of tests to be plotted
results.append(results_geomean)
tests_to_run.append("GeoMean")

results_amean = []

# Calculate Amean
for i in range(len(results[0])):
	results_average_per_test = []

	for j in range(len(results[0][0])):
		data_list = []
		for k in range(len(results)):
			data_list.append(results[k][i][j])

		mean = amean(data_list)

		results_average_per_test.append(mean)

	results_amean.append(results_average_per_test)

# Add the amean to the list of tests to be plotted
results.append(results_amean)
tests_to_run.append("AMean")

# plot_labels = [configuration_to_str(conf_i) for conf_i in configurations]

# mpkis = [[(c[5] / c[1] * 1000) if c[1] != 0 else 0 for c in t] for t in results]
# mpkis = [list(i) for i in zip(*mpkis)]
# plot_grouped_bars_to_pdf(pdf, "MPKI Results", mpkis, tests_to_run, plot_labels)

# hit_ratios = [[(c[4] / c[3]) if c[3] != 0 else 0 for c in t] for t in results]
# hit_ratios = [list(i) for i in zip(*hit_ratios)]
# plot_grouped_bars_to_pdf(pdf, "Hit ratio Results", hit_ratios, tests_to_run, plot_labels)

# hit_ratios_load = [[(c[7] / c[6]) if c[6] != 0 else 0 for c in t] for t in results]
# hit_ratios_load = [list(i) for i in zip(*hit_ratios_load)]
# plot_grouped_bars_to_pdf(pdf, "Hit ratio for load Results", hit_ratios_load, tests_to_run, plot_labels)

# hit_ratios_rfo = [[(c[10] / c[9]) if c[9] != 0 else 0 for c in t] for t in results]
# hit_ratios_rfo = [list(i) for i in zip(*hit_ratios_rfo)]
# plot_grouped_bars_to_pdf(pdf, "Hit ratio for RFO Results", hit_ratios_rfo, tests_to_run, plot_labels)

# hit_ratios_writeback = [[(c[16] / c[15]) if c[15] != 0 else 0 for c in t] for t in results]
# hit_ratios_writeback = [list(i) for i in zip(*hit_ratios_writeback)]
# plot_grouped_bars_to_pdf(pdf, "Hit ratio for writeback Results", hit_ratios_writeback, tests_to_run, plot_labels)

# IPCs = [[c[0] for c in t] for t in results]
# IPCs = [list(i) for i in zip(*IPCs)]
# plot_grouped_bars_to_pdf(pdf, "IPC Results", IPCs, tests_to_run, plot_labels)

# IPCs_scaled = [[c[0] for c in t] for t in results]
# IPCs_scaled = [[(t[c]/t[-1])-1 for c in range(len(t))] for t in IPCs_scaled]
# IPCs_scaled = [list(i) for i in zip(*IPCs_scaled)]
# plot_grouped_bars_to_pdf(pdf, "Scaled IPC Results", IPCs_scaled, tests_to_run, plot_labels)

# CPIs = [[(c[2] / c[1]) if c[1] != 0 else 0 for c in t] for t in results]
# CPIs = [list(i) for i in zip(*CPIs)]
# plot_grouped_bars_to_pdf(pdf, "CPI Results", CPIs, tests_to_run, plot_labels)

# AvgMissLat = [[c[22] for c in t] for t in results]
# AvgMissLat = [list(i) for i in zip(*AvgMissLat)]
# plot_grouped_bars_to_pdf(pdf, "Average Miss Latency", AvgMissLat, tests_to_run, plot_labels)



bases = dict()

L1_to_fill = replacement_algorithms
L2_to_fill = [0, 1]
L3_to_fill = [4, 8, 16, 32]

plotted_results = dict()
for i in L1_to_fill:
	plotted_results[i] = dict()
	for j in L2_to_fill:
		plotted_results[i][j] = dict()
		for k in L3_to_fill:
			plotted_results[i][j][k] = dict()

for j in range(len(configurations)):
	if configurations[j][1] == 0:
		bases[configurations[j][0]] = j
	elif configurations[j][2] == 0:
		if configurations[j][3] == 4:
			plotted_results[configurations[j][0]][0][4][configurations[j][4]] = j
		elif configurations[j][3] == 8:
			plotted_results[configurations[j][0]][0][8][configurations[j][4]] = j
		elif configurations[j][3] == 16:
			plotted_results[configurations[j][0]][0][16][configurations[j][4]] = j
		elif configurations[j][3] == 32:
			plotted_results[configurations[j][0]][0][32][configurations[j][4]] = j
	else:
		if configurations[j][3] == 4:
			plotted_results[configurations[j][0]][1][4][configurations[j][4]] = j
		elif configurations[j][3] == 8:
			plotted_results[configurations[j][0]][1][8][configurations[j][4]] = j
		elif configurations[j][3] == 16:
			plotted_results[configurations[j][0]][1][16][configurations[j][4]] = j
		elif configurations[j][3] == 32:
			plotted_results[configurations[j][0]][1][32][configurations[j][4]] = j

policies_to_plot = replacement_algorithms
for my_test in range(len(tests_to_run)):
	for l in policies_to_plot:
		for j in plotted_results[l]:
			for k in plotted_results[l][j]:
				to_plot_x = []
				to_plot_y = []
				to_plot_x.append(0)
				# to_plot_y.append(results[my_test][bases["LRU"]][2])
				to_plot_y.append(0)
				for i in plotted_results[l][j][k]:
					to_plot_x.append(i)
					to_plot_y.append((results[my_test][plotted_results[l][j][k][i]][2] / results[my_test][bases[l]][2] - 1) * 100)

				plt.plot(to_plot_x, to_plot_y, label=f"{l} ql = {k} " + ("serial" if j == 1 else "parallel"))


		plt.yscale('linear')
		fig = plt.gcf()
		fig.set_size_inches(19.20, 10.80)
		fig.set_dpi(100)

		
		plt.axhline(y = (results[my_test][bases['RANDOM']][2] / results[my_test][bases[l]][2] - 1) * 100, color = horizontal_line_color, linestyle = horizontal_line_style)

		plt.grid()

		plt.title(tests_to_run[my_test])
		plt.xlabel("queue latency")
		plt.ylabel("cycles")

		plt.legend()
		pdf.savefig()
		plt.clf()
		plt.cla()
		plt.close()

pdf.close()
exit(0)

# Figure out the families of delayed replacement policies
replacement_policy_families = []

for i in range(len(configurations)):
	if ("_DEL" in configurations[i][0]):
		if not (configurations[i][0][:-4] in replacement_policy_families):
			replacement_policy_families.append(configurations[i][0][:-4])

for j in replacement_policy_families:
	av_age_data = []
	av_age_texts = []
	specific_family = False
	original_family = ""

	if ("_SLOW" in j) or ("_FAST" in j):
		specific_family = True
		original_family = j[:-5]

	for k in range(len(tests_to_run)):
		Average_Age_Perf = []

		for i in range(len(results[0])):
			if (j in configurations[i][0]) or (specific_family and (configurations[i][0] == original_family)):
				Av_Age = average_age(configurations[i])
				
				s = results[k][i][0]

				Average_Age_Perf.append((float(Av_Age), float(s)))

		av_age_data.append(Average_Age_Perf)
		av_age_texts.append("Performance vs Average Age for " + tests_to_run[k])

	plot_linear_graphs(av_age_data, av_age_texts, None, order=True, title="Performance vs Average Age for " + j, grid=True)

tests_to_plot_ipc = ["challenge_cactus", "challenge_sphinx", "challenge_astar", "challenge_gems", "challenge_tonto", "challenge_omnetpp", "GeoMean"]
tests_to_plot_mpki = ["challenge_cactus", "challenge_sphinx", "challenge_astar", "challenge_gems", "challenge_tonto", "challenge_omnetpp", "AMean"]

random_config_location = -1
for i in range(len(configurations)):
	if configurations[i][0] == "RANDOM":
		random_config_location = i

add_random_to_plot = random_config_location >= 0
IPCs_rand = [i[random_config_location][0] for i in results] if add_random_to_plot else []

IPCs = [[c[0] for c in t] for t in results]
plot_test_group(IPCs, axis=[1000, None, None, None], x_label="Average Age", y_label="IPC", add_zero_points=True, figure_size=1, add_random_to_plot=add_random_to_plot, random_val=IPCs_rand)
plot_test_group(IPCs, axis=[1000, None, -1, 2], x_label="Average Age", y_label="% IPC change over no delay", add_zero_points=False, divide_zero_point=True, figure_size=1)
plot_test_group(IPCs, axis=[1000, None, None, None], x_label="Average Age", y_label="IPC", add_zero_points=True, svg_name=results_data_dir + "IPC_abs.svg", tests_to_plot=tests_to_plot_ipc, figure_size=2, add_random_to_plot=add_random_to_plot, random_val=IPCs_rand)
plot_test_group(IPCs, axis=[1000, None, -1, 2], x_label="Average Age", y_label="% IPC change over no delay", add_zero_points=False, svg_name=results_data_dir + "IPC_rel.svg", divide_zero_point=True, tests_to_plot=tests_to_plot_ipc, figure_size=2)
mpkis = [[(c[5] / c[1] * 1000) if c[1] != 0 else 0 for c in t] for t in results]
plot_test_group(mpkis, axis=[1000, None, -2, 5], x_label="Average Age", y_label="Absolute MPKI change over no delay", add_zero_points=False, subtract_zero_point=True, figure_size=1)
plot_test_group(mpkis, axis=[1000, None, 0, 40], x_label="Average Age", y_label="MPKI", add_zero_points=True, figure_size=1)
plot_test_group(mpkis, axis=[1000, None, -2, 5], x_label="Average Age", y_label="Absolute MPKI change over no delay", add_zero_points=False, svg_name=results_data_dir + "mpki_rel.svg", subtract_zero_point=True, tests_to_plot=tests_to_plot_mpki, figure_size=2)
plot_test_group(mpkis, axis=[1000, None, 0, 40], x_label="Average Age", y_label="MPKI", add_zero_points=True, svg_name=results_data_dir + "mpki_abs.svg", tests_to_plot=tests_to_plot_mpki, figure_size=2)
mpkis = [[((c[5] - c[17]) / c[1] * 1000) if c[1] != 0 else 0 for c in t] for t in results]
plot_test_group(mpkis, axis=[1000, None, -2, 5], x_label="Average Age", y_label="Absolute MPKI change over no delay", add_zero_points=False, subtract_zero_point=True, figure_size=1)
plot_test_group(mpkis, axis=[1000, None, 0, 40], x_label="Average Age", y_label="MPKI", add_zero_points=True, figure_size=1)
plot_test_group(mpkis, axis=[1000, None, -2, 5], x_label="Average Age", y_label="Absolute MPKI change over no delay", add_zero_points=False, svg_name=results_data_dir + "mpki2_rel.svg", subtract_zero_point=True, tests_to_plot=tests_to_plot_mpki, figure_size=2)
plot_test_group(mpkis, axis=[1000, None, 0, 40], x_label="Average Age", y_label="MPKI", add_zero_points=True, svg_name=results_data_dir + "mpki2_abs.svg", tests_to_plot=tests_to_plot_mpki, figure_size=2)


pdf.close()
