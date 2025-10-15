#!/bin/bash
## Do not put any commands or blank lines before the #SBATCH lines
#SBATCH --nodes=2                   # Number of nodes - all cores per node are allocated to the job
#SBATCH --time=4:00:00              # Wall clock time (HH:MM:SS) - once the job exceeds this time, the job will be terminated (default is 5 minutes)
#SBATCH --account=fy250045 # WC ID
#SBATCH --job-name=decay_v1              # Name of job
#SBATCH --partition=short,batch       # partition/queue name: short or batch
                                      #            short: 4hrs wallclock limit
                                      #            batch: nodes reserved for > 4hrs (default)
#SBATCH --qos=normal                  # Quality of Service: long, large, priority or normal
                                      #           normal: request up to 48hrs wallclock (default)
                                      #           long:   request up to 96hrs wallclock and no larger than 64nodes
                                      #           large:  greater than 50% of cluster (special request)
                                      #           priority: High priority jobs (special request)

nodes=$SLURM_JOB_NUM_NODES

source ~/Software/OpenFOAM-v2312/etc/bashrc
sed -i "s/^nNodes.*/nNodes $nodes;/" system/decomposeParDict

./restart.sh
./Allrun


