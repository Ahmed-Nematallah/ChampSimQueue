
graph_colors = ['#0000ff', '#00ff00', '#ff0000', 
                '#00ffff', '#ff00ff', '#ffff00', 
				'#000000', '#00007f', '#007f00', 
				'#7f0000', '#007f7f', '#7f007f', 
				'#7f7f00', '#7f7fff', '#7fff7f', 
				'#ff7f7f', '#ffff7f', '#ff7fff', 
				'#7fffff', '#00003f', '#003f00', 
				'#3f0000', '#003f3f', '#3f003f', 
				'#3f3f00', '#3f3fff', '#3fff3f', 
				'#ff3f3f', '#ffff3f', '#ff3fff', 
				'#3fffff', '#3f37ff', '#37ff3f', 
				'#7f3f3f', '#7f7f3f', '#7f37ff', 
				'#37f7ff']

subplot_colors = ['#ff0000', '#ff0000', '#0000ff', '#0000ff', '#00ff00', '#7f4f00']

subplot_styles = ['-', '--', '-', '--', '-', '-']

x_axis_zero_point_data = 1200

traces_dir = "../ChampSim/traces/"

results_dir = "results/"
individual_results_dir = results_dir + "individual_results/"
compressed_results_dir = results_dir + "compressed_results/"
results_data_dir = results_dir + "results_data/"
temp_script_dir = results_dir + "temp_scripts/"

tests = ["perlbench", "gcc", "bwaves", "mcf", "cactus", "lbm", "omnetpp", "wrf", "xalancbmx", "x264", 
         "bzip_old", "graph_old", "libq_old", "mcf_old", "xololo_old", 
		 "1.5_mb_loop", "2.5_mb_loop", "7_mb_loop", "9_mb_loop", 
		 "challenge_cactus", "challenge_sphinx", "challenge_astar", "challenge_gems", 
		 "challenge_tonto", "challenge_omnetpp", "challenge_bwaves", "challenge_bzip", 
		 "challenge_gcc", "challenge_h.264ref", "challenge_lbm", "challenge_libquantum", 
		 "challenge_calculix", "challenge_gamess", "challenge_gobmk", "challenge_gromacs", 
		 "challenge_hmmer", "challenge_leslie3d", "challenge_mcf", "challenge_milc", 
		 "challenge_namd", "challenge_perlbench", "challenge_povray", "challenge_sjeng", 
		 "challenge_soplex", "challenge_wrf", "challenge_xalancbmk", "challenge_zeusmp"]
tests_to_run = tests
tests_to_run = ["challenge_cactus", "challenge_sphinx", "challenge_astar", "challenge_gems", 
				"challenge_tonto", "challenge_omnetpp", "challenge_bwaves", "challenge_bzip", 
				"challenge_gcc", "challenge_h.264ref", "challenge_lbm", "challenge_libquantum", 
				"challenge_calculix", "challenge_gamess", "challenge_gobmk", "challenge_gromacs", 
				"challenge_hmmer", "challenge_leslie3d", "challenge_mcf", "challenge_milc", 
				"challenge_namd", "challenge_perlbench", "challenge_povray", "challenge_sjeng", 
				"challenge_soplex", "challenge_wrf", "challenge_xalancbmk", "challenge_zeusmp"]
# tests_to_run = ["challenge_astar", "challenge_tonto", "challenge_omnetpp"]

