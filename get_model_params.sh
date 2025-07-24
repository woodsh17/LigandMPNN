#!/bin/bash

#make new directory for model parameters
#e.g.   bash get_model_params.sh "./model_params"

mkdir -p $1

#Original ProteinMPNN weights
wget -q https://files.ipd.uw.edu/pub/ligandmpnn/proteinmpnn_v_48_002.pt -O $1"/proteinmpnn_v_48_002.pt"
wget -q https://files.ipd.uw.edu/pub/ligandmpnn/proteinmpnn_v_48_010.pt -O $1"/proteinmpnn_v_48_010.pt"
wget -q https://files.ipd.uw.edu/pub/ligandmpnn/proteinmpnn_v_48_020.pt -O $1"/proteinmpnn_v_48_020.pt"
wget -q https://files.ipd.uw.edu/pub/ligandmpnn/proteinmpnn_v_48_030.pt -O $1"/proteinmpnn_v_48_030.pt"

#ProteinMPNN with num_edges=32
# wget -q https://files.ipd.uw.edu/pub/ligandmpnn/proteinmpnn_v_32_002.pt -O $1"/proteinmpnn_v_32_002.pt"
# wget -q https://files.ipd.uw.edu/pub/ligandmpnn/proteinmpnn_v_32_010.pt -O $1"/proteinmpnn_v_32_010.pt"
# wget -q https://files.ipd.uw.edu/pub/ligandmpnn/proteinmpnn_v_32_020.pt -O $1"/proteinmpnn_v_32_020.pt"
# wget -q https://files.ipd.uw.edu/pub/ligandmpnn/proteinmpnn_v_32_030.pt -O $1"/proteinmpnn_v_32_030.pt"

#LigandMPNN with num_edges=32; atom_context_num=25
wget -q https://files.ipd.uw.edu/pub/ligandmpnn/ligandmpnn_v_32_005_25.pt -O $1"/ligandmpnn_v_32_005_25.pt"
wget -q https://files.ipd.uw.edu/pub/ligandmpnn/ligandmpnn_v_32_010_25.pt -O $1"/ligandmpnn_v_32_010_25.pt"
wget -q https://files.ipd.uw.edu/pub/ligandmpnn/ligandmpnn_v_32_020_25.pt -O $1"/ligandmpnn_v_32_020_25.pt"
wget -q https://files.ipd.uw.edu/pub/ligandmpnn/ligandmpnn_v_32_030_25.pt -O $1"/ligandmpnn_v_32_030_25.pt"

#LigandMPNN with num_edges=32; atom_context_num=16
# wget -q https://files.ipd.uw.edu/pub/ligandmpnn/ligandmpnn_v_32_005_16.pt -O $1"/ligandmpnn_v_32_005_16.pt"
# wget -q https://files.ipd.uw.edu/pub/ligandmpnn/ligandmpnn_v_32_010_16.pt -O $1"/ligandmpnn_v_32_010_16.pt"
# wget -q https://files.ipd.uw.edu/pub/ligandmpnn/ligandmpnn_v_32_020_16.pt -O $1"/ligandmpnn_v_32_020_16.pt"
# wget -q https://files.ipd.uw.edu/pub/ligandmpnn/ligandmpnn_v_32_030_16.pt -O $1"/ligandmpnn_v_32_030_16.pt"

# wget -q https://files.ipd.uw.edu/pub/ligandmpnn/publication_version_ligandmpnn_v_32_010_25.pt -O $1"/publication_version_ligandmpnn_v_32_010_25.pt"

#Per residue label membrane ProteinMPNN
wget -q https://files.ipd.uw.edu/pub/ligandmpnn/per_residue_label_membrane_mpnn_v_48_020.pt -O $1"/per_residue_label_membrane_mpnn_v_48_020.pt"

#Global label membrane ProteinMPNN
wget -q https://files.ipd.uw.edu/pub/ligandmpnn/global_label_membrane_mpnn_v_48_020.pt -O $1"/global_label_membrane_mpnn_v_48_020.pt"

#SolubleMPNN
wget -q https://files.ipd.uw.edu/pub/ligandmpnn/solublempnn_v_48_002.pt -O $1"/solublempnn_v_48_002.pt"
wget -q https://files.ipd.uw.edu/pub/ligandmpnn/solublempnn_v_48_010.pt -O $1"/solublempnn_v_48_010.pt"
wget -q https://files.ipd.uw.edu/pub/ligandmpnn/solublempnn_v_48_020.pt -O $1"/solublempnn_v_48_020.pt"
wget -q https://files.ipd.uw.edu/pub/ligandmpnn/solublempnn_v_48_030.pt -O $1"/solublempnn_v_48_030.pt"

#LigandMPNN for side-chain packing (multi-step denoising model)
wget -q https://files.ipd.uw.edu/pub/ligandmpnn/ligandmpnn_sc_v_32_002_16.pt -O $1"/ligandmpnn_sc_v_32_002_16.pt"

#HypderMPNN for designing thermostable proteins learned from hyperthermophilic organisms with proteinmpnn model
wget -q https://raw.githubusercontent.com/meilerlab/HyperMPNN/1877ea181d23fe84fb33147748e1367e5a02b6a9/retrained_models/v48_002_epoch240_hyper.pt -O $1"/hypermpnn_v48_002_epoch240.pt"
wget -q https://raw.githubusercontent.com/meilerlab/HyperMPNN/1877ea181d23fe84fb33147748e1367e5a02b6a9/retrained_models/v48_010_epoch300_hyper.pt -O $1"/hypdermpnn_v48_010_epoch300.pt"
wget -q https://raw.githubusercontent.com/meilerlab/HyperMPNN/1877ea181d23fe84fb33147748e1367e5a02b6a9/retrained_models/v48_020_epoch300_hyper.pt -O $1"/hypermpnn_v48_020_epoch300.pt"
wget -q https://raw.githubusercontent.com/meilerlab/HyperMPNN/1877ea181d23fe84fb33147748e1367e5a02b6a9/retrained_models/v48_030_epoch300_hyper.pt -O $1"/hypermpnn_v48_030_epoch300.pt"
