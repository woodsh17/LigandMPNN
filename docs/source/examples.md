# Examples

Here are examples of how to use some of the different options available in RosettaMPNN. 

## Design 
### Default
Default settings will run ProteinMPNN.
```
python -m RosettaMPNN \
        --seed 111 \
        --pdb_path "./inputs/1BC8.pdb" \
        --out_folder "./outputs/default"
```
###  --temperature
`--temperature 0.05` Change sampling temperature (higher temperature gives more sequence diversity).
```
python -m RosettaMPNN \
        --seed 111 \
        --pdb_path "./inputs/1BC8.pdb" \
        --temperature 0.05 \
        --out_folder "./outputs/temperature"
```
### --seed
`--seed` Not selecting a seed will run with a random seed. Running this multiple times will give different results.
```
python -m RosettaMPNN \
        --pdb_path "./inputs/1BC8.pdb" \
        --out_folder "./outputs/random_seed"
```
### --verbose
`--verbose 0` Do not print any statements.
```
python -m RosettaMPNN \
        --seed 111 \
        --verbose 0 \
        --pdb_path "./inputs/1BC8.pdb" \
        --out_folder "./outputs/verbose"
```
### --save_stats
`--save_stats 1` Save sequence design statistics.
```
#['generated_sequences', 'sampling_probs', 'log_probs', 'decoding_order', 'native_sequence', 'mask', 'chain_mask', 'seed', 'temperature']
python -m RosettaMPNN \
        --seed 111 \
        --pdb_path "./inputs/1BC8.pdb" \
        --out_folder "./outputs/save_stats" \
        --save_stats 1
```
### --fixed_residues
`--fixed_residues` Fixing specific amino acids. This example fixes the first 10 residues in chain C and adds global bias towards A (alanine). The output should have all alanines except the first 10 residues should be the same as in the input sequence since those are fixed.
```
python -m RosettaMPNN \
        --seed 111 \
        --pdb_path "./inputs/1BC8.pdb" \
        --out_folder "./outputs/fix_residues" \
        --fixed_residues "C1 C2 C3 C4 C5 C6 C7 C8 C9 C10" \
        --bias_AA "A:10.0"
```

### --redesigned_residues
`--redesigned_residues` Specifying which residues need to be designed. This example redesigns the first 10 residues while fixing everything else.
```
python -m RosettaMPNN \
        --seed 111 \
        --pdb_path "./inputs/1BC8.pdb" \
        --out_folder "./outputs/redesign_residues" \
        --redesigned_residues "C1 C2 C3 C4 C5 C6 C7 C8 C9 C10" \
        --bias_AA "A:10.0"
```

### --number_of_batches
Design 15 sequences; with batch size 3 (can be 1 when using CPUs) and the number of batches 5.
```
python -m RosettaMPNN \
        --seed 111 \
        --pdb_path "./inputs/1BC8.pdb" \
        --out_folder "./outputs/batch_size" \
        --batch_size 3 \
        --number_of_batches 5
```
### --bias_AA
Global amino acid bias. In this example, output sequences are biased towards W, P, C and away from A.
```
python -m RosettaMPNN \
        --seed 111 \
        --pdb_path "./inputs/1BC8.pdb" \
        --bias_AA "W:3.0,P:3.0,C:3.0,A:-3.0" \
        --out_folder "./outputs/global_bias"
```

### --bias_AA_per_residue
Specify per residue amino acid bias, e.g. make residues C1, C3, C5, and C7 to be prolines.
```
# {
# "C1": {"G": -0.3, "C": -2.0, "P": 10.8},
# "C3": {"P": 10.0},
# "C5": {"G": -1.3, "P": 10.0},
# "C7": {"G": -1.3, "P": 10.0}
# }
python -m RosettaMPNN \
        --seed 111 \
        --pdb_path "./inputs/1BC8.pdb" \
        --bias_AA_per_residue "./inputs/bias_AA_per_residue.json" \
        --out_folder "./outputs/per_residue_bias"
```
### --omit_AA
Global amino acid restrictions. This is equivalent to using `--bias_AA` and setting bias to be a large negative number. The output should be just made of E, K, A.
```
python -m RosettaMPNN \
        --seed 111 \
        --pdb_path "./inputs/1BC8.pdb" \
        --omit_AA "CDFGHILMNPQRSTVWY" \
        --out_folder "./outputs/global_omit"
```

