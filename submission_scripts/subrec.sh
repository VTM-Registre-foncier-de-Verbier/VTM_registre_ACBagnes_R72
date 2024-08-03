#!/bin/env bash
#SBATCH --partition=shared-gpu
#SBATCH --time=02:00:00
#SBATCH --gpus=1
#SBATCH --output=kraken-%j.out
#SBATCH --mem=12GB
#SBATCH --ntasks-per-node=12
#SBATCH --gres=gpu:1,VramPerGpu:24GB

module load CUDA/11.8.0 GCCcore/11.2.0 Python/3.9.6
source ~/kraken-env/bin/activate

OUTPUT_NAME="output_name"
XML_FOLDER="/home/users/p/payotch2/VTM_registre_ACBagnes_R72/data"

echo "KETOS training"
srun ketos train -o $OUTPUT_NAME -f alto -d cuda:0 "${XML_FOLDER}/*.xml" --workers 4
