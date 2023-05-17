#!/bin/bash

export PYTHONPATH=$PYTHONPATH:"/path/to/project/root/directory"

export LIBRARY="chytorch_rxnmap"
export INPUT_CSV_DATASET_FILE_PATH="/path/to/input/csv/dataset/file.csv"
export REACTION_SMILES_COLUMN_NAME="reaction_smiles"
export OUTPUT_CSV_DATASET_FILE_PATH="/path/to/output/csv/dataset/file.csv"
export NUMBER_OF_CPU_CORES=1


python "$(cd -P "$(dirname "${BASH_SOURCE[0]}")" && pwd)"/run_atom_mapping_on_csv_dataset.py \
        --library $LIBRARY \
        --input_csv_dataset_file_path $INPUT_CSV_DATASET_FILE_PATH \
        --reaction_smiles_column_name $REACTION_SMILES_COLUMN_NAME \
        --output_csv_dataset_file_path $OUTPUT_CSV_DATASET_FILE_PATH \
        --number_of_cpu_cores $NUMBER_OF_CPU_CORES