### --omit_AA_per_residue
Per residue amino acid restrictions.
```
# {
# "C1": "ACDEFGHIKLMNPQRSTVW",
# "C3": "ACDEFGHIKLMNPQRSTVW",
# "C5": "ACDEFGHIKLMNPQRSTVW",
# "C7": "ACDEFGHIKLMNPQRSTVW"
# }
python -m RosettaMPNN \
        --seed 111 \
        --pdb_path "./inputs/1BC8.pdb" \
        --omit_AA_per_residue "./inputs/omit_AA_per_residue.json" \
        --out_folder "./outputs/per_residue_omit"
```

### --symmetry_residues, --symmetry_weights
Designing sequences with symmetry, e.g. homooligomer/2-state proteins, etc. In this example make C1=C2=C3, also C4=C5, and C6=C7.
```
#total_logits += symmetry_weights[t]*logits
#probs = torch.nn.functional.softmax((total_logits+bias_t) / temperature, dim=-1)
#total_logits_123 = 0.33*logits_1+0.33*logits_2+0.33*logits_3
#output should be ***ooxx
python -m RosettaMPNN \
        --seed 111 \
        --pdb_path "./inputs/1BC8.pdb" \
        --out_folder "./outputs/symmetry" \
        --symmetry_residues "C1,C2,C3|C4,C5|C6,C7" \
        --symmetry_weights "0.33,0.33,0.33|0.5,0.5|0.5,0.5"
```

### --homo_oligomer
Design homooligomer sequences. This automatically sets `--symmetry_residues` and `--symmetry_weights` assuming equal weighting from all chains.
```
python -m RosettaMPNN \
        --model_type "ligand_mpnn" \
        --seed 111 \
        --pdb_path "./inputs/4GYT.pdb" \
        --out_folder "./outputs/homooligomer" \
        --homo_oligomer 1 \
        --number_of_batches 2
```

### --file_ending
Outputs will have a specified ending; e.g. `1BC8_xyz.fa` instead of `1BC8.fa`
```
python -m RosettaMPNN \
        --seed 111 \
        --pdb_path "./inputs/1BC8.pdb" \
        --out_folder "./outputs/file_ending" \
        --file_ending "_xyz"
```

### --zero_indexed
Zero indexed names in /backbones/1BC8_0.pdb, 1BC8_1.pdb, 1BC8_2.pdb etc
```
python -m RosettaMPNN \
        --seed 111 \
        --pdb_path "./inputs/1BC8.pdb" \
        --out_folder "./outputs/zero_indexed" \
        --zero_indexed 1 \
        --number_of_batches 2
```

### --chains_to_design
Specify which chains (e.g. "A,B,C") need to be redesigned, other chains will be kept fixed. Outputs in seqs/backbones will still have atoms/sequences for the whole input PDB.
```
python -m RosettaMPNN \
        --model_type "ligand_mpnn" \
        --seed 111 \
        --pdb_path "./inputs/4GYT.pdb" \
        --out_folder "./outputs/chains_to_design" \
        --chains_to_design "A,B"
```

###  --parse_these_chains_only
Parse and design only specified chains (e.g. "A,B,C"). Outputs will have only specified chains.
```
python -m RosettaMPNN \
        --model_type "ligand_mpnn" \
        --seed 111 \
        --pdb_path "./inputs/4GYT.pdb" \
        --out_folder "./outputs/parse_these_chains_only" \
        --parse_these_chains_only "A,B"
```

### --model_type "ligand_mpnn"
Run LigandMPNN with default settings.
```
python -m RosettaMPNN \
        --model_type "ligand_mpnn" \
        --seed 111 \
        --pdb_path "./inputs/1BC8.pdb" \
        --out_folder "./outputs/ligandmpnn_default"
```

### --checkpoint_ligand_mpnn
Run LigandMPNN using 0.05A model by specifying `--checkpoint_ligand_mpnn` flag.
```
python -m RosettaMPNN \
        --checkpoint_ligand_mpnn "./model_params/ligandmpnn_v_32_005_25.pt" \
        --model_type "ligand_mpnn" \
        --seed 111 \
        --pdb_path "./inputs/1BC8.pdb" \
        --out_folder "./outputs/ligandmpnn_v_32_005_25"
```
### --ligand_mpnn_use_atom_context
Setting `--ligand_mpnn_use_atom_context 0` will mask all ligand atoms. This can be used to assess how much ligand atoms affect AA probabilities.
```
python -m RosettaMPNN \
        --model_type "ligand_mpnn" \
        --seed 111 \
        --pdb_path "./inputs/1BC8.pdb" \
        --out_folder "./outputs/ligandmpnn_no_context" \
        --ligand_mpnn_use_atom_context 0
```