test_files = [[(traces_dir + "dpc3_traces/600.perlbench_s-210B.champsimtrace.xz", 1)], 
              [(traces_dir + "dpc3_traces/602.gcc_s-734B.champsimtrace.xz", 1)], 
			  [(traces_dir + "dpc3_traces/603.bwaves_s-3699B.champsimtrace.xz", 1)], 
			  [(traces_dir + "dpc3_traces/605.mcf_s-665B.champsimtrace.xz", 1)], 
			  [(traces_dir + "dpc3_traces/607.cactuBSSN_s-2421B.champsimtrace.xz", 1)], 
			  [(traces_dir + "dpc3_traces/619.lbm_s-4268B.champsimtrace.xz", 1)], 
			  [(traces_dir + "dpc3_traces/620.omnetpp_s-874B.champsimtrace.xz", 1)], 
			  [(traces_dir + "dpc3_traces/621.wrf_s-575B.champsimtrace.xz", 1)], 
			  [(traces_dir + "dpc3_traces/623.xalancbmk_s-700B.champsimtrace.xz", 1)], 
			  [(traces_dir + "dpc3_traces/625.x264_s-18B.champsimtrace.xz", 1)], 
			  [(traces_dir + "dpc3_traces/bzip2_10M.trace.gz", 1)], 
			  [(traces_dir + "dpc3_traces/graph_analytics_10M.trace.gz", 1)], 
			  [(traces_dir + "dpc3_traces/libquantum_10M.trace.gz", 1)], 
			  [(traces_dir + "dpc3_traces/mcf_10M.trace.gz", 1)], 
			  [(traces_dir + "dpc3_traces/xalancbmk_10M.trace.gz", 1)], 
			  [(traces_dir + "my_traces/easy0.trace.xz", 1)], 
			  [(traces_dir + "my_traces/hard0.trace.xz", 1)], 
			  [(traces_dir + "my_traces/7_mb0.trace.xz", 0.75), (traces_dir + "my_traces/7_mb1.trace.xz", 0.25)], 
			  [(traces_dir + "my_traces/9_mb0.trace.xz", 0.333333), (traces_dir + "my_traces/9_mb1.trace.xz", 0.5), (traces_dir + "my_traces/9_mb3.trace.xz", 0.166667)], 
			  [(traces_dir + "crc2_traces/cactusADM_734B.trace.xz", 0.515756), (traces_dir + "crc2_traces/cactusADM_1039B.trace.xz", 0.0643087), (traces_dir + "crc2_traces/cactusADM_1495B.trace.xz", 0.353698)], 
			  [(traces_dir + "crc2_traces/sphinx3_2520B.trace.xz", 0.222623), (traces_dir + "crc2_traces/sphinx3_1339B.trace.xz", 0.175692), (traces_dir + "crc2_traces/sphinx3_883B.trace.xz", 0.135078)], 
			  [(traces_dir + "crc2_traces/astar_23B.trace.xz", 0.162319), (traces_dir + "crc2_traces/astar_163B.trace.xz", 0.452174), (traces_dir + "crc2_traces/astar_313B.trace.xz", 0.22029)], 
			  [(traces_dir + "crc2_traces/GemsFDTD_109B.trace.xz", 0.228906), (traces_dir + "crc2_traces/GemsFDTD_716B.trace.xz", 0.16792), (traces_dir + "crc2_traces/GemsFDTD_712B.trace.xz", 0.148705)], 
			  [(traces_dir + "crc2_traces/tonto_2834B.trace.xz", 0.269155), (traces_dir + "crc2_traces/tonto_2049B.trace.xz", 0.205746), (traces_dir + "crc2_traces/tonto_422B.trace.xz", 0.137715)], 
			  [(traces_dir + "crc2_traces/omnetpp_340B.trace.xz", 0.954463), (traces_dir + "crc2_traces/omnetpp_17B.trace.xz", 0.0309654), (traces_dir + "crc2_traces/omnetpp_4B.trace.xz", 0.010929)], 
			  [(traces_dir + "crc2_traces/bwaves_1861B.trace.xz", 0.337187), (traces_dir + "crc2_traces/bwaves_1609B.trace.xz", 0.262524), (traces_dir + "crc2_traces/bwaves_98B.trace.xz", 0.157996)], 
			  [(traces_dir + "crc2_traces/bzip2_183B.trace.xz", 0.334184), (traces_dir + "crc2_traces/bzip2_281B.trace.xz", 0.211735), (traces_dir + "crc2_traces/bzip2_259B.trace.xz", 0.19898)], 
			  [(traces_dir + "crc2_traces/gcc_13B.trace.xz", 0.323077), (traces_dir + "crc2_traces/gcc_39B.trace.xz", 0.153846), (traces_dir + "crc2_traces/gcc_56B.trace.xz", 0.138462)], 
			  [(traces_dir + "crc2_traces/h264ref_273B.trace.xz", 0.359551), (traces_dir + "crc2_traces/h264ref_351B.trace.xz", 0.21573), (traces_dir + "crc2_traces/h264ref_178B.trace.xz", 0.168539)], 
			  [(traces_dir + "crc2_traces/lbm_94B.trace.xz", 0.583797), (traces_dir + "crc2_traces/lbm_1004B.trace.xz", 0.375695), (traces_dir + "crc2_traces/lbm_564B.trace.xz", 0.0349484)], 
			  [(traces_dir + "crc2_traces/libquantum_1210B.trace.xz", 0.220129), (traces_dir + "crc2_traces/libquantum_1735B.trace.xz", 0.204521), (traces_dir + "crc2_traces/libquantum_964B.trace.xz", 0.203983)], 
			  [(traces_dir + "crc2_traces/calculix_2670B.trace.xz", 0.555355), (traces_dir + "crc2_traces/calculix_2655B.trace.xz", 0.207185), (traces_dir + "crc2_traces/calculix_3812B.trace.xz", 0.0964754)], 
			  [(traces_dir + "crc2_traces/gamess_316B.trace.xz", 0.31694), (traces_dir + "crc2_traces/gamess_196B.trace.xz", 0.224044), (traces_dir + "crc2_traces/gamess_247B.trace.xz", 0.166667)], 
			  [(traces_dir + "crc2_traces/gobmk_135B.trace.xz", 0.201835), (traces_dir + "crc2_traces/gobmk_60B.trace.xz", 0.201835), (traces_dir + "crc2_traces/gobmk_76B.trace.xz", 0.178899)], 
			  [(traces_dir + "crc2_traces/gromacs_1B.trace.xz", 0.75), (traces_dir + "crc2_traces/gromacs_0B.trace.xz", 0.25)], 
			  [(traces_dir + "crc2_traces/hmmer_7B.trace.xz", 0.317479), (traces_dir + "crc2_traces/hmmer_546B.trace.xz", 0.243757), (traces_dir + "crc2_traces/hmmer_397B.trace.xz", 0.198573)], 
			  [(traces_dir + "crc2_traces/leslie3d_1116B.trace.xz", 0.191894), (traces_dir + "crc2_traces/leslie3d_94B.trace.xz", 0.163772), (traces_dir + "crc2_traces/leslie3d_1186B.trace.xz", 0.142266)], 
			  [(traces_dir + "crc2_traces/mcf_46B.trace.xz", 0.329897), (traces_dir + "crc2_traces/mcf_250B.trace.xz", 0.175258), (traces_dir + "crc2_traces/mcf_158B.trace.xz", 0.154639)], 
			  [(traces_dir + "crc2_traces/milc_360B.trace.xz", 0.240631), (traces_dir + "crc2_traces/milc_744B.trace.xz", 0.206114), (traces_dir + "crc2_traces/milc_409B.trace.xz", 0.197239)], 
			  [(traces_dir + "crc2_traces/namd_400B.trace.xz", 0.181818), (traces_dir + "crc2_traces/namd_851B.trace.xz", 0.135698), (traces_dir + "crc2_traces/namd_1907B.trace.xz", 0.110421)], 
			  [(traces_dir + "crc2_traces/perlbench_53B.trace.xz", 0.536765), (traces_dir + "crc2_traces/perlbench_135B.trace.xz", 0.404412), (traces_dir + "crc2_traces/perlbench_105B.trace.xz", 0.0220588)], 
			  [(traces_dir + "crc2_traces/povray_437B.trace.xz", 0.29989), (traces_dir + "crc2_traces/povray_711B.trace.xz", 0.149945), (traces_dir + "crc2_traces/povray_250B.trace.xz", 0.140022)], 
			  [(traces_dir + "crc2_traces/sjeng_358B.trace.xz", 0.225079), (traces_dir + "crc2_traces/sjeng_1966B.trace.xz", 0.217411), (traces_dir + "crc2_traces/sjeng_1109B.trace.xz", 0.201173)], 
			  [(traces_dir + "crc2_traces/soplex_66B.trace.xz", 0.347561), (traces_dir + "crc2_traces/soplex_205B.trace.xz", 0.185976), (traces_dir + "crc2_traces/soplex_217B.trace.xz", 0.164634)], 
			  [(traces_dir + "crc2_traces/wrf_1212B.trace.xz", 0.35202), (traces_dir + "crc2_traces/wrf_1650B.trace.xz", 0.123232), (traces_dir + "crc2_traces/wrf_1228B.trace.xz", 0.122222)], 
			  [(traces_dir + "crc2_traces/xalancbmk_748B.trace.xz", 0.346578), (traces_dir + "crc2_traces/xalancbmk_768B.trace.xz", 0.250552), (traces_dir + "crc2_traces/xalancbmk_99B.trace.xz", 0.188742)], 
			  [(traces_dir + "crc2_traces/zeusmp_600B.trace.xz", 1), (traces_dir + "crc2_traces/zeusmp_300B.trace.xz", 1), (traces_dir + "crc2_traces/zeusmp_100B.trace.xz", 1)]]

