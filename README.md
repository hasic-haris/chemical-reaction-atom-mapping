# Chemical Reaction Atom Mapping
The computer-assisted synthesis field grew to become one of the most active fields in chemoinformatics, with new and
improved approaches centered around chemical reactions being published on a regular basis. To understand the gist of a
chemical reaction, it is essential to know how the atoms of the participating compounds re-arrange during the chemical
transformation. This process is widely known as atom mapping, and it has proven to be quite challenging. Taking all of
this into account, the goal of this project is to systematically curate, categorize and facilitate the access to
existing open-source chemical reaction atom mapping libraries in one place.

**Author:** Haris Hasić, M.Eng.<br>
**Affiliation:**
Dr.Sci. Student @
[Ishida Laboratory, Department of Computer Science, Tokyo Institute of Technology](http://www.cb.cs.titech.ac.jp) &&
Research Engineer @ [Elix, Inc.](https://www.elix-inc.com)<br>
**Current Version:** 2023.1.0


## Setup
To use the ***chemical_reaction_atom_mapping*** package, please ensure that the
[chytorch-rxnmap](https://github.com/chython/chytorch-rxnmap), [epam.indigo](https://github.com/epam/Indigo),
[rxnmapper](https://github.com/rxn4chemistry/rxnmapper) and [tqdm](https://github.com/tqdm/tqdm) libraries are
available. A minimal execution environment can be set up using [conda](https://docs.conda.io/en/latest/) and
[pip](https://pip.pypa.io/en/stable/) as follows:

```shell
conda create -c conda-forge -n chemical-reaction-atom-mapping python=3.8 rdkit -y

conda activate chemical-reaction-atom-mapping

pip install chython chytorch chytorch-rxnmap epam.indigo rxnmapper tqdm
```


## Scripts
The ***scripts*** directory is primarily meant to illustrate how to utilize the ***chemical_reaction_atom_mapping***
package to run the atom mapping procedures on chemical reaction data. The first line of each script is just a reminder
to add the path to the project root directory to the `PYTHONPATH` variable to make the package visible before running
the scripts.


## Supported Chemical Reaction Atom Mapping Libraries
Currently, the ***chemical_reaction_atom_mapping*** package supports the following open-source chemical reaction atom
mapping libraries:

1. The [EPAM Indigo](https://github.com/epam/Indigo) library incorporates a number of unique algorithms developed by
   [EPAM](https://lifescience.opensource.epam.com), as well as some standard algorithms well-known in the
   cheminformatics world. [[1]](#References)
2. The [RXNMapper](https://github.com/rxn4chemistry/rxnmapper) library is constructed around a chemically agnostic
   attention-guided reaction mapper transformer model that shows a remarkable performance in terms of accuracy and
   speed, even for strongly imbalanced reactions. [[2]](#References)
3. The [Chytorch RxnMap](https://github.com/chython/chytorch-rxnmap) library is constructed around a transformer neural
   network adopted for the direct processing of molecular graphs as sets of atoms and bonds, as opposed to
   SMILES/SELFIES sequence-based approaches, in combination with the Bidirectional Encoder Representations from
   Transformers (BERT) network. [[3]](#References)


## License Information
This project is published under the [MIT License](/LICENSE). For more details on the license information of individual
chemical reaction atom mapping libraries, please refer to the original publications.


## Contact
If you are interested in contributing to this project by reporting bugs, submitting feedback or anything else that
might be beneficial, please feel free to do so via GitHub issues or [e-mail](mailto:hasic@cb.cs.titech.ac.jp). Also,
check out the latest [Elix, Inc.](https://www.elix-inc.com/research) research. 


## References
1. **EPAM Indigo Library**: https://lifescience.opensource.epam.com/indigo/index.html. Accessed on: May 18th, 2023.
2. Schwaller, P., Hoover, B., Reymond, J., Strobelt, H., and Laino, T. **Extraction of Organic Chemistry Grammar from
   Unsupervised Learning of Chemical Reactions**. *Sci. Adv.*, 2021, 7, 15. DOI:
   https://doi.org/10.1126/sciadv.abe4166.
3. Nugmanov, R., Dyubankova, N., Gedich, A., and Wegner, J.K. **Bidirectional Graphormer for Reactivity Understanding:
   Neural Network Trained to Reaction Atom-to-Atom Mapping Task**, *J. Chem. Inf. Model.*, 2022, 62, 14, 3307–3315.
   DOI: https://doi.org/10.1021/acs.jcim.2c00344.
