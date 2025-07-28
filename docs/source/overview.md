# Overview

**RosettaMPNN** combines all of the capabilities of [ProteinMPNN](https://www.science.org/doi/10.1126/science.add2187), [LigandMPNN](https://www.biorxiv.org/content/10.1101/2023.12.22.573103v1.full), and [HyperMPNN](https://www.biorxiv.org/content/biorxiv/early/2024/12/01/2024.11.26.625397.full.pdf) into a single, Rosetta Commons-supported tool for protein sequence generation.

**ProteinMPNN** forms the basis for LigandMPNN, HyperMPNN, and now RosettaMPNN. It is a message-passing neural network that can generate protein sequences based on backbone structures. Due to its ability to couple amino acid sequences in different chains and awareness of symmetry, it can be used to design <span style='color:#F68A33'>monomers</span>, <span style='color:#F68A33'>cyclic oligomers</span>, <span style='color:#F68A33'>protein nanoparticles</span>, and <span style='color:#F68A33'>protein-protein interfaces</span>. We have also included the Multi-State design capabilities developed by the [Kuhlman Lab](https://github.com/Kuhlman-Lab/proteinmpnn/tree/main) to enable sequence design for multiple protein conformations. 

**LigandMPNN** extends the capabilities of ProteinMPNN to also be able to design protein sequences in the context of small molecules, nucleotides and metals. This allows for the design of <span style='color:#F68A33'>small molecule binding proteins</span>, <span style='color:#F68A33'>sensors</span>, and <span style='color:#F68A33'>enzymes</span>.

**HyperMPNN** uses ProteinMPNN’s model architecture and training algorithm, but includes proteins found in hyperthermophilic organisms to generate <span style='color:#F68A33'>highly thermostable proteins</span>. These proteins are incredibly useful for the creation of vaccines, protein nanoparticles for drug delivery, and industrial biocatalysts.

RosettaMPNN can be used in a workflow to design de novo proteins that combine backbone generation tools - such as [RFdiffusion](https://sites.google.com/omsf.io/rfdiffusion) - and 3D structure prediction tools - such as [AlphaFold2](https://github.com/google-deepmind/alphafold). 

