# RosettaMPNN

## Overview

### Description
RosettaMPNN contains code for running protein sequence design based on [ProteinMPNN](https://github.com/dauparas/ProteinMPNN) and [LigandMPNN](https://github.com/dauparas/LigandMPNN) with additional features and weights developed for these models after their original release. RosettaMPNN is maintained by the [RosettaCommons](https://www.rosettacommons.org/). 

### Key Publications

[ProteinMPNN](https://github.com/dauparas/ProteinMPNN): [https://doi.org/10.1126/science.add2187](https://doi.org/10.1126/science.add2187)

[LigandMPNN](https://github.com/dauparas/LigandMPNN): [https://doi.org/10.1038/s41592-025-02626-1](https://doi.org/10.1038/s41592-025-02626-1)

[HyperMPNN](https://github.com/meilerlab/HyperMPNN): [https://doi.org/10.1101/2024.11.26.625397](https://doi.org/10.1101/2024.11.26.625397)

---
## Table of Contents

- [Overview](#overview)
  - [Description](#description)
  - [Key Publications](#key-publications)
- [Getting Started](#getting-started)
  - [Installation Guide](#installation-guide)
    - [Prerequisites](#prerequisites)
    - [Installation Methods](#installation-methods)
    - [Post-Installation Setup](#post-installation-setup)
  - [Usage](#usage)
    - [Input Files](#input-files)
    - [Output Files](#output-files)
    - [How to Run](#how-to-run)
    - [Description](#description)
- [Developing](#developing)
- [Support & Help](#support--help)
- [Acknowledgements](#acknowledgements)

## Getting Started
### Installation Guide

**Prerequisites:**  
[Conda or Miniconda](https://www.anaconda.com/download) installation 

**Installation**
1. Clone the repository
```
git clone https://github.com/woodsh17/RosettaMPNN.git
```
2. Download the model weights (includes weights for HyperMPNN)
```
cd RosettaMPNN
bash get_model_params.sh model_params
```
3. Setup conda/or other environment
```
conda create -n rosettampnn_env python=3.11
conda activate rosettampnn
pip install -r requirements.txt
```
***Whenever you want to run RosettaMPNN you will need to activate your RosettaMPNN environment via `conda activate rosettampnn`***
4. Add RosettaMPNN to your PYTHONPATH
```
export PYTHONPATH=/PATH/TO/RosettaMPNN:$PYTHONPATH
```

_Docker image coming soon_

### Usage

**How to Run Basic Use Case:**  
For this example we will use 1BC8.pdb from the example inputs.
```
python -m RosettaMPNN \
--out_folder ./out/ \
--pdb_path ~/RosettaMPNN/inputs/1BC8.pdb \
--checkpoint_protein_mpnn ~/RosettaMPNN/model_params/ proteinmpnn_v_48_020.pt 
```
If this runs successfully, in the `out_folder` you specified you should have three directories created:
* `seqs` with the designed sequence in the fasta file `1BC8.fa`
* `backbones` with the output structure containing the predicted sequence in pdb file: `1BC8.pdb`
* `packed` that should be empty since we didn't specify for side-chains to be packed

**Multi-State Design:** 
The multi-state implementation for RosettaMPNN has not been scientifically tested yet so use with caution! This was originally implemented by the Kuhlman lab into ProteinMPNN (https://github.com/Kuhlman-Lab/proteinmpnn)
```
#copy PDB files to working directory
cp PATH/TO/RosettaMPNN/inputs/4GYT_dimer.pdb .
cp PATH/TO/RosettaMPNN/inputs/4GYT_monomer.pdb .
#create json file that points to input pdbs
cat <<EOF >> msd_pdbs.json
{
    "./4GYT_dimer.pdb": "",
    "./4GYT_monomer.pdb": ""
}
EOF

#run RosettaMPNN with multi_state design options
python -m RosettaMPNN \
--out_folder ./out_msd \
--multi_state_pdb_path ~/RosettaMPNN/inputs/msd_pdbs.json \
--multi_state_constraints 4GYT_dimer:A7-A183:0.5,4GYT_dimer:B7-B183:0.5,4GYT_monomer:A7-A183:1 \
--checkpoint_protein_mpnn ~/RosettaMPNN/model_params/proteinmpnn_v_48_020.pt 
```
If this runs successfully, you will have the same directories as before, with an additional `msd` directory where a pdb (`msd.pdb`)that combines all pdb files listed in the input json file are combined into one pdb file and separated in space. 


For more information on how to run RosettaMPNN and different options available see the documentation. 

---
### Developing 
We welcome contributions to improve RosettaMPNN. We use a fork-and-PR system for contribution. To contribute to RosettaMPNN, please fork the RosettaMPNN repo under your own Github user space. You can then develop your additions in your own space. Once you're ready to contribute it back, open a PR agaist the main RosettaMPNN repo.

### Support & Help
You can find more detailed documentation here: 

For problems running RosettaMPNN please submit a github issue or submit your question [here](https://rosettacommons.org/contact/). 
