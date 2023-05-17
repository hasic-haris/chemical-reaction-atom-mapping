""" The 'scripts' directory 'run_atom_mapping_on_reaction_smiles' script. """

from argparse import ArgumentParser, Namespace


def parse_arguments() -> Namespace:
    """ Parse the 'run_atom_mapping_on_reaction_smiles' script arguments. """

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
        "-s",
        "--reaction_smiles",
        type=str,
        required=True,
        help="The chemical reaction SMILES string."
    )

    return argument_parser.parse_args()


if __name__ == "__main__":
    script_arguments = parse_arguments()

    if script_arguments.library == "chytorch_rxnmap":
        from chemical_reaction_atom_mapping.chytorch_rxnmap import ChytorchRxnMapReactionAtomMappingUtilities

        chytorch_rxnmap_mapped_reaction_smiles, chytorch_rxnmap_atom_mapping_score = \
            ChytorchRxnMapReactionAtomMappingUtilities.run_atom_mapping_on_reaction_smiles(
                reaction_smiles=script_arguments.reaction_smiles
            )

        print("Reaction SMILES: '{0}'".format(script_arguments.reaction_smiles))
        print("Mapped Reaction SMILES (Chytorch RxnMap): '{0}'".format(chytorch_rxnmap_mapped_reaction_smiles))
        print("Atom Mapping Score (Chytorch RxnMap): {0}".format(chytorch_rxnmap_atom_mapping_score))

    elif script_arguments.library == "epam_indigo":
        from chemical_reaction_atom_mapping.epam_indigo import EpamIndigoReactionAtomMappingUtilities

        epam_indigo_mapped_reaction_smiles, epam_indigo_atom_mapping_status_indicator = \
            EpamIndigoReactionAtomMappingUtilities.run_atom_mapping_on_reaction_smiles(
                reaction_smiles=script_arguments.reaction_smiles
            )

        print("Reaction SMILES: '{0}'".format(script_arguments.reaction_smiles))
        print("Mapped Reaction SMILES (EPAM Indigo): '{0}'".format(epam_indigo_mapped_reaction_smiles))
        print("Atom Mapping Procedure Completed without Errors (EPAM Indigo): {0}".format(
            epam_indigo_atom_mapping_status_indicator
        ))

    elif script_arguments.library == "rxnmapper":
        from chemical_reaction_atom_mapping.rxnmapper import RxnMapperReactionAtomMappingUtilities

        rxnmapper_mapped_reaction_smiles, rxnmapper_atom_mapping_confidence_score = \
            RxnMapperReactionAtomMappingUtilities.run_atom_mapping_on_reaction_smiles(
                reaction_smiles=script_arguments.reaction_smiles
            )

        print("Reaction SMILES: '{0}'".format(script_arguments.reaction_smiles))
        print("Mapped Reaction SMILES (RXNMapper): '{0}'".format(rxnmapper_mapped_reaction_smiles))
        print("Atom Mapping Confidence Score (RXNMapper): {0}".format(rxnmapper_atom_mapping_confidence_score))
