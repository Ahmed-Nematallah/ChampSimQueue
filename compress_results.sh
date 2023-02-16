cd results/individual_results
timestamp=$(date +%s)
if [ ! -d ../compressed_results ]; then
	mkdir ../compressed_results
fi
zip -9 -j -q "../compressed_results/results$timestamp.zip" ../../champsim_run_commons.py *.txt
