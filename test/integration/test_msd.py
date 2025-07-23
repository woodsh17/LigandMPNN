import subprocess
import sys
import os

sys.path.append("/Users/woodsh/LigandMPNN")


def test_run_msd_single_constraint():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "-m",
        "LigandMPNN",
        "--out_folder",
        "./test/integration/outputs/single_constraint",
        "--multi_state_pdb_path",
        "./test/integration/msd_pdbs.json",
        "--multi_state_constraints",
        "4GYT_dimer:A7-A183:0.5,4GYT_dimer:B7-B183:0.5,4GYT_monomer:A7-A183:1",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/LigandMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0

    # Check if predicted sequences for the three states are identical
    fasta_path = "./outputs/single_constraint/seqs/msd.fa"
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


def test_run_msd_mulitple_constraint():
    cmd = [
        sys.executable,  # this runs the current Python interpreter
        "-m",
        "LigandMPNN",
        "--out_folder",
        "./test/integration/outputs/msd_multiple_constraint",
        "--multi_state_pdb_path",
        "./test/integration/msd_multi_constraint_pdbs.json",
        "--multi_state_constraints",
        "1a0o:A1-A128:1,1a0o_chainA_monomer:A1-A128:1;1a0o:B1-B70:1,1a0o_chainB_monomer:B1-B70:-1",
    ]

    result = subprocess.run(
        cmd, cwd="/Users/woodsh/LigandMPNN", capture_output=True, text=True
    )
    # Check for successful run and expected outputs
    assert result.returncode == 0

    base = "./outputs/msd_multiple_constraint/seqs"

    def get_seq(path):
        with open(path, "r") as f:
            lines = f.readlines()
        return "".join([l.strip() for l in lines if not l.startswith(">")])

    # load sequences
    seq_1a0o = get_seq(os.path.join(base, "1a0o_1.fa")).split(":")
    seq_chainA_monomer = get_seq(os.path.join(base, "1a0o_chainA_monomer_1.fa")).split(
        ":"
    )
    seq_chainB_monomer = get_seq(os.path.join(base, "1a0o_chainB_monomer_1.fa")).split(
        ":"
    )

    # verify correct chain counts
    assert len(seq_1a0o) >= 2, "Expected at least two chains in 1a0o"
    assert len(seq_chainA_monomer) == 1
    assert len(seq_chainB_monomer) == 1

    # A1–A128 check
    assert (
        seq_1a0o[0][:128] == seq_chainA_monomer[0][:128]
    ), "Mismatch in A1–A128 between 1a0o and 1a0o_chainA_monomer"

    # B1–B70 check
    assert (
        seq_1a0o[1][:70] == seq_chainB_monomer[0][:70]
    ), "Mismatch in B1–B70 between 1a0o and 1a0o_chainB_monomer"
