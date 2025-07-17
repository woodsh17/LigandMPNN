import subprocess
import sys
import os

sys.path.append("/Users/woodsh/LigandMPNN")

def test_run_msd():
    cmd = [
        sys.executable, # this runs the current Python interpreter
        "run.py",
        "--out_folder", "./test/integration/outputs/",
        "--multi_state_pdb_path", "./test/integration/msd_pdbs.json",
        "--multi_state_constraints", "4GYT_dimer:A7-A183:0.5,4GYT_dimer:B7-B183:0.5,4GYT_monomer:A7-A183:1"
    ]

    result = subprocess.run(cmd, cwd="/Users/woodsh/LigandMPNN", capture_output=True, text=True)
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)
    # Check for successful run and expected outputs
    assert result.returncode == 0

    # Check if predicted sequences for the three states are identical 
    fasta_path = "./outputs/seqs/msd.fa"
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

    assert len(sequences) > 0, "No sequences found in FASTA file"
    reference_seq = sequences[1]
    for seq in sequences[2:]:
        assert seq == reference_seq, f"Sequence mismatch:\n{seq}\n!=\n{reference_seq}"


