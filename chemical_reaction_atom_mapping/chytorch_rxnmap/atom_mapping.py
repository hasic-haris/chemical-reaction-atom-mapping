""" The 'chemical_reaction_atom_mapping.chytorch_rxnmap' package 'atom_mapping' module. """

from functools import partial
from logging import getLogger
from typing import Iterable, List, Optional, Tuple
from warnings import filterwarnings

from chython.files.daylight.smiles import smiles

from ..utilities.multiprocessing import MultiprocessingUtilities


class ChytorchRxnMapReactionAtomMappingUtilities:
    """ The Chytorch RxnMap library chemical reaction atom mapping utilities class. """

    @staticmethod
    def run_atom_mapping_on_reaction_smiles(
            reaction_smiles: str,
            **kwargs
    ) -> Tuple[Optional[str], Optional[float]]:
        """
        Run the Chytorch RxnMap library atom mapping on a chemical reaction SMILES string.

        :parameter reaction_smiles: The chemical reaction SMILES string.
        :parameter kwargs: The default keyword arguments for the adjustment of underlying functions:
                           'chython.files.daylight.smiles.{smiles}' and
                           'chython.algorithms.mapping.attention.Attention.{reset_mapping}'.

        :returns: The mapped chemical reaction SMILES string, and the Chytorch RxnMap library atom mapping score.
        """

        try:
            reaction_chytorch_rxnmap_rxn = smiles(
                reaction_smiles,
                ignore=kwargs["ignore"] if "ignore" in kwargs.keys() else True,
                remap=kwargs["remap"] if "remap" in kwargs.keys() else False,
                ignore_stereo=kwargs["ignore_stereo"] if "ignore_stereo" in kwargs.keys() else False,
                ignore_bad_isotopes=kwargs["ignore_bad_isotopes"] if "ignore_bad_isotopes" in kwargs.keys() else False,
                keep_implicit=kwargs["keep_implicit"] if "keep_implicit" in kwargs.keys() else False,
                ignore_carbon_radicals=kwargs["ignore_carbon_radicals"]
                if "ignore_carbon_radicals" in kwargs.keys() else False
            )

            chytorch_rxnmap_atom_mapping_score = reaction_chytorch_rxnmap_rxn.reset_mapping(
                return_score=True,
                multiplier=kwargs["multiplier"] if "multiplier" in kwargs.keys() else 1.75,
                keep_reactants_numbering=kwargs["keep_reactants_numbering"]
                if "keep_reactants_numbering" in kwargs.keys() else False
            )

            mapped_reaction_smiles = format(reaction_chytorch_rxnmap_rxn, "m")

            return mapped_reaction_smiles, chytorch_rxnmap_atom_mapping_score

        except Exception as exception_handle:
            getLogger(
                "{0}.ChytorchRxnMapReactionAtomMappingUtilities.run_atom_mapping_on_reaction_smiles".format(__name__)
            ).exception(exception_handle)

            return None, None

    @staticmethod
    def run_atom_mapping_on_reaction_smiles_strings(
            reaction_smiles_strings: Iterable[str],
            **kwargs
    ) -> List[Tuple[Optional[str], Optional[float]]]:
        """
        Run the Chytorch RxnMap library atom mapping on chemical reaction SMILES strings.

        :parameter reaction_smiles_strings: The chemical reaction SMILES strings.
        :parameter kwargs: The default keyword arguments for the adjustment of underlying functions:
                           'chython.files.daylight.smiles.{smiles}' and
                           'chython.algorithms.mapping.attention.Attention.{reset_mapping}'.

        :returns: The mapped chemical reaction SMILES strings, and the Chytorch RxnMap library atom mapping scores.
        """

        filterwarnings(
            action="ignore"
        )

        return MultiprocessingUtilities.run_with_progress_bar(
            processing_procedure=partial(
                ChytorchRxnMapReactionAtomMappingUtilities.run_atom_mapping_on_reaction_smiles,
                **kwargs
            ),
            primary_input_argument=reaction_smiles_strings,
            description_message="Mapping the chemical reaction SMILES strings using the Chytorch RxnMap library"
        )
