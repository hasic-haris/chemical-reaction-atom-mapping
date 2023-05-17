""" The 'chemical_reaction_atom_mapping.rxnmapper' package 'atom_mapping' module. """

from logging import getLogger
from tqdm import tqdm
from typing import Any, Iterable, Dict, List, Optional, Tuple

from rxnmapper.core import RXNMapper
from transformers.utils.logging import set_verbosity_error


class RxnMapperReactionAtomMappingUtilities:
    """ The RXNMapper library chemical reaction atom mapping utilities class. """

    @staticmethod
    def _get_attention_guided_atom_maps_wrapper(
            rxnmapper_model: RXNMapper,
            reaction_smiles_strings: List[str],
            **kwargs
    ) -> List[Dict[str, Any]]:
        """
        The 'RXNMapper' class 'get_attention_guided_atom_maps' method wrapper.

        :parameter rxnmapper_model: The RXNMapper model RXNMapper object.
        :parameter reaction_smiles_strings: The chemical reaction SMILES strings.
        :parameter kwargs: The default keyword arguments for the adjustment of underlying functions:
                           'rxnmapper.core.RXNMapper.{get_attention_guided_atom_maps}'.

        :returns: The mapped chemical reaction SMILES strings, and the RXNMapper library atom mapping confidence scores.
        """

        return rxnmapper_model.get_attention_guided_atom_maps(
            rxns=reaction_smiles_strings,
            zero_set_p=kwargs["zero_set_p"] if "zero_set_p" in kwargs.keys() else True,
            zero_set_r=kwargs["zero_set_r"] if "zero_set_r" in kwargs.keys() else True,
            canonicalize_rxns=kwargs["canonicalize_rxns"] if "canonicalize_rxns" in kwargs.keys() else True,
            detailed_output=kwargs["detailed_output"] if "detailed_output" in kwargs.keys() else False,
            absolute_product_inds=kwargs["absolute_product_inds"]
            if "absolute_product_inds" in kwargs.keys() else False,
            force_layer=kwargs["force_layer"] if "force_layer" in kwargs.keys() else None,
            force_head=kwargs["force_head"] if "force_head" in kwargs.keys() else None
        )

    @staticmethod
    def run_atom_mapping_on_reaction_smiles(
            reaction_smiles: str,
            **kwargs
    ) -> Tuple[Optional[str], Optional[float]]:
        """
        Run the RXNMapper library atom mapping on a chemical reaction SMILES string.

        :parameter reaction_smiles: The chemical reaction SMILES string.
        :parameter kwargs: The default keyword arguments for the adjustment of underlying functions:
                           'rxnmapper.core.RXNMapper.{get_attention_guided_atom_maps}'.

        :returns: The mapped chemical reaction SMILES string, and the RXNMapper library atom mapping confidence score.
        """

        try:
            set_verbosity_error()

            rxnmapper_model_output = RxnMapperReactionAtomMappingUtilities._get_attention_guided_atom_maps_wrapper(
                rxnmapper_model=RXNMapper(),
                reaction_smiles_strings=[reaction_smiles],
                **kwargs
            )[0]

            return rxnmapper_model_output["mapped_rxn"] if "mapped_rxn" in rxnmapper_model_output.keys() else None, \
                   rxnmapper_model_output["confidence"] if "confidence" in rxnmapper_model_output.keys() else None

        except Exception as exception_handle:
            getLogger(
                "{0}.RxnMapperReactionAtomMappingUtilities.run_atom_mapping_on_reaction_smiles".format(__name__)
            ).debug(exception_handle)

            return None, None

    @staticmethod
    def run_atom_mapping_on_reaction_smiles_strings(
            reaction_smiles_strings: Iterable[str],
            number_of_reaction_smiles_strings: int,
            rxnmapper_model_batch_size: int = 10,
            **kwargs
    ) -> Optional[List[Tuple[Optional[str], Optional[float]]]]:
        """
        Run the RXNMapper library atom mapping on chemical reaction SMILES strings.

        :parameter reaction_smiles_strings: The chemical reaction SMILES strings.
        :parameter number_of_reaction_smiles_strings: The number of chemical reaction SMILES strings.
        :parameter rxnmapper_model_batch_size: The RXNMapper model batch size.
        :parameter kwargs: The default keyword arguments for the adjustment of underlying functions:
                           'rxnmapper.core.RXNMapper.{get_attention_guided_atom_maps}'.

        :returns: The mapped chemical reaction SMILES strings, and the RXNMapper library atom mapping confidence scores.
        """

        try:
            set_verbosity_error()

            rxnmapper_model = RXNMapper()

            reaction_smiles_batch, mapped_reaction_smiles_strings_and_confidence_scores = list(), list()

            for reaction_smiles_index, reaction_smiles in tqdm(
                iterable=enumerate(reaction_smiles_strings),
                total=number_of_reaction_smiles_strings,
                ascii=True,
                ncols=150,
                desc="Mapping the chemical reaction SMILES strings using the RXNMapper library"
            ):
                reaction_smiles_batch.append(
                    reaction_smiles
                )

                if (reaction_smiles_index + 1) % rxnmapper_model_batch_size == 0:
                    rxnmapper_model_outputs = \
                        RxnMapperReactionAtomMappingUtilities._get_attention_guided_atom_maps_wrapper(
                            rxnmapper_model=rxnmapper_model,
                            reaction_smiles_strings=reaction_smiles_batch,
                            **kwargs
                        )

                    for rxnmapper_model_output in rxnmapper_model_outputs:
                        mapped_reaction_smiles_strings_and_confidence_scores.append((
                            rxnmapper_model_output["mapped_rxn"]
                            if "mapped_rxn" in rxnmapper_model_output.keys() else None,
                            rxnmapper_model_output["confidence"]
                            if "confidence" in rxnmapper_model_output.keys() else None
                        ))

                    reaction_smiles_batch.clear()

            if len(reaction_smiles_batch) > 0:
                rxnmapper_model_outputs = RxnMapperReactionAtomMappingUtilities._get_attention_guided_atom_maps_wrapper(
                    rxnmapper_model=rxnmapper_model,
                    reaction_smiles_strings=reaction_smiles_batch,
                    **kwargs
                )

                for rxnmapper_model_output in rxnmapper_model_outputs:
                    mapped_reaction_smiles_strings_and_confidence_scores.append((
                        rxnmapper_model_output["mapped_rxn"] if "mapped_rxn" in rxnmapper_model_output.keys() else None,
                        rxnmapper_model_output["confidence"] if "confidence" in rxnmapper_model_output.keys() else None
                    ))

            return mapped_reaction_smiles_strings_and_confidence_scores

        except Exception as exception_handle:
            getLogger(
                "{0}.RxnMapperReactionAtomMappingUtilities.run_atom_mapping_on_reaction_smiles_strings".format(__name__)
            ).debug(exception_handle)

            return None
