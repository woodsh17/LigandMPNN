import subprocess
import sys
import os

sys.path.append("/Users/woodsh/LigandMPNN")

def test_run_symm():
    cmd = [
        sys.executable, # this runs the current Python interpreter
        "run.py",
        "--out_folder", "./test/integration/outputs/",
        "--pdb_path", "./test/integration/inputs/1BC8.pdb",
        "--symmetry_residues", "C1,C2,C3|C4,C5|C6,C7",
        "--symmetry_weights", "0.33,0.33,0.33|0.5,0.5|0.5,0.5"
    ]

    result = subprocess.run(cmd, cwd="/Users/woodsh/LigandMPNN", capture_output=True, text=True)
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)
    # Check for successful run and expected outputs
    assert result.returncode == 0

     # Parse second sequence from FASTA file
    fasta_path = "./outputs/seqs/1BC8.fa"
    assert os.path.exists(fasta_path), f"FASTA file not found: {fasta_path}"

    with open(fasta_path, "r") as f:
        lines = f.read().splitlines()

    sequences = []
    seq_buffer = []
    for line in lines:
        if line.startswith(">"):
            if seq_buffer:
                sequences.append("".join(seq_buffer))
                seq_buffer = []
        else:
            seq_buffer.append(line)
    if seq_buffer:
        sequences.append("".join(seq_buffer))

    assert len(sequences) >= 2, "Less than 2 sequences in FASTA file"

    seq = sequences[1]  # second sequence

    # Symmetry checks
    assert seq[0] == seq[1] == seq[2], f"First three residues not equal: {seq[0:3]}"
    assert seq[3] == seq[4], f"Residues 4 and 5 not equal: {seq[3]} != {seq[4]}"
    assert seq[5] == seq[6], f"Residues 6 and 7 not equal: {seq[5]} != {seq[6]}"