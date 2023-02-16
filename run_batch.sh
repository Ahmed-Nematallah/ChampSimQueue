#!/bin/bash
#SBATCH -A p2017001
#SBATCH --time 04:00:0
#SBATCH --requeue

chmod +x results/temp_scripts/*.sh

BATCH=0

if [ $# -eq 0 ] 
then
	echo "No arguments supplied, running with sbatch"
elif [ $1 = "-bash" ] 
then
	BATCH=1
fi

for f in results/temp_scripts/*.sh; do
	if [ $BATCH -eq 0 ] 
	then
		sbatch "$f" 
	else
		/bin/bash "$f" #& # Remove comment to parallelize, do at your own risk
	fi
done