### --ligand_mpnn_use_side_chain_context
Use fixed residue side chain atoms as extra ligand atoms.
```
python -m RosettaMPNN \
        --model_type "ligand_mpnn" \
        --seed 111 \
        --pdb_path "./inputs/1BC8.pdb" \
        --out_folder "./outputs/ligandmpnn_use_side_chain_atoms" \
        --ligand_mpnn_use_side_chain_context 1 \
        --fixed_residues "C1 C2 C3 C4 C5 C6 C7 C8 C9 C10"
```

### --model_type "soluble_mpnn"
Run SolubleMPNN (ProteinMPNN-like model with only soluble proteins in the training dataset).
```
python -m RosettaMPNN \
        --model_type "soluble_mpnn" \
        --seed 111 \
        --pdb_path "./inputs/1BC8.pdb" \
        --out_folder "./outputs/soluble_mpnn_default"
```

### --model_type "global_label_membrane_mpnn"
Run global label membrane MPNN (trained with extra input - binary label soluble vs not) `--global_transmembrane_label #1 - membrane, 0 - soluble`.
```
python -m RosettaMPNN \
        --model_type "global_label_membrane_mpnn" \
        --seed 111 \
        --pdb_path "./inputs/1BC8.pdb" \
        --out_folder "./outputs/global_label_membrane_mpnn_0" \
        --global_transmembrane_label 0
```

### --model_type "per_residue_label_membrane_mpnn"
Run per residue label membrane MPNN (trained with extra input per residue specifying buried (hydrophobic), interface (polar), or other type residues; 3 classes).
```
python -m RosettaMPNN \
        --model_type "per_residue_label_membrane_mpnn" \
        --seed 111 \
        --pdb_path "./inputs/1BC8.pdb" \
        --out_folder "./outputs/per_residue_label_membrane_mpnn_default" \
        --transmembrane_buried "C1 C2 C3 C11" \
        --transmembrane_interface "C4 C5 C6 C22"
```

### HyperMPNN weights
Run ProteinMPNN with HyperMPNN weights
```
python -m RosettaMPNN \
        --out_folder "./test/integration/outputs/hyper" \
        --pdb_path "./inputs/1BC8.pdb" \
        --model_type "protein_mpnn" \
        --checkpoint_protein_mpnn "model_params/hypermpnn_v48_020_epoch300.pt" \
```

### --fasta_seq_separation
Choose a symbol to put between different chains in fasta output format. It's recommended to PDB output format to deal with residue jumps and multiple chain parsing.
```
python -m RosettaMPNN \
        --pdb_path "./inputs/1BC8.pdb" \
        --out_folder "./outputs/fasta_seq_separation" \
        --fasta_seq_separation ":"
```

### --pdb_path_multi
Specify multiple PDB input paths. This is more efficient since the model needs to be loaded from the checkpoint once.
```
#{
#"./inputs/1BC8.pdb": "",
#"./inputs/4GYT.pdb": ""
#}
python -m RosettaMPNN \
        --pdb_path_multi "./inputs/pdb_ids.json" \
        --out_folder "./outputs/pdb_path_multi" \
        --seed 111
```

###  --fixed_residues_multi
Specify fixed residues when using `--pdb_path_multi` flag.
```
#{
#"./inputs/1BC8.pdb": "C1 C2 C3 C4 C5 C10 C22",
#"./inputs/4GYT.pdb": "A7 A8 A9 A10 A11 A12 A13 B38"
#}
python -m RosettaMPNN \
        --pdb_path_multi "./inputs/pdb_ids.json" \
        --fixed_residues_multi "./inputs/fix_residues_multi.json" \
        --out_folder "./outputs/fixed_residues_multi" \
        --seed 111
```

### --redesigned_residues_multi
Specify which residues need to be redesigned when using `--pdb_path_multi` flag.
```
#{
#"./inputs/1BC8.pdb": "C1 C2 C3 C4 C5 C10",
#"./inputs/4GYT.pdb": "A7 A8 A9 A10 A12 A13 B38"
#}
python -m RosettaMPNN \
        --pdb_path_multi "./inputs/pdb_ids.json" \
        --redesigned_residues_multi "./inputs/redesigned_residues_multi.json" \
        --out_folder "./outputs/redesigned_residues_multi" \
        --seed 111
```

