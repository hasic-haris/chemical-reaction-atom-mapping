""" The 'chemical_reaction_atom_mapping' package initialization module. """

from logging import Formatter, getLogger, INFO, StreamHandler


__author__, __institution__, __version__ = (
    "Haris Hasic",
    "Ishida Laboratory, Department of Computer Science, Tokyo Institute of Technology && Elix, Inc.",
    "2023.1.0"
)


chemical_reaction_atom_mapping_logger = getLogger(__name__)
chemical_reaction_atom_mapping_logger.setLevel(INFO)

chemical_reaction_atom_mapping_stream_handler = StreamHandler()
chemical_reaction_atom_mapping_stream_handler.setLevel(INFO)

chemical_reaction_atom_mapping_stream_handler.setFormatter(
    Formatter("%(asctime)s (%(levelname)s @ %(name)s): %(message)s")
)

chemical_reaction_atom_mapping_logger.addHandler(chemical_reaction_atom_mapping_stream_handler)
