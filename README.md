# RosettaMPNN

## Overview

### Description
**RosettaMPNN** is a community-driven repository for protein sequence design tools based on Message Passing Neural Networks (MPNNs), developed and used within the [RosettaCommons](https://www.rosettacommons.org/). The repository is intended for computational biologists, protein engineers, machine learning researchers, and experimentalists interested in applying state-of-the-art AI methods to protein design—regardless of prior familiarity with Rosetta software.

RosettaMPNN builds upon earlier tools like [LigandMPNN](https://github.com/dauparas/LigandMPNN), but aims to serve as a **centralized home for multiple MPNN-based sequence design tools**. 

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
  - [What are Message Passing Neural Networks (MPNNs)?](#what-are-message-passing-neural-networks-mpnns)
  - [Key Publications](#key-publications)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Installation Guide](#installation-guide)
  - [Docker image](#docker-image)
- [Examples](#examples)
  - Basic Use Case
  - Multi-State Design
  - Using HyperMPNN Weights
- [Developing](#developing)
  - [Contributing](#contributing)
  - [Testing](#testing)
- [Support & Help](#support--help)
- [License](#license)
- [Citing RosettaMPNN](#citing-rosettampnn)

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

## Examples

<details>
<summary><strong>Basic Use Case</strong></summary>

For this example we will use 1BC8.pdb from the example inputs.
**Flags explained:**
- `--out_folder`: Output directory for results
- `--pdb_path`: Input structure in PDB format
- `--checkpoint_protein_mpnn`: Path to model weights, necessary if you are not running inside RosettaMPNN

**Example Command Line**
```
python -m RosettaMPNN \
--out_folder ./out/ \
--pdb_path ~/RosettaMPNN/inputs/1BC8.pdb \
--checkpoint_protein_mpnn ~/RosettaMPNN/model_params/ proteinmpnn_v_48_020.pt 
```
**Expected outputs:**
- `seqs/`: Designed sequence as `1BC8.fa`
- `backbones/`: Output structure with predicted sequence as `1BC8.pdb`
- `packed/`: (empty unless side-chain packing is specified)

</details>

<details>
<summary><strong>Multi-State Design</strong></summary>

> ⚠️ **Experimental Feature**: The multi-state implementation is not yet scientifically validated. Use with caution.

Multi-state design allows you to design sequences compatible with multiple structures or states.  
Originally implemented by the Kuhlman lab ([GitHub](https://github.com/Kuhlman-Lab/proteinmpnn)).

**Flags explained:**
- `--multi_state_pdb_path`: Path to a json file listing the PDBS to be included 
- `--multi_state_constraints`: Semicolon-separated list of multi-state design constraints, commas separate individual residue sets within a constraint

**Example Command Line**
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
Same as basic use case, plus:
- `msd/`: Combined multi-state structure as `msd.pdb`
- Extra FASTA/PDB files for each input structure

</details>

<details>
<summary><strong>Using HyperMPNN Weights</strong></summary>

The retrained HyperMPNN weights were downloaded when you ran `get_model_params.sh`. You can use these weights with the `protein_mpnn` model option. This is **not compatible** with the `ligand_mpnn` model. 

**Example Command Line**
```
python -m RosettaMPNN \
--out_folder ./out_hyper/ \
--pdb_path ~/RosettaMPNN/inputs/1BC8.pdb \
--model_type protein_mpnn \
--checkpoint_protein_mpnn ~/RosettaMPNN/model_params/hypermpnn_v48_020_epoch300.pt 
```
</details>

**For more information on how to run RosettaMPNN and different options available see the [documentation](https://woodsh17.github.io/RosettaMPNN/).** 

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