# RosettaMPNN

## Overview

### Description
**RosettaMPNN** is a community-driven repository for protein sequence design tools based on Message Passing Neural Networks (MPNNs). Starting from the [**LigandMPNN**](https://www.biorxiv.org/content/10.1101/2023.12.22.573103v1.full) infrastructure, this repository combines many of the MPNN-based tools developed by Rosetta Commons, including [**ProteinMPNN**](https://www.science.org/doi/10.1126/science.add2187) and [**HyperMPNN**](https://www.biorxiv.org/content/biorxiv/early/2024/12/01/2024.11.26.625397.full.pdf) to serve as a **centralized home for multiple MPNN-based sequence design tools**. <mark>If you would like your MPNN-based tool incorporated into this repository, reach out to [Hope Woods](mailto:hope.woods@omsf.io), the Rosetta Commons Technical Product Lead.</mark>

As one of the tools maintained by the Commons, the MPNN tools that compose RosettaMPPN have been refactored to create a single, unified interface with consistant usage patterns, infrastructure for code tests, and tests

This includes integrating and maintaining various *MPNN model variants—such as ProteinMPNN, LigandMPNN, HyperMPNN, and others—under a unified interface, with added features, consistent usage patterns, and tested workflows. By integrating these tools under a unified Python API and command-line interface, we aim to streamline development, ensure long-term maintenance, and foster collaboration across the protein design community.

RosettaMPNN is intended as an actively supported, evolving framework for MPNN-based protein design, allowing for flexible extensions to support new model variants, design protocols, and experimental use cases.

### What are Message Passing Neural Networks (MPNNs)?

MPNNs are a class of machine learning models that operate on graphs, making them ideal for modeling protein structures as networks of interacting atoms or residues. They have recently enabled state-of-the-art performance in protein design tasks.

### Key Publications

The following publications describe the underlying methods and models integrated in RosettaMPNN: 

- **[ProteinMPNN](https://github.com/dauparas/ProteinMPNN):** General protein backbone-based sequence design  
  [Science, 2023](https://doi.org/10.1126/science.add2187)
- **[LigandMPNN](https://github.com/dauparas/LigandMPNN):** Extends sequence design for protein-ligand complexes, while maintaining compatibility with ProteinMPNN models
  [Nature Methods, 2025](https://doi.org/10.1038/s41592-025-02626-1)
- **[HyperMPNN](https://github.com/meilerlab/HyperMPNN):** A set of weights that can be used with the ProteinMPNN model that generate highly thermostable protein sequences. 
  [bioRxiv, 2024](https://doi.org/10.1101/2024.11.26.625397)

---
## Table of Contents

- [Overview](#overview)
  - [Description](#description)
  - [Key Publications](#key-publications)
- [Getting Started](#getting-started)
  - [Installation Guide](#installation-guide)
  - [Docker image](#docker-image)
  - [Usage](#usage)
    - [Basic Use Case](#how-to-run-basic-use-case)
    - [Multi-State Design](#multi-state-design)
- [Developing](#developing)
  - [Testing](#testing)
- [Support & Help](#support--help)
- [License](#license)

---

## Features
- **Multiple MPNN model variants:** ProteinMPNN, LigandMPNN, HyperMPNN, and more
- **Unified Python API and CLI:** Consistent interface for scripting and command-line use
- **Flexible, extensible framework:** Add your own models or design protocols
- **Actively maintained:** Community contributions encouraged
- **Tested workflows:** Integration and unit tests, reproducible pipelines

---

## Getting Started

### Installation Guide

**1. Clone the repository:**
```
git clone https://github.com/woodsh17/RosettaMPNN.git
cd RosettaMPNN
```
**2. Download the model weights (includes weights for HyperMPNN):**
```
bash get_model_params.sh model_params
```

**3. Set up your Python environment and install (choose one of the following options):**

<details>
<summary><strong>Option A: Using Conda</strong></summary>

```
conda create -n rosettampnn python=3.11
conda activate rosettampnn
pip install -r requirements.txt
pip install -e .
```
(Optional but recommended) Add RosettaMPNN to your PYTHONPATH:
```
export PYTHONPATH=/PATH/TO/RosettaMPNN:$PYTHONPATH
```
Whenever you want to run RosettaMPNN, activate your environment:
```
conda activate rosettampnn
```
</details>

<details>
<summary><strong>Option B: Using <code>uv</code> and venv</strong></summary>

```
#create virtual environment with python3.11
uv venv --python=python3.11
source .venv/bin/activate
#if cuda is available
uv pip install -e .[cuda]
#if cuda is not available
uv pip install -e .
```
(Optional but recommended) Add RosettaMPNN to your PYTHONPATH:
```
export PYTHONPATH=/PATH/TO/RosettaMPNN:$PYTHONPATH
```
Whenever you want to run RosettaMPNN, activate your environment:
```
source .venv/bin/activate
```
If you do not have <code>uv</code> installed, run:
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```
</details>

### Docker image
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
If this runs successfully, you will have the same directories as before, with an additional `msd` directory where a pdb file (`msd.pdb`)that combines all pdb files listed in the input json file are combined into one pdb file and separated in space. There will be additional fasta files and PDB files in `seqs` and `backbones` directories for the different structures included in your input. 

**Using HyperMPNN Weights:** 
The retrained HyperMPNN weights were downloaded when you ran `get_model_params.sh`. You can use these weights with the `protein_mpnn` model option. This is not compatible with the `ligand_mpnn` model. 
```
python -m RosettaMPNN \
--out_folder ./out_hyper/ \
--pdb_path ~/RosettaMPNN/inputs/1BC8.pdb \
--model_type protein_mpnn \
--checkpoint_protein_mpnn ~/RosettaMPNN/model_params/hypermpnn_v48_020_epoch300.pt 
```

For more information on how to run RosettaMPNN and different options available see the [documentation]((https://woodsh17.github.io/RosettaMPNN/)). 

---
## Developing 

### Contributing
We welcome contributions to improve RosettaMPNN. We use a fork-and-PR system for contribution. To contribute to RosettaMPNN, please fork the RosettaMPNN repo under your own Github user space. You can then develop your additions in your own space. Once you're ready to contribute it back, open a PR agaist the main RosettaMPNN repo.

### Testing
- Unit and integration tests are provided in the `test/` directory.
- Run all tests locally with:
  ```
  pytest test/
  ```
- Continuous integration (CI) is planned for automated testing.

---

## Support & Help

You can find more detailed documentation on the [documentation site](https://woodsh17.github.io/RosettaMPNN/)

- Full documentation: [https://woodsh17.github.io/RosettaMPNN/](https://woodsh17.github.io/RosettaMPNN/)
- Open an issue for bugs or feature requests: [GitHub Issues](https://github.com/woodsh17/RosettaMPNN/issues)
- General questions: [RosettaCommons contact form](https://rosettacommons.org/contact/)

---

## License 
RosettaMPNN is released under the [MIT License](LICENSE).

---

## Citing RosettaMPNN

If you use RosettaMPNN in your work, please cite the relevant publications listed in [Key Publications](#key-publications)