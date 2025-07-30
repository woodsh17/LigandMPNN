# RosettaMPNN

## Overview

### Description
**RosettaMPNN** is a community-driven repository for protein sequence design tools based on Message Passing Neural Networks (MPNNs). Starting from the [**LigandMPNN**](https://www.biorxiv.org/content/10.1101/2023.12.22.573103v1.full) infrastructure, this repository combines many of the MPNN-based tools developed by Rosetta Commons, including [**ProteinMPNN**](https://www.science.org/doi/10.1126/science.add2187) and [**HyperMPNN**](https://www.biorxiv.org/content/biorxiv/early/2024/12/01/2024.11.26.625397.full.pdf) to serve as a **centralized home for MPNN-based sequence design tools**. <mark>If you would like your MPNN-based tool incorporated into this repository, create a pull request or reach out to [Hope Woods](mailto:hope.woods@omsf.io), the Rosetta Commons Technical Product Lead.</mark>

As one of the tools maintained by Rosetta Commons, the MPNN tools that compose RosettaMPPN have been refactored to create a single, unified Python API and command-line interface. This, along with the creation of unit and integration test infrastructure, will streamline development of RosettaMPNN, facilitate long-term maintenance, and promote collaboration between contributors.


### What MPNN tools are currently included? 
- **ProteinMPNN**: The original MPNN tool that can couple amino acid sequences in different chains and is symmetry aware. It can be used to design <span style='color:#F68A33'>monomers</span>, <span style='color:#F68A33'>cyclic oligomers</span>, <span style='color:#F68A33'>protein nanoparticles</span>, and <span style='color:#F68A33'>protein-protein interfaces</span>.
- **LigandMPNN**: Extends the capabilities of ProteinMPNN to also be able to design protein sequences in the context of small molecules, nucleotides and metals. This allows for the design of <span style='color:#F68A33'>small molecule binding proteins</span>, <span style='color:#F68A33'>sensors</span>, and <span style='color:#F68A33'>enzymes</span>.
- **HyperMPNN**: Adds a new model to construct <span style='color:#F68A33'>highly thermostable proteins</span>. These proteins are incredibly useful for the creation of vaccines, protein nanoparticles for drug delivery, and industrial biocatalysts. For more information on how this model was trained please see the [HyperMPNN github page](https://github.com/meilerlab/HyperMPNN).
- **Multistate Design**: Enables sequence design for multiple protein conformations at once, improving protein flexibility and resulting in more realistic protein structures.

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
- [Features](#features)
- [Getting Started](#getting-started)
  - [Installation Guide](#installation-guide)
  - [Docker Image](#docker-image)
- [Examples](#examples)
  - [Basic Use Case](#basic-use-case)
  - [Multi-State Design](#multi-state-design)
  - [HyperMPNN Example](#hypermpnn-example)
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
#create virtual environment with python 3.11
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
If you do not have `uv` installed, run:
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```
</details>

### Docker image
_Docker image coming soon_

## Examples

### Basic Use Case
<details>

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
--checkpoint_protein_mpnn ~/RosettaMPNN/model_params/proteinmpnn_v_48_020.pt 
```
**Expected outputs:**
- `seqs/`: Designed sequence as `1BC8.fa`
- `backbones/`: Output structure with predicted sequence as `1BC8.pdb`
- `packed/`: (empty unless side-chain packing is specified)

</details>

### Multi-State Design
<details>

> ⚠️ **Experimental Feature**: The multi-state implementation is not yet scientifically validated. Use with caution.

Multi-state design allows you to design sequences compatible with multiple structures or states.  
Originally implemented by the Kuhlman lab ([GitHub](https://github.com/Kuhlman-Lab/proteinmpnn)).

**Flags explained:**
- `--multi_state_pdb_path`: Path to a JSON file listing the PDBs to be included 
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

### HyperMPNN Example
<details>

The retrained HyperMPNN weights were downloaded when you ran `get_model_params.sh`. You can use these weights with the `protein_mpnn` model option. These weights are **not compatible** with the `ligand_mpnn` model. 

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
We welcome contributions to improve RosettaMPNN. We use a fork-and-PR system for contribution. To contribute to RosettaMPNN, please fork the RosettaMPNN repo under your own GitHub user space. You can then develop your additions in your own space. Once you're ready to contribute it back, open a PR against the main RosettaMPNN repo.

### Testing
- Unit and integration tests are located in the `test/` directory.
- To run tests locally, use:
  ```
  pytest test/
  ```
- Continuous integration (CI) is set up with GitHub Actions to automatically run all unit and integration tests for pull requests targeting the `main` branch.
- Please ensure that you add appropriate tests for any new code contributed to the repository.

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
