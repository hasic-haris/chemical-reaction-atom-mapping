#!/bin/bash

export PYTHONPATH=$PYTHONPATH:"/path/to/project/root/directory"

export LIBRARY="chytorch_rxnmap"
export REACTION_SMILES="BrCCBr.COC(=O)c1cc(n[nH]1)C(F)(F)F>>COC(=O)c1cc(nn1CCBr)C(F)(F)F"


python "$(cd -P "$(dirname "${BASH_SOURCE[0]}")" && pwd)"/run_atom_mapping_on_reaction_smiles.py \
        --library $LIBRARY \
        --reaction_smiles $REACTION_SMILES
