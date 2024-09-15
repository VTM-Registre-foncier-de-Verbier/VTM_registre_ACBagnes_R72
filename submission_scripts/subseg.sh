#!/bin/env bash
#SBATCH --partition=shared-gpu
#SBATCH --time=08:00:00
#SBATCH --gpus=1
#SBATCH --output=kraken-%j.out
#SBATCH --mem=24GB
#SBATCH --cpus-per-task=4
#SBATCH --gres=gpu:1,VramPerGpu:24GB


module load CUDA/11.8.0 GCCcore/11.2.0 Python/3.9.6
source ~/kraken-env/bin/activate


echo "KETOS training"
srun ketos segtrain -t train.txt
