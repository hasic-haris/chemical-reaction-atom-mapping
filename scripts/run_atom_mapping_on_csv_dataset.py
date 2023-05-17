""" The 'scripts' directory 'run_atom_mapping_on_csv_dataset' script. """

from argparse import ArgumentParser, Namespace

from pandas import read_csv


def parse_arguments() -> Namespace:
    """ Parse the 'run_atom_mapping_on_csv_dataset' script arguments. """

    argument_parser = ArgumentParser()

    argument_parser.add_argument(
        "-l",
        "--library",
        type=str,
        choices=[
            "chytorch_rxnmap",
            "epam_indigo",
            "rxnmapper"
        ],
        required=True,
        help="The indicator of the chemical reaction atom mapping library that should be utilized."
    )

    argument_parser.add_argument(
        "-i",
        "--input_csv_dataset_file_path",
        type=str,
        required=True,
        help="The path to the input '*.csv' dataset file."
    )

    argument_parser.add_argument(
        "-s",
        "--reaction_smiles_column_name",
        type=str,
        required=True,
        help="The name of the chemical reaction SMILES string column in the input dataset '*.csv' file."
    )

    argument_parser.add_argument(
        "-o",
        "--output_csv_dataset_file_path",
        type=str,
        required=True,
        help="The path to the output '*.csv' dataset file."
    )

    argument_parser.add_argument(
        "-c",
        "--number_of_cpu_cores",
        type=int,
        default=1,
        help="The number of CPU cores that should be utilized."
    )

    return argument_parser.parse_args()


if __name__ == "__main__":
    script_arguments = parse_arguments()

    csv_dataset = read_csv(
        filepath_or_buffer=script_arguments.input_csv_dataset_file_path
    )

    if script_arguments.library == "chytorch_rxnmap":
        from chemical_reaction_atom_mapping.chytorch_rxnmap import ChytorchRxnMapReactionAtomMappingUtilities

        chytorch_rxnmap_atom_mapping_outputs = \
            ChytorchRxnMapReactionAtomMappingUtilities.run_atom_mapping_on_reaction_smiles_strings(
                reaction_smiles_strings=csv_dataset[script_arguments.reaction_smiles_column_name].values
            )

        csv_dataset["chytorch_rxnmap_mapped_reaction_smiles"], csv_dataset["chytorch_rxnmap_atom_mapping_score"] = \
            list(zip(*chytorch_rxnmap_atom_mapping_outputs))

        csv_dataset.to_csv(
            path_or_buf=script_arguments.output_csv_dataset_file_path,
            index=False
        )

    elif script_arguments.library == "epam_indigo":
        from chemical_reaction_atom_mapping.epam_indigo import EpamIndigoReactionAtomMappingUtilities

        epam_indigo_atom_mapping_outputs = \
            EpamIndigoReactionAtomMappingUtilities.run_atom_mapping_on_reaction_smiles_strings(
                reaction_smiles_strings=csv_dataset[script_arguments.reaction_smiles_column_name],
                number_of_cpu_cores=script_arguments.number_of_cpu_cores
            )

        csv_dataset["epam_indigo_mapped_reaction_smiles"], csv_dataset["epam_indigo_atom_mapping_status_indicator"] = \
            list(zip(*epam_indigo_atom_mapping_outputs))

        csv_dataset.to_csv(
            path_or_buf=script_arguments.output_csv_dataset_file_path,
            index=False
        )

    elif script_arguments.library == "rxnmapper":
        from chemical_reaction_atom_mapping.rxnmapper import RxnMapperReactionAtomMappingUtilities

        rxnmapper_atom_mapping_outputs = \
            RxnMapperReactionAtomMappingUtilities.run_atom_mapping_on_reaction_smiles_strings(
                reaction_smiles_strings=csv_dataset[script_arguments.reaction_smiles_column_name],
                number_of_reaction_smiles_strings=len(csv_dataset[script_arguments.reaction_smiles_column_name])
            )

        csv_dataset["rxnmapper_mapped_reaction_smiles"], csv_dataset["rxnmapper_atom_mapping_confidence_score"] = \
            list(zip(*rxnmapper_atom_mapping_outputs))

        csv_dataset.to_csv(
            path_or_buf=script_arguments.output_csv_dataset_file_path,
            index=False
        )
