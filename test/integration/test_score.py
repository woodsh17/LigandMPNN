import subprocess
import sys
import os

sys.path.append("/Users/woodsh/RosettaMPNN")


def test_score_autoregressive_score_w_seq():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "score.py",
        "--out_folder",
        "./test/integration/outputs/autoregressive_score_w_seq",
        "--seed",
        "111",
        "--model_type",
        "ligand_mpnn",
        "--pdb_path",
        "./outputs/ligandmpnn_default/backbones/1BC8_1.pdb",
        "--use_sequence",
        "1",
        "--batch_size",
        "1",
        "--number_of_batches",
        "10",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_score_autoregressive_score_wo_seq():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "score.py",
        "--out_folder",
        "./test/integration/outputs/autoregressive_score_wo_seq",
        "--seed",
        "111",
        "--model_type",
        "ligand_mpnn",
        "--pdb_path",
        "./outputs/ligandmpnn_default/backbones/1BC8_1.pdb",
        "--use_sequence",
        "0",
        "--batch_size",
        "1",
        "--number_of_batches",
        "10",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_score_single_aa_score_w_seq():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "score.py",
        "--out_folder",
        "./test/integration/outputs/score_single_aa_score_w_seq",
        "--seed",
        "111",
        "--model_type",
        "ligand_mpnn",
        "--pdb_path",
        "./outputs/ligandmpnn_default/backbones/1BC8_1.pdb",
        "--single_aa_score",
        "1",
        "--use_sequence",
        "1",
        "--batch_size",
        "1",
        "--number_of_batches",
        "10",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_score_single_aa_score_wo_seq():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "score.py",
        "--out_folder",
        "./test/integration/outputs/score_single_aa_score_wo_seq",
        "--seed",
        "111",
        "--model_type",
        "ligand_mpnn",
        "--pdb_path",
        "./outputs/ligandmpnn_default/backbones/1BC8_1.pdb",
        "--single_aa_score",
        "1",
        "--use_sequence",
        "0",
        "--batch_size",
        "1",
        "--number_of_batches",
        "10",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0