conf = 0 # 0 for no prefetcher, 1 for prefetcher

warmup_inst = 1000000
sim_inst = 999000000
hb_inst = 1000000

executables = [
	("./bin/bimodal-no-no-no-no-lru_new-1core", "./bin/bimodal-next_line-next_line-next_line-next_line-lru_new-1core"), 
	("./bin/bimodal-no-no-no-no-mockingjay-1core", "./bin/bimodal-next_line-next_line-next_line-next_line-mockingjay-1core"),
	("./bin/bimodal-no-no-no-no-hawkeye-1core", "./bin/bimodal-next_line-next_line-next_line-next_line-hawkeye-1core"),
	("./bin/bimodal-no-no-no-no-drrip-1core", "./bin/bimodal-next_line-next_line-next_line-next_line-drrip-1core"),
	("./bin/bimodal-no-no-no-no-ship-1core", "./bin/bimodal-next_line-next_line-next_line-next_line-ship-1core"),
	("./bin/bimodal-no-no-no-no-perceptron-1core", "./bin/bimodal-next_line-next_line-next_line-next_line-perceptron-1core"),
	("./bin/bimodal-no-no-no-no-random_replacement-1core", "./bin/bimodal-next_line-next_line-next_line-next_line-random_replacement-1core"),
]

replacement_algorithms = ["LRU", "MOCKINGJAY", "HAWKEYE", "DRRIP", "SHIP", "PERCEPTRON", "RANDOM"]

