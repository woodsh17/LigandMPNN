import subprocess
import sys
import os

sys.path.append("/Users/woodsh/LigandMPNN")


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
        cmd, cwd="/Users/woodsh/LigandMPNN", capture_output=True, text=True
    )
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)
    # Check for successful run and expected outputs
    assert result.returncode == 0
