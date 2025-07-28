import subprocess
import sys
import os

sys.path.append("/Users/woodsh/RosettaMPNN")


def test_run_hyper_for_proteinmpnn():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/hyper",
        "--seed",
        "111",
        "--pdb_path",
        "./test/integration/inputs/1BC8.pdb",
        "--model_type",
        "protein_mpnn",
        "--checkpoint_protein_mpnn",
        "model_params/hypermpnn_v48_020_epoch300.pt",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_hyper_for_proteinmpnn_e240():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/hyper_e240",
        "--seed",
        "111",
        "--pdb_path",
        "./test/integration/inputs/1BC8.pdb",
        "--model_type",
        "protein_mpnn",
        "--checkpoint_protein_mpnn",
        "model_params/hypermpnn_v48_002_epoch240.pt",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_hyper_for_proteinmpnn_01():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/hyper_01",
        "--seed",
        "111",
        "--pdb_path",
        "./test/integration/inputs/1BC8.pdb",
        "--model_type",
        "protein_mpnn",
        "--checkpoint_protein_mpnn",
        "model_params/hypermpnn_v48_010_epoch300.pt",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)
    # Check for successful run and expected outputs
    assert result.returncode == 0


def test_run_hyper_for_proteinmpnn_03():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "run.py",
        "--out_folder",
        "./test/integration/outputs/hyper_03",
        "--seed",
        "111",
        "--pdb_path",
        "./test/integration/inputs/1BC8.pdb",
        "--model_type",
        "protein_mpnn",
        "--checkpoint_protein_mpnn",
        "model_params/hypermpnn_v48_030_epoch300.pt",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/RosettaMPNN", capture_output=True, text=True
    )
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)
    # Check for successful run and expected outputs
    assert result.returncode == 0