# Replacement policy, implement queue, serial queue, queue length, queue cycles
configurations = [("LRU", 0, 0, 1, 1), 
                  ("LRU", 1, 0, 4, 8), ("LRU", 1, 0, 4, 16), ("LRU", 1, 0, 4, 32), ("LRU", 1, 0, 4, 64), ("LRU", 1, 0, 4, 128), 
                  ("LRU", 1, 0, 8, 8), ("LRU", 1, 0, 8, 16), ("LRU", 1, 0, 8, 32), ("LRU", 1, 0, 8, 64), ("LRU", 1, 0, 4, 128), 
                  ("LRU", 1, 0, 16, 8), ("LRU", 1, 0, 16, 16), ("LRU", 1, 0, 16, 32), ("LRU", 1, 0, 16, 64), ("LRU", 1, 0, 16, 128), 
                  ("LRU", 1, 0, 32, 8), ("LRU", 1, 0, 32, 16), ("LRU", 1, 0, 32, 32), ("LRU", 1, 0, 32, 64), ("LRU", 1, 0, 32, 128), 
                  ("LRU", 1, 1, 4, 8), ("LRU", 1, 1, 4, 16), ("LRU", 1, 1, 4, 32), ("LRU", 1, 1, 4, 64), ("LRU", 1, 1, 4, 128), 
                  ("LRU", 1, 1, 8, 8), ("LRU", 1, 1, 8, 16), ("LRU", 1, 1, 8, 32), ("LRU", 1, 1, 8, 64), ("LRU", 1, 1, 8, 128), 
                  ("LRU", 1, 1, 16, 8), ("LRU", 1, 1, 16, 16), ("LRU", 1, 1, 16, 32), ("LRU", 1, 1, 16, 64), ("LRU", 1, 1, 16, 128), 
                  ("LRU", 1, 1, 32, 8), ("LRU", 1, 1, 32, 16), ("LRU", 1, 1, 32, 32), ("LRU", 1, 1, 32, 64), ("LRU", 1, 1, 32, 128), 
                  ("MOCKINGJAY", 0, 0, 1, 1), 
                  ("MOCKINGJAY", 1, 0, 4, 8), ("MOCKINGJAY", 1, 0, 4, 16), ("MOCKINGJAY", 1, 0, 4, 32), ("MOCKINGJAY", 1, 0, 4, 64), ("MOCKINGJAY", 1, 0, 4, 128), 
                  ("MOCKINGJAY", 1, 0, 8, 8), ("MOCKINGJAY", 1, 0, 8, 16), ("MOCKINGJAY", 1, 0, 8, 32), ("MOCKINGJAY", 1, 0, 8, 64), ("MOCKINGJAY", 1, 0, 8, 128), 
                  ("MOCKINGJAY", 1, 0, 16, 8), ("MOCKINGJAY", 1, 0, 16, 16), ("MOCKINGJAY", 1, 0, 16, 32), ("MOCKINGJAY", 1, 0, 16, 64), ("MOCKINGJAY", 1, 0, 16, 128), 
                  ("MOCKINGJAY", 1, 0, 32, 8), ("MOCKINGJAY", 1, 0, 32, 16), ("MOCKINGJAY", 1, 0, 32, 32), ("MOCKINGJAY", 1, 0, 32, 64), ("MOCKINGJAY", 1, 0, 32, 128), 
                  ("MOCKINGJAY", 1, 1, 4, 8), ("MOCKINGJAY", 1, 1, 4, 16), ("MOCKINGJAY", 1, 1, 4, 32), ("MOCKINGJAY", 1, 1, 4, 64), ("MOCKINGJAY", 1, 1, 4, 128), 
                  ("MOCKINGJAY", 1, 1, 8, 8), ("MOCKINGJAY", 1, 1, 8, 16), ("MOCKINGJAY", 1, 1, 8, 32), ("MOCKINGJAY", 1, 1, 8, 64), ("MOCKINGJAY", 1, 1, 8, 128), 
                  ("MOCKINGJAY", 1, 1, 16, 8), ("MOCKINGJAY", 1, 1, 16, 16), ("MOCKINGJAY", 1, 1, 16, 32), ("MOCKINGJAY", 1, 1, 16, 64), ("MOCKINGJAY", 1, 1, 16, 128), 
                  ("MOCKINGJAY", 1, 1, 32, 8), ("MOCKINGJAY", 1, 1, 32, 16), ("MOCKINGJAY", 1, 1, 32, 32), ("MOCKINGJAY", 1, 1, 32, 64), ("MOCKINGJAY", 1, 1, 32, 128), 
				  ("HAWKEYE", 0, 0, 1, 1), 
                  ("HAWKEYE", 1, 0, 4, 8), ("HAWKEYE", 1, 0, 4, 16), ("HAWKEYE", 1, 0, 4, 32), ("HAWKEYE", 1, 0, 4, 64), ("HAWKEYE", 1, 0, 4, 128), 
                  ("HAWKEYE", 1, 0, 8, 8), ("HAWKEYE", 1, 0, 8, 16), ("HAWKEYE", 1, 0, 8, 32), ("HAWKEYE", 1, 0, 8, 64), ("HAWKEYE", 1, 0, 8, 128), 
                  ("HAWKEYE", 1, 0, 16, 8), ("HAWKEYE", 1, 0, 16, 16), ("HAWKEYE", 1, 0, 16, 32), ("HAWKEYE", 1, 0, 16, 64), ("HAWKEYE", 1, 0, 16, 128), 
                  ("HAWKEYE", 1, 0, 32, 8), ("HAWKEYE", 1, 0, 32, 16), ("HAWKEYE", 1, 0, 32, 32), ("HAWKEYE", 1, 0, 32, 64), ("HAWKEYE", 1, 0, 32, 128), 
                  ("HAWKEYE", 1, 1, 4, 8), ("HAWKEYE", 1, 1, 4, 16), ("HAWKEYE", 1, 1, 4, 32), ("HAWKEYE", 1, 1, 4, 64), ("HAWKEYE", 1, 1, 4, 128), 
                  ("HAWKEYE", 1, 1, 8, 8), ("HAWKEYE", 1, 1, 8, 16), ("HAWKEYE", 1, 1, 8, 32), ("HAWKEYE", 1, 1, 8, 64), ("HAWKEYE", 1, 1, 8, 128), 
                  ("HAWKEYE", 1, 1, 16, 8), ("HAWKEYE", 1, 1, 16, 16), ("HAWKEYE", 1, 1, 16, 32), ("HAWKEYE", 1, 1, 16, 64), ("HAWKEYE", 1, 1, 16, 128), 
                  ("HAWKEYE", 1, 1, 32, 8), ("HAWKEYE", 1, 1, 32, 16), ("HAWKEYE", 1, 1, 32, 32), ("HAWKEYE", 1, 1, 32, 64), ("HAWKEYE", 1, 1, 32, 128), 
                  ("DRRIP", 0, 0, 1, 1), 
                  ("DRRIP", 1, 0, 4, 8), ("DRRIP", 1, 0, 4, 16), ("DRRIP", 1, 0, 4, 32), ("DRRIP", 1, 0, 4, 64), ("DRRIP", 1, 0, 4, 128), 
                  ("DRRIP", 1, 0, 8, 8), ("DRRIP", 1, 0, 8, 16), ("DRRIP", 1, 0, 8, 32), ("DRRIP", 1, 0, 8, 64), ("DRRIP", 1, 0, 8, 128), 
                  ("DRRIP", 1, 0, 16, 8), ("DRRIP", 1, 0, 16, 16), ("DRRIP", 1, 0, 16, 32), ("DRRIP", 1, 0, 16, 64), ("DRRIP", 1, 0, 16, 128), 
                  ("DRRIP", 1, 0, 32, 8), ("DRRIP", 1, 0, 32, 16), ("DRRIP", 1, 0, 32, 32), ("DRRIP", 1, 0, 32, 64), ("DRRIP", 1, 0, 32, 128), 
                  ("DRRIP", 1, 1, 4, 8), ("DRRIP", 1, 1, 4, 16), ("DRRIP", 1, 1, 4, 32), ("DRRIP", 1, 1, 4, 64), ("DRRIP", 1, 1, 4, 128), 
                  ("DRRIP", 1, 1, 8, 8), ("DRRIP", 1, 1, 8, 16), ("DRRIP", 1, 1, 8, 32), ("DRRIP", 1, 1, 8, 64), ("DRRIP", 1, 1, 8, 128), 
                  ("DRRIP", 1, 1, 16, 8), ("DRRIP", 1, 1, 16, 16), ("DRRIP", 1, 1, 16, 32), ("DRRIP", 1, 1, 16, 64), ("DRRIP", 1, 1, 16, 128), 
                  ("DRRIP", 1, 1, 32, 8), ("DRRIP", 1, 1, 32, 16), ("DRRIP", 1, 1, 32, 32), ("DRRIP", 1, 1, 32, 64), ("DRRIP", 1, 1, 32, 128), 
				  ("SHIP", 0, 0, 1, 1), 
                  ("SHIP", 1, 0, 4, 8), ("SHIP", 1, 0, 4, 16), ("SHIP", 1, 0, 4, 32), ("SHIP", 1, 0, 4, 64), ("SHIP", 1, 0, 4, 128), 
                  ("SHIP", 1, 0, 8, 8), ("SHIP", 1, 0, 8, 16), ("SHIP", 1, 0, 8, 32), ("SHIP", 1, 0, 8, 64), ("SHIP", 1, 0, 8, 128), 
                  ("SHIP", 1, 0, 16, 8), ("SHIP", 1, 0, 16, 16), ("SHIP", 1, 0, 16, 32), ("SHIP", 1, 0, 16, 64), ("SHIP", 1, 0, 16, 128), 
                  ("SHIP", 1, 0, 32, 8), ("SHIP", 1, 0, 32, 16), ("SHIP", 1, 0, 32, 32), ("SHIP", 1, 0, 32, 64), ("SHIP", 1, 0, 32, 128), 
                  ("SHIP", 1, 1, 4, 8), ("SHIP", 1, 1, 4, 16), ("SHIP", 1, 1, 4, 32), ("SHIP", 1, 1, 4, 64), ("SHIP", 1, 1, 4, 128), 
                  ("SHIP", 1, 1, 8, 8), ("SHIP", 1, 1, 8, 16), ("SHIP", 1, 1, 8, 32), ("SHIP", 1, 1, 8, 64), ("SHIP", 1, 1, 8, 128), 
                  ("SHIP", 1, 1, 16, 8), ("SHIP", 1, 1, 16, 16), ("SHIP", 1, 1, 16, 32), ("SHIP", 1, 1, 16, 64), ("SHIP", 1, 1, 16, 128), 
                  ("SHIP", 1, 1, 32, 8), ("SHIP", 1, 1, 32, 16), ("SHIP", 1, 1, 32, 32), ("SHIP", 1, 1, 32, 64), ("SHIP", 1, 1, 32, 128), 
                  ("PERCEPTRON", 0, 0, 1, 1), 
                  ("PERCEPTRON", 1, 0, 4, 8), ("PERCEPTRON", 1, 0, 4, 16), ("PERCEPTRON", 1, 0, 4, 32), ("PERCEPTRON", 1, 0, 4, 64), ("PERCEPTRON", 1, 0, 4, 128), 
                  ("PERCEPTRON", 1, 0, 8, 8), ("PERCEPTRON", 1, 0, 8, 16), ("PERCEPTRON", 1, 0, 8, 32), ("PERCEPTRON", 1, 0, 8, 64), ("PERCEPTRON", 1, 0, 8, 128), 
                  ("PERCEPTRON", 1, 0, 16, 8), ("PERCEPTRON", 1, 0, 16, 16), ("PERCEPTRON", 1, 0, 16, 32), ("PERCEPTRON", 1, 0, 16, 64), ("PERCEPTRON", 1, 0, 16, 128), 
                  ("PERCEPTRON", 1, 0, 32, 8), ("PERCEPTRON", 1, 0, 32, 16), ("PERCEPTRON", 1, 0, 32, 32), ("PERCEPTRON", 1, 0, 32, 64), ("PERCEPTRON", 1, 0, 32, 128), 
                  ("PERCEPTRON", 1, 1, 4, 8), ("PERCEPTRON", 1, 1, 4, 16), ("PERCEPTRON", 1, 1, 4, 32), ("PERCEPTRON", 1, 1, 4, 64), ("PERCEPTRON", 1, 1, 4, 128), 
                  ("PERCEPTRON", 1, 1, 8, 8), ("PERCEPTRON", 1, 1, 8, 16), ("PERCEPTRON", 1, 1, 8, 32), ("PERCEPTRON", 1, 1, 8, 64), ("PERCEPTRON", 1, 1, 8, 128), 
                  ("PERCEPTRON", 1, 1, 16, 8), ("PERCEPTRON", 1, 1, 16, 16), ("PERCEPTRON", 1, 1, 16, 32), ("PERCEPTRON", 1, 1, 16, 64), ("PERCEPTRON", 1, 1, 16, 128), 
                  ("PERCEPTRON", 1, 1, 32, 8), ("PERCEPTRON", 1, 1, 32, 16), ("PERCEPTRON", 1, 1, 32, 32), ("PERCEPTRON", 1, 1, 32, 64), ("PERCEPTRON", 1, 1, 32, 128), 
				  ("RANDOM", 0, 0, 1, 1), 
                  ("RANDOM", 1, 0, 4, 8), ("RANDOM", 1, 0, 4, 16), ("RANDOM", 1, 0, 4, 32), ("RANDOM", 1, 0, 4, 64), ("RANDOM", 1, 0, 4, 128), 
                  ("RANDOM", 1, 0, 8, 8), ("RANDOM", 1, 0, 8, 16), ("RANDOM", 1, 0, 8, 32), ("RANDOM", 1, 0, 8, 64), ("RANDOM", 1, 0, 8, 128), 
                  ("RANDOM", 1, 0, 16, 8), ("RANDOM", 1, 0, 16, 16), ("RANDOM", 1, 0, 16, 32), ("RANDOM", 1, 0, 16, 64), ("RANDOM", 1, 0, 16, 128), 
                  ("RANDOM", 1, 0, 32, 8), ("RANDOM", 1, 0, 32, 16), ("RANDOM", 1, 0, 32, 32), ("RANDOM", 1, 0, 32, 64), ("RANDOM", 1, 0, 32, 128), 
                  ("RANDOM", 1, 1, 4, 8), ("RANDOM", 1, 1, 4, 16), ("RANDOM", 1, 1, 4, 32), ("RANDOM", 1, 1, 4, 64), ("RANDOM", 1, 1, 4, 128), 
                  ("RANDOM", 1, 1, 8, 8), ("RANDOM", 1, 1, 8, 16), ("RANDOM", 1, 1, 8, 32), ("RANDOM", 1, 1, 8, 64), ("RANDOM", 1, 1, 8, 128), 
                  ("RANDOM", 1, 1, 16, 8), ("RANDOM", 1, 1, 16, 16), ("RANDOM", 1, 1, 16, 32), ("RANDOM", 1, 1, 16, 64), ("RANDOM", 1, 1, 16, 128), 
                  ("RANDOM", 1, 1, 32, 8), ("RANDOM", 1, 1, 32, 16), ("RANDOM", 1, 1, 32, 32), ("RANDOM", 1, 1, 32, 64), ("RANDOM", 1, 1, 32, 128), 
				 ]