### --omit_AA_per_residue_multi
Specify which residues need to be omitted when using `--pdb_path_multi` flag.
```
#{
#"./inputs/1BC8.pdb": {"C1":"ACDEFGHILMNPQRSTVWY", "C2":"ACDEFGHILMNPQRSTVWY", "C3":"ACDEFGHILMNPQRSTVWY"},
#"./inputs/4GYT.pdb": {"A7":"ACDEFGHILMNPQRSTVWY", "A8":"ACDEFGHILMNPQRSTVWY"}
#}
python -m RosettaMPNN \
        --pdb_path_multi "./inputs/pdb_ids.json" \
        --omit_AA_per_residue_multi "./inputs/omit_AA_per_residue_multi.json" \
        --out_folder "./outputs/omit_AA_per_residue_multi" \
        --seed 111
```

### --bias_AA_per_residue_multi
Specify amino acid biases per residue when using `--pdb_path_multi` flag.
```
#{
#"./inputs/1BC8.pdb": {"C1":{"A":3.0, "P":-2.0}, "C2":{"W":10.0, "G":-0.43}},
#"./inputs/4GYT.pdb": {"A7":{"Y":5.0, "S":-2.0}, "A8":{"M":3.9, "G":-0.43}}
#}
python -m RosettaMPNN \
        --pdb_path_multi "./inputs/pdb_ids.json" \
        --bias_AA_per_residue_multi "./inputs/bias_AA_per_residue_multi.json" \
        --out_folder "./outputs/bias_AA_per_residue_multi" \
        --seed 111
```

### --ligand_mpnn_cutoff_for_score
This sets the cutoff distance in angstroms to select residues that are considered to be close to ligand atoms. This flag only affects the `num_ligand_res` and `ligand_confidence` in the output fasta files.
```
python -m RosettaMPNN \
        --model_type "ligand_mpnn" \
        --seed 111 \
        --pdb_path "./inputs/1BC8.pdb" \
        --ligand_mpnn_cutoff_for_score "6.0" \
        --out_folder "./outputs/ligand_mpnn_cutoff_for_score"
```

### Specifying residues with insertion codes
You can specify residue using chain_id + residue_number + insersion_code; e.g. redesign only residue B82, B82A, B82B, B82C.
```
python -m RosettaMPNN \
        --seed 111 \
        --pdb_path "./inputs/2GFB.pdb" \
        --out_folder "./outputs/insertion_code" \
        --redesigned_residues "B82 B82A B82B B82C" \
        --parse_these_chains_only "B"
```

### Parse atoms with zero occupancy
Parse atoms in the PDB files with zero occupancy too.
```
python -m RosettaMPNN \
        --model_type "ligand_mpnn" \
        --seed 111 \
        --pdb_path "./inputs/1BC8.pdb" \
        --out_folder "./outputs/parse_atoms_with_zero_occupancy" \
        --parse_atoms_with_zero_occupancy 1
```
### Multi-State Design - single constraint
Design single chain for multiple states. Each state is comma separated, each state consist of PDB_name:Start_residue-Stop_residue:Weight. Residues should be specified with the chain ID followed by the residue number. 
```
python -m RosettaMPNN \
        --out_folder ./outputs/msd_single/ \
        --multi_state_pdb_path ./inputs/msd_pdbs.json \
        --multi_state_constraints 4GYT_dimer:A7-A183:0.5,4GYT_dimer:B7-B183:0.5,4GYT_monomer:A7-A183:1 \
```

### Multi-State Design - multiple constraints
Design multiple chains with multiple states. Each constraint is separated by a ";". Within each constraint the states are specified following the same format as above. Negative weights can be used for negative design. 
```
python -m RosettaMPNN \
        --out_folder ./outputs/msd_single/ \
        --multi_state_pdb_path ./inputs/msd_multi_constraint_pdbs.json \
        --multi_state_constraints 1a0o:A1-A128:1,1a0o_chainA_monomer:A1-A128:1;1a0o:B1-B70:1,1a0o_chainB_monomer:B1-B70:-1 \
```

## Scoring examples
### Autoregressive with sequence info
Get probabilities/scores for backbone-sequence pairs using autoregressive probabilities: p(AA_1|backbone), p(AA_2|backbone, AA_1) etc. These probabilities will depend on the decoding order, so it's recomended to set number_of_batches to at least 10.
```
python score.py \
        --model_type "ligand_mpnn" \
        --seed 111 \
        --autoregressive_score 1\
        --pdb_path "./outputs/ligandmpnn_default/backbones/1BC8_1.pdb" \
        --out_folder "./outputs/autoregressive_score_w_seq" \
        --use_sequence 1\
        --batch_size 1 \
        --number_of_batches 10
```

### Autoregressive with backbone info only
Get probabilities/scores for backbone using probabilities: p(AA_1|backbone), p(AA_2|backbone) etc. These probabilities will depend on the decoding order, so it's recomended to set number_of_batches to at least 10.
```
python score.py \
        --model_type "ligand_mpnn" \
        --seed 111 \
        --autoregressive_score 1\
        --pdb_path "./outputs/ligandmpnn_default/backbones/1BC8_1.pdb" \
        --out_folder "./outputs/autoregressive_score_wo_seq" \
        --use_sequence 0\
        --batch_size 1 \
        --number_of_batches 10
```

### Single amino acid score with sequence info
Get probabilities/scores for backbone-sequence pairs using single aa probabilities: p(AA_1|backbone, AA_{all except AA_1}), p(AA_2|backbone, AA_{all except AA_2}) etc. These probabilities will depend on the decoding order, so it's recomended to set number_of_batches to at least 10.
```
python score.py \
        --model_type "ligand_mpnn" \
        --seed 111 \
        --single_aa_score 1\
        --pdb_path "./outputs/ligandmpnn_default/backbones/1BC8_1.pdb" \
        --out_folder "./outputs/single_aa_score_w_seq" \
        --use_sequence 1\
        --batch_size 1 \
        --number_of_batches 10
```

### Single amino acid score with backbone info only
Get probabilities/scores for backbone-sequence pairs using single aa probabilities: p(AA_1|backbone), p(AA_2|backbone) etc. These probabilities will depend on the decoding order, so it's recomended to set number_of_batches to at least 10.
```
python score.py \
        --model_type "ligand_mpnn" \
        --seed 111 \
        --single_aa_score 1\
        --pdb_path "./outputs/ligandmpnn_default/backbones/1BC8_1.pdb" \
        --out_folder "./outputs/single_aa_score_wo_seq" \
        --use_sequence 0\
        --batch_size 1 \
        --number_of_batches 10
```

## Side chain packing examples

### Design a new sequence and pack side chains (return 1 side chain packing sample - fast)
Design a new sequence using any of the available models and also pack side chains of the new sequence. Return only a single solution for the side chain packing.
```
python -m RosettaMPNN \
        --model_type "ligand_mpnn" \
        --seed 111 \
        --pdb_path "./inputs/1BC8.pdb" \
        --out_folder "./outputs/sc_default_fast" \
        --pack_side_chains 1 \
        --number_of_packs_per_design 0 \
        --pack_with_ligand_context 1
```

### Design a new sequence and pack side chains (return 4 side chain packing samples)
Same as above, but returns 4 independent samples for side chains. b-factor shows log prob density per chi angle group.
```
python -m RosettaMPNN \
        --model_type "ligand_mpnn" \
        --seed 111 \
        --pdb_path "./inputs/1BC8.pdb" \
        --out_folder "./outputs/sc_default" \
        --pack_side_chains 1 \
        --number_of_packs_per_design 4 \
        --pack_with_ligand_context 1
```

### Fix specific residues fors sequence design and packing
This option will not repack side chains of the fixed residues, but use them as a context.
```
python -m RosettaMPNN \
        --model_type "ligand_mpnn" \
        --seed 111 \
        --pdb_path "./inputs/1BC8.pdb" \
        --out_folder "./outputs/sc_fixed_residues" \
        --pack_side_chains 1 \
        --number_of_packs_per_design 4 \
        --pack_with_ligand_context 1 \
        --fixed_residues "C6 C7 C8 C9 C10 C11 C12 C13 C14 C15" \
        --repack_everything 0
```

### Fix specific residues for sequence design but repack everything
This option will repacks all the residues.
```
python -m RosettaMPNN \
        --model_type "ligand_mpnn" \
        --seed 111 \
        --pdb_path "./inputs/1BC8.pdb" \
        --out_folder "./outputs/sc_fixed_residues_full_repack" \
        --pack_side_chains 1 \
        --number_of_packs_per_design 4 \
        --pack_with_ligand_context 1 \
        --fixed_residues "C6 C7 C8 C9 C10 C11 C12 C13 C14 C15" \
        --repack_everything 1
```

### Design a new sequence using LigandMPNN but pack side chains without considering ligand/DNA etc atoms
You can run side chain packing without taking into account context atoms like DNA atoms. This most likely will results in side chain clashing with context atoms, but it might be interesting to see how model's uncertainty changes when ligand atoms are present vs not for side chain conformations.
```
python -m RosettaMPNN \
        --model_type "ligand_mpnn" \
        --seed 111 \
        --pdb_path "./inputs/1BC8.pdb" \
        --out_folder "./outputs/sc_no_context" \
        --pack_side_chains 1 \
        --number_of_packs_per_design 4 \
        --pack_with_ligand_context 0
```
