""" The 'chemical_reaction_atom_mapping.epam_indigo' package 'atom_mapping' module. """

from functools import partial
from logging import getLogger
from typing import Iterable, List, Optional, Tuple

from indigo.indigo.indigo import Indigo

from ..utilities.multiprocessing import MultiprocessingUtilities


class EpamIndigoReactionAtomMappingUtilities:
    """ The EPAM Indigo library chemical reaction atom mapping utilities class. """

    @staticmethod
    def run_atom_mapping_on_reaction_smiles(
            reaction_smiles: str,
            timeout_period_ms: int = 10000,
            handle_existing_atom_mapping: str = "discard",
            ignore_charges: bool = False,
            ignore_isotopes: bool = False,
            ignore_valences: bool = False,
            ignore_radicals: bool = False,
            canonicalize_mapped_reaction_smiles: bool = True
    ) -> Tuple[Optional[str], Optional[bool]]:
        """
        Run the EPAM Indigo library atom mapping on a chemical reaction SMILES string.

        :parameter reaction_smiles: The chemical reaction SMILES string.
        :parameter timeout_period_ms: The maximum amount of time in milliseconds that may be spent on the atom mapping
                                      procedure.
        :parameter handle_existing_atom_mapping: The indicator how existing atom mapping should be handled.
        :parameter ignore_charges: The indicator whether the chemical reaction compound atom charges should be ignored
                                   during the atom mapping procedure.
        :parameter ignore_isotopes: The indicator whether the chemical reaction compound atom isotopes should be ignored
                                    during the atom mapping procedure.
        :parameter ignore_valences: The indicator whether the chemical reaction compound atom valences should be ignored
                                    during the atom mapping procedure.
        :parameter ignore_radicals: The indicator whether the chemical reaction compound atom radicals should be ignored
                                    during the atom mapping procedure.
        :parameter canonicalize_mapped_reaction_smiles: The indicator whether the mapped chemical reaction SMILES string
                                                        should be canonicalized.

        :returns: The mapped chemical reaction SMILES string, and the indicator whether the atom mapping procedure was
                  completed without errors.
        """

        try:
            epam_indigo_toolkit = Indigo()

            epam_indigo_toolkit.setOption("aam-timeout", timeout_period_ms)

            # ----------------------------------------------------------------------------------------------------------
            #  The 'loadReactionSmarts' method is utilized instead of the 'loadReaction' method to avoid the EPAM Indigo
            #  library internal sanitization procedure which can sometimes raise exceptions for correct chemical
            #  reaction compound SMILES strings.
            # ----------------------------------------------------------------------------------------------------------

            reaction_epam_indigo_rxn = epam_indigo_toolkit.loadReactionSmarts(
                string=reaction_smiles
            )

            epam_indigo_status_code = reaction_epam_indigo_rxn.automap(
                mode="".join([
                    handle_existing_atom_mapping
                    if handle_existing_atom_mapping in ["alter", "clear", "discard", "keep"] else "discard",
                    " ignore_charges" if ignore_charges else "",
                    " ignore_isotopes" if ignore_isotopes else "",
                    " ignore_valence" if ignore_valences else "",
                    " ignore_radicals" if ignore_radicals else ""
                ])
            )

            if canonicalize_mapped_reaction_smiles:
                return reaction_epam_indigo_rxn.canonicalSmiles(), True if epam_indigo_status_code == 1 else False

            else:
                return reaction_epam_indigo_rxn.smiles(), True if epam_indigo_status_code == 1 else False

        except Exception as exception_handle:
            getLogger(
                "{0}.EpamIndigoReactionAtomMappingUtilities.run_atom_mapping_on_reaction_smiles".format(__name__)
            ).debug(exception_handle)

            return None, None

    @staticmethod
    def run_atom_mapping_on_reaction_smiles_strings(
            reaction_smiles_strings: Iterable[str],
            number_of_cpu_cores: int = 1,
            **kwargs
    ) -> List[Tuple[Optional[str], Optional[bool]]]:
        """
        Run the EPAM Indigo library atom mapping on chemical reaction SMILES strings.

        :parameter reaction_smiles_strings: The chemical reaction SMILES strings.
        :parameter number_of_cpu_cores: The number of CPU cores that should be utilized.
        :parameter kwargs: The default keyword arguments for the adjustment of underlying functions:
                           'chemical_reaction_atom_mapping.indigo.IndigoReactionAtomMappingUtilities.
                           {run_atom_mapping_on_reaction_smiles}'.

        :returns: The mapped chemical reaction SMILES strings, and the indicators whether the atom mapping procedure
                  was completed without errors.
        """

        return MultiprocessingUtilities.run_with_progress_bar(
            processing_procedure=partial(
                EpamIndigoReactionAtomMappingUtilities.run_atom_mapping_on_reaction_smiles,
                **kwargs
            ),
            primary_input_argument=reaction_smiles_strings,
            description_message="Mapping the chemical reaction SMILES strings using the EPAM Indigo library",
            number_of_cpu_cores=number_of_cpu_cores
        )
