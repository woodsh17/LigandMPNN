import argparse

def get_argparser(
        include_main_args=True,
        include_score_args=False,
):
    """
    Constructs and returns an argument parser for LigandMPNN. 

    This parser includes a comprehensive set of arguments for controlling model type,
    checkpoint paths, sequence design options, input/output specifications, symmetry constraints, 
    ligand context usage, transmembrane settings, and optional side chain packing and scoring routines. 

    Parameters: 
        include_main_args (bool): If True, includes arguments specific to the main design and packing
            functionality (e.g., packing options, amino acid biasing, temperature, etc.).
        include_score_args (bool): If True, includes arguments specific to scoring functionalities
            (e.g., autoregressive or single-AA scoring).

    Returns:
        argparse.ArgumentParser: Configured argument parser.
    """
    argparser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    # Arguments always included 
    argparser.add_argument(
        "--model_type",
        type=str,
        default="protein_mpnn",
        help="Choose your model: protein_mpnn, ligand_mpnn, per_residue_label_membrane_mpnn, global_label_membrane_mpnn, soluble_mpnn",
    )
    # protein_mpnn - original ProteinMPNN trained on the whole PDB exluding non-protein atoms
    # ligand_mpnn - atomic context aware model trained with small molecules, nucleotides, metals etc on the whole PDB
    # per_residue_label_membrane_mpnn - ProteinMPNN model trained with addition label per residue specifying if that residue is buried or exposed
    # global_label_membrane_mpnn - ProteinMPNN model trained with global label per PDB id to specify if protein is transmembrane
    # soluble_mpnn - ProteinMPNN trained only on soluble PDB ids
    argparser.add_argument(
        "--checkpoint_protein_mpnn",
        type=str,
        default="./model_params/proteinmpnn_v_48_020.pt",
        help="Path to model weights.",
    )
    argparser.add_argument(
        "--checkpoint_ligand_mpnn",
        type=str,
        default="./model_params/ligandmpnn_v_32_010_25.pt",
        help="Path to model weights.",
    )
    argparser.add_argument(
        "--checkpoint_per_residue_label_membrane_mpnn",
        type=str,
        default="./model_params/per_residue_label_membrane_mpnn_v_48_020.pt",
        help="Path to model weights.",
    )
    argparser.add_argument(
        "--checkpoint_global_label_membrane_mpnn",
        type=str,
        default="./model_params/global_label_membrane_mpnn_v_48_020.pt",
        help="Path to model weights.",
    )
    argparser.add_argument(
        "--checkpoint_soluble_mpnn",
        type=str,
        default="./model_params/solublempnn_v_48_020.pt",
        help="Path to model weights.",
    )

    argparser.add_argument(
        "--fasta_seq_separation",
        type=str,
        default=":",
        help="Symbol to use between sequences from different chains",
    )
    argparser.add_argument("--verbose", type=int, default=1, help="Print stuff")

    argparser.add_argument(
        "--pdb_path", type=str, default="", help="Path to the input PDB."
    )
    argparser.add_argument(
        "--pdb_path_multi",
        type=str,
        default="",
        help="Path to json listing PDB paths. {'/path/to/pdb': ''} - only keys will be used.",
    )
    argparser.add_argument(
        "--multi_state_pdb_path",
        type=str,
        default="",
        help="Path to json listing PDB paths of pdbs to be included in multi-state design.",
    )
    argparser.add_argument(
        "--multi_state_constraints",
        type=str,
        default="",
        help="Semicolon-separated list of multi-state design constraints. "
        "commas separate individual residue sets within a constraint. "
        "E.g. PDB1:A10-A15:1,PDB2:A10-A15:0.5;PDB1:A20-A25:1,PDB3:B20-B25:-1",
    )
    argparser.add_argument(
        "--fixed_residues",
        type=str,
        default="",
        help="Provide fixed residues, A12 A13 A14 B2 B25",
    )
    argparser.add_argument(
        "--fixed_residues_multi",
        type=str,
        default="",
        help="Path to json mapping of fixed residues for each pdb i.e., {'/path/to/pdb': 'A12 A13 A14 B2 B25'}",
    )

    argparser.add_argument(
        "--redesigned_residues",
        type=str,
        default="",
        help="Provide to be redesigned residues, everything else will be fixed, A12 A13 A14 B2 B25",
    )
    argparser.add_argument(
        "--redesigned_residues_multi",
        type=str,
        default="",
        help="Path to json mapping of redesigned residues for each pdb i.e., {'/path/to/pdb': 'A12 A13 A14 B2 B25'}",
    )
    argparser.add_argument(
        "--symmetry_residues",
        type=str,
        default="",
        help="Add list of lists for which residues need to be symmetric, e.g. 'A12,A13,A14|C2,C3|A5,B6'",
    )
    argparser.add_argument(
        "--homo_oligomer",
        type=int,
        default=0,
        help="Setting this to 1 will automatically set --symmetry_residues and --symmetry_weights to do homooligomer design with equal weighting.",
    )

    argparser.add_argument(
        "--out_folder",
        type=str,
        help="Path to a folder to output, e.g. /home/out/",
    )
    argparser.add_argument(
        "--file_ending", type=str, default="", help="adding_string_to_the_end"
    )
    argparser.add_argument(
        "--zero_indexed",
        type=str,
        default=0,
        help="1 - to start output PDB numbering with 0",
    )
    argparser.add_argument(
        "--seed",
        type=int,
        default=0,
        help="Set seed for torch, numpy, and python random.",
    )
    argparser.add_argument(
        "--batch_size",
        type=int,
        default=1,
        help="Number of sequence to generate per one pass.",
    )
    argparser.add_argument(
        "--number_of_batches",
        type=int,
        default=1,
        help="Number of times to design sequence using a chosen batch size.",
    )
    argparser.add_argument(
        "--save_stats", type=int, default=0, help="Save output statistics"
    )

    argparser.add_argument(
        "--ligand_mpnn_use_atom_context",
        type=int,
        default=1,
        help="1 - use atom context, 0 - do not use atom context.",
    )
    argparser.add_argument(
        "--ligand_mpnn_cutoff_for_score",
        type=float,
        default=8.0,
        help="Cutoff in angstroms between protein and context atoms to select residues for reporting score.",
    )
    argparser.add_argument(
        "--ligand_mpnn_use_side_chain_context",
        type=int,
        default=0,
        help="Flag to use side chain atoms as ligand context for the fixed residues",
    )
    argparser.add_argument(
        "--chains_to_design",
        type=str,
        default="",
        help="Specify which chains to redesign, all others will be kept fixed, 'A,B,C,F'",
    )

    argparser.add_argument(
        "--parse_these_chains_only",
        type=str,
        default="",
        help="Provide chains letters for parsing backbones, 'A,B,C,F'",
    )

    argparser.add_argument(
        "--transmembrane_buried",
        type=str,
        default="",
        help="Provide buried residues when using checkpoint_per_residue_label_membrane_mpnn model, A12 A13 A14 B2 B25",
    )
    argparser.add_argument(
        "--transmembrane_interface",
        type=str,
        default="",
        help="Provide interface residues when using checkpoint_per_residue_label_membrane_mpnn model, A12 A13 A14 B2 B25",
    )

    argparser.add_argument(
        "--global_transmembrane_label",
        type=int,
        default=0,
        help="Provide global label for global_label_membrane_mpnn model. 1 - transmembrane, 0 - soluble",
    )

    argparser.add_argument(
        "--parse_atoms_with_zero_occupancy",
        type=int,
        default=0,
        help="To parse atoms with zero occupancy in the PDB input files. 0 - do not parse, 1 - parse atoms with zero occupancy",
    )

    argparser.add_argument(
        "--checkpoint_path_sc",
        type=str,
        default="./model_params/ligandmpnn_sc_v_32_002_16.pt",
        help="Path to model weights.",
    )

    # Arguments unique to main
    if include_main_args:
        argparser.add_argument(
            "--force_hetatm",
            type=int,
            default=0,
            help="To force ligand atoms to be written as HETATM to PDB file after packing.",
        )

        argparser.add_argument(
            "--packed_suffix",
            type=str,
            default="_packed",
            help="Suffix for packed PDB paths",
        )

        argparser.add_argument(
            "--pack_with_ligand_context",
            type=int,
            default=1,
            help="1-pack side chains using ligand context, 0 - do not use it.",
        )
        argparser.add_argument(
            "--repack_everything",
            type=int,
            default=0,
            help="1 - repacks side chains of all residues including the fixed ones; 0 - keeps the side chains fixed for fixed residues",
        )
        argparser.add_argument(
            "--sc_num_samples",
            type=int,
            default=16,
            help="Number of samples to draw from a mixture distribution and then take a sample with the highest likelihood.",
        )
        argparser.add_argument(
            "--sc_num_denoising_steps",
            type=int,
            default=3,
            help="Number of denoising/recycling steps to make for side chain packing",
        )
        argparser.add_argument(
            "--number_of_packs_per_design",
            type=int,
            default=4,
            help="Number of independent side chain packing samples to return per design",
        )
        argparser.add_argument(
            "--temperature",
            type=float,
            default=0.1,
            help="Temperature to sample sequences.",
        )
        argparser.add_argument(
            "--pack_side_chains",
            type=int,
            default=0,
            help="1 - to run side chain packer, 0 - do not run it",
        )
        argparser.add_argument(
            "--symmetry_weights",
            type=str,
            default="",
            help="Add weights that match symmetry_residues, e.g. '1.01,1.0,1.0|-1.0,2.0|2.0,2.3'",
        )
        argparser.add_argument(
            "--bias_AA",
            type=str,
            default="",
            help="Bias generation of amino acids, e.g. 'A:-1.024,P:2.34,C:-12.34'",
        )
        argparser.add_argument(
            "--bias_AA_per_residue",
            type=str,
            default="",
            help="Path to json mapping of bias {'A12': {'G': -0.3, 'C': -2.0, 'H': 0.8}, 'A13': {'G': -1.3}}",
        )
        argparser.add_argument(
            "--bias_AA_per_residue_multi",
            type=str,
            default="",
            help="Path to json mapping of bias {'pdb_path': {'A12': {'G': -0.3, 'C': -2.0, 'H': 0.8}, 'A13': {'G': -1.3}}}",
        )

        argparser.add_argument(
            "--omit_AA",
            type=str,
            default="",
            help="Bias generation of amino acids, e.g. 'ACG'",
        )
        argparser.add_argument(
            "--omit_AA_per_residue",
            type=str,
            default="",
            help="Path to json mapping of bias {'A12': 'APQ', 'A13': 'QST'}",
        )
        argparser.add_argument(
            "--omit_AA_per_residue_multi",
            type=str,
            default="",
            help="Path to json mapping of bias {'pdb_path': {'A12': 'QSPC', 'A13': 'AGE'}}",
        )

    # Score-specific arguments
    if include_score_args:
        argparser.add_argument(
            "--use_sequence",
            type=int,
            default=1,
            help="1 - get scores using amino acid sequence info; 0 - get scores using backbone info only",
        )

        argparser.add_argument(
            "--autoregressive_score",
            type=int,
            default=0,
            help="1 - run autoregressive scoring function; p(AA_1|backbone); p(AA_2|backbone, AA_1) etc, 0 - False",
        )

        argparser.add_argument(
            "--single_aa_score",
            type=int,
            default=1,
            help="1 - run single amino acid scoring function; p(AA_i|backbone, AA_{all except ith one}), 0 - False",
        )
    return argparser