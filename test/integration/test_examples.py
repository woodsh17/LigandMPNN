import subprocess
import sys
import os

sys.path.append("/Users/woodsh/RosettaMPNN")


def test_run_default_main():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "-m",
        "RosettaMPNN",
        "--out_folder",
        "./test/integration/outputs/default_main",
        "--pdb_path",
        "./inputs/1BC8.pdb",
        "--seed",
        "111",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_default():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/default",
        "--pdb_path",
        "./inputs/1BC8.pdb",
        "--seed",
        "111",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_temperature():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/temperature",
        "--pdb_path",
        "./inputs/1BC8.pdb",
        "--seed",
        "111",
        "--temperature",
        "0.05",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_seed():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/seed",
        "--pdb_path",
        "./inputs/1BC8.pdb",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_verbose():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/verbose",
        "--pdb_path",
        "./inputs/1BC8.pdb",
        "--seed",
        "111",
        "--verbose",
        "0",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_save_stats():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/save_stats",
        "--pdb_path",
        "./inputs/1BC8.pdb",
        "--seed",
        "111",
        "--save_stats",
        "1",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_fixed_residues():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/fixed_residues",
        "--pdb_path",
        "./inputs/1BC8.pdb",
        "--seed",
        "111",
        "--fixed_residues",
        "C1 C2 C3 C4 C5 C6 C7 C8 C9 C10",
        "--bias_AA",
        "A:10.0",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_redesigned_residues():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/redesign_residues",
        "--pdb_path",
        "./inputs/1BC8.pdb",
        "--seed",
        "111",
        "--redesigned_residues",
        "C1 C2 C3 C4 C5 C6 C7 C8 C9 C10",
        "--bias_AA",
        "A:10.0",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_number_of_batches():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/batch_size",
        "--pdb_path",
        "./inputs/1BC8.pdb",
        "--seed",
        "111",
        "--batch_size",
        "3",
        "--number_of_batches",
        "5",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_bias_AA():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/global_bias",
        "--pdb_path",
        "./inputs/1BC8.pdb",
        "--seed",
        "111",
        "--bias_AA",
        "W:3.0,P:3.0,C:3.0,A:-3.0",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_bias_AA_per_residue():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/per_residue_bias",
        "--pdb_path",
        "./inputs/1BC8.pdb",
        "--seed",
        "111",
        "--bias_AA_per_residue",
        "./inputs/bias_AA_per_residue.json",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_omit_AA():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/global_omit",
        "--pdb_path",
        "./inputs/1BC8.pdb",
        "--seed",
        "111",
        "--omit_AA",
        "CDFGHILMNPQRSTVWY",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_omit_AA_per_residue():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/per_residue_omit",
        "--pdb_path",
        "./inputs/1BC8.pdb",
        "--seed",
        "111",
        "--omit_AA_per_residue",
        "./inputs/omit_AA_per_residue.json",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_symmetry():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/symmetry",
        "--pdb_path",
        "./inputs/1BC8.pdb",
        "--seed",
        "111",
        "--symmetry_residues",
        "C1,C2,C3|C4,C5|C6,C7",
        "--symmetry_weights",
        "0.33,0.33,0.33|0.5,0.5|0.5,0.5",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_homo_oligomer():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/homooligomer",
        "--pdb_path",
        "./inputs/1BC8.pdb",
        "--seed",
        "111",
        "--homo_oligomer",
        "1",
        "--number_of_batches",
        "2",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_file_ending():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/file_ending",
        "--pdb_path",
        "./inputs/1BC8.pdb",
        "--seed",
        "111",
        "--file_ending",
        "_xyz",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_zero_indexed():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/zero_indexed",
        "--pdb_path",
        "./inputs/1BC8.pdb",
        "--seed",
        "111",
        "--zero_indexed",
        "1",
        "--number_of_batches",
        "2",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_chains_to_design():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/chains_to_design",
        "--pdb_path",
        "./inputs/4GYT.pdb",
        "--seed",
        "111",
        "--chains_to_design",
        "A,B",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_parse_these_chains_only():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/parse_these_chains_only",
        "--pdb_path",
        "./inputs/4GYT.pdb",
        "--seed",
        "111",
        "--parse_these_chains_only",
        "A,B",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_ligand_mpnn():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/ligandmpnn_default",
        "--pdb_path",
        "./inputs/1BC8.pdb",
        "--seed",
        "111",
        "--model_type",
        "ligand_mpnn",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_checkpoint_ligand_mpnn():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/ligandmpnn_v_32_005_25",
        "--pdb_path",
        "./inputs/1BC8.pdb",
        "--seed",
        "111",
        "--checkpoint_ligand_mpnn",
        "./model_params/ligandmpnn_v_32_005_25.pt",
        "--model_type",
        "ligand_mpnn",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_ligand_mpnn_use_atom_context():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/ligandmpnn_no_context",
        "--pdb_path",
        "./inputs/1BC8.pdb",
        "--seed",
        "111",
        "--ligand_mpnn_use_atom_context",
        "0",
        "--model_type",
        "ligand_mpnn",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_ligand_mpnn_use_side_chain_context():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/ligandmpnn_use_side_chain_atoms",
        "--pdb_path",
        "./inputs/1BC8.pdb",
        "--seed",
        "111",
        "--ligand_mpnn_use_side_chain_context",
        "1",
        "--model_type",
        "ligand_mpnn",
        "--fixed_residues",
        "C1 C2 C3 C4 C5 C6 C7 C8 C9 C10",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_soluble_mpnn():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/soluble_mpnn_default",
        "--pdb_path",
        "./inputs/1BC8.pdb",
        "--seed",
        "111",
        "--model_type",
        "soluble_mpnn",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_global_label_membrane_mpnn():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/global_label_membrane_mpnn_0",
        "--pdb_path",
        "./inputs/1BC8.pdb",
        "--seed",
        "111",
        "--model_type",
        "global_label_membrane_mpnn",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_global_label_membrane_mpnn():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/global_label_membrane_mpnn_0",
        "--pdb_path",
        "./inputs/1BC8.pdb",
        "--seed",
        "111",
        "--model_type",
        "global_label_membrane_mpnn",
        "--global_transmembrane_label",
        "0",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_per_residue_label_membrane_mpnn():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/per_residue_label_membrane_mpnn",
        "--pdb_path",
        "./inputs/1BC8.pdb",
        "--seed",
        "111",
        "--model_type",
        "global_label_membrane_mpnn",
        "--transmembrane_buried",
        "C1 C2 C3 C11",
        "--transmembrane_interface",
        "C4 C5 C6 C22",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_fasta_seq_separation():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/fasta_seq_separation",
        "--pdb_path",
        "./inputs/1BC8.pdb",
        "--seed",
        "111",
        "--fasta_seq_separation",
        ":",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_pdb_path_multi():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/pdb_path_multi",
        "--pdb_path_multi",
        "./inputs/pdb_ids.json",
        "--seed",
        "111",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_fixed_residues_multi():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/fixed_residues_multi",
        "--pdb_path_multi",
        "./inputs/pdb_ids.json",
        "--seed",
        "111",
        "--fixed_residues_multi",
        "./inputs/fix_residues_multi.json",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_redesigned_residues_multi():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/redesigned_residues_multi",
        "--pdb_path_multi",
        "./inputs/pdb_ids.json",
        "--seed",
        "111",
        "--redesigned_residues_multi",
        "./inputs/redesigned_residues_multi.json",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_omit_AA_per_residue_multi():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/omit_AA_per_residues_multi",
        "--pdb_path_multi",
        "./inputs/pdb_ids.json",
        "--seed",
        "111",
        "--omit_AA_per_residue_multi",
        "./inputs/omit_AA_per_residue_multi.json",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_bias_AA_per_residue_multi():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/bias_AA_per_residues_multi",
        "--pdb_path_multi",
        "./inputs/pdb_ids.json",
        "--seed",
        "111",
        "--bias_AA_per_residue_multi",
        "./inputs/bias_AA_per_residue_multi.json",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_ligand_mpnn_cutoff_for_score():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/ligand_mpnn_cutoff_for_score",
        "--pdb_path",
        "./inputs/1BC8.pdb",
        "--seed",
        "111",
        "--ligand_mpnn_cutoff_for_score",
        "6.0",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_insertion_code():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/insertion_code",
        "--pdb_path",
        "./inputs/2GFB.pdb",
        "--seed",
        "111",
        "--redesigned_residues",
        "B82 B82A B82B B82C",
        "--parse_these_chains_only",
        "B",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_parse_atoms_with_zero_occupancy():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/parse_atoms_with_zero_occupancy",
        "--pdb_path",
        "./inputs/1BC8.pdb",
        "--seed",
        "111",
        "--parse_atoms_with_zero_occupancy",
        "1",
        "--model_type",
        "ligand_mpnn",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0
