# Model Weights
This pages contains the reference documentation for the different model weights available in RosettaMPNN
## Download Weights
To download model parameters run:
```
bash get_model_params.sh "./model_params"
```

## Available models

To run the model of your choice specify `--model_type` and optionally the model checkpoint path. If you do not specify a model checkpoint path then the default for that model will be used. 

Available models:

### ProteinMPNN

ProteinMPNN model is the original ProteinMPNN trained on the whole PDB excluding non-protein atoms

Specify with this option:
```
--model_type "protein_mpnn" #specify model
--checkpoint_protein_mpnn "/PATH/TO/WEIGHTS/WEIGHTS.pt" #specify weights
```
The default for `checkpoint_protein_mpnn` is `./model_params/proteinmpnn_v_48_020.pt`

Compatible weights for ProteinMPNN are: 
```
proteinmpnn_v_48_002.pt #noised with 0.02A Gaussian noise
proteinmpnn_v_48_010.pt #noised with 0.10A Gaussian noise
proteinmpnn_v_48_020.pt #noised with 0.20A Gaussian noise
proteinmpnn_v_48_030.pt #noised with 0.30A Gaussian noise
```
### HyperMPNN

HyperMPNN weights are used with the `protein_mpnn` model.

Specify with this option:
```
--model_type "protein_mpnn" #specify model
--checkpoint_protein_mpnn "/PATH/TO/WEIGHTS/HYPERMPNN_WEIGHTS.pt" #specify weights
```
Different HyperMPNN weights:
```
hypermpnn_v48_002_epoch240.pt #noised with 0.02A Gaussian noise
hypermpnn_v48_010_epoch300.pt #noised with 0.10A Gaussian noise
hypermpnn_v48_020_epoch300.pt #noised with 0.20A Gaussian noise 
hypermpnn_v48_030_epoch300.pt #noised with 0.30A Gaussian noise
```
An epoch is one complete pass through the entire training dataset during the training of a machine learning model.

### LigandMPNN

LigandMPNN model is an atomic context aware model trained with small molecules, nucleotides, metals etc on the whole PDB

Specify with this option:
```
--model_type "ligand_mpnn" #specify model
--checkpoint_ligand_mpnn "/PATH/TO/WEIGHTS/WEIGHTS.pt" #specify weights
```
The default for `checkpoint_ligand_mpnn` is `./model_params/ligandmpnn_v_32_010_25.pt`

Compatible weights for LigandMPNN are: 
```
ligandmpnn_v_32_005_25.pt #noised with 0.05A Gaussian noise
ligandmpnn_v_32_010_25.pt #noised with 0.10A Gaussian noise
ligandmpnn_v_32_020_25.pt #noised with 0.20A Gaussian noise
ligandmpnn_v_32_030_25.pt #noised with 0.30A Gaussian noise
```

### SolubleMPNN

SolubleMPNN is ProteinMPNN trained only on soluble PDB ids.

Specify with this option:
```
--model_type "soluble_mpnn" #specify model
--checkpoint_soluble_mpnn "/PATH/TO/WEIGHTS/WEIGHTS.pt" #specify weights
```
The default for `checkpoint_soluble_mpnn` is `./model_params/solublempnn_v_48_020.pt`

Compatible weights for SolubleMPNN are: 
```
solublempnn_v_48_002.pt" #noised with 0.02A Gaussian noise
solublempnn_v_48_010.pt" #noised with 0.10A Gaussian noise
solublempnn_v_48_020.pt" #noised with 0.20A Gaussian noise
solublempnn_v_48_030.pt" #noised with 0.30A Gaussian noise
```
### Global Label MembraneMPNN

ProteinMPNN model trained with global label per PDB id to specify if protein is transmembrane

Specify with this option:
```
--model_type "global_label_membrane_mpnn" #specify model
--checkpoint_global_label_membrane_mpnn "/PATH/TO/WEIGHTS/global_label_membrane_mpnn_v_48_020.pt" #specify weights
```
The default and only weights for `checkpoint_global_label_membrane_mpnn` is `./model_params/global_label_membrane_mpnn_v_48_020.pt`

### Per Residue Label MembraneMPNN

ProteinMPNN model trained with addition label per residue specifying if that residue is buried or exposed

Specify with this option:
```
--model_type "per_residue_label_membrane_mpnn"
--checkpoint_per_residue_label_membrane_mpnn "/PATH/TO/WEIGHTS/per_residue_label_membrane_mpnn_v_48_020.pt"
```
The default and only weights for `checkpoint_per_residue_label_membrane_mpnn` is `./model_params/per_residue_label_membrane_mpnn_v_48_020.pt`

### Side chain packing model

Weights used for repacking side chains. Should be used with `--pack_side_chains 1`. 

Specify with this option:
```
--checkpoint_path_sc "/PATH/TO/WEIGHTS/ligandmpnn_sc_v_32_002_16.pt"
```
The default and only weights for `--checkpoint_path_sc` is `./model_params/ligandmpnn_sc_v_32_002_16.pt`