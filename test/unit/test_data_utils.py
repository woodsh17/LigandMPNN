import sys
import os

from Bio.PDB import PDBParser

sys.path.append("/Users/woodsh/RosettaMPNN/RosettaMPNN")
from data_utils import (
    combine_pdbs,
    parse_PDB,
    parse_msd_residue_range,
    parse_msd_constraints,
)


def create_mock_pdb(
    path,
    chain_id="A",
    res_start=1,
    res_end=3,
    atom_start=1,
    ligand=False,
    ligand_chain_id=None,
):
    """
    Create a minimal mock PDB file with a few residues and optionally a ligand.
    Args:
        path: Output file path
        chain_id: Chain identifier
        res_start: First residue number
        res_end: Last residue number (inclusive)
        atom_start: Atom serial start (for unique numbering)
        ligand: If True, adds a ligand (HETATM) record
        ligand_chain_id: Chain ID for the ligand (if None, uses chain_id)
    """
    pdb_lines = []
    atom_serial = atom_start
    # Protein atoms: 1 N, 1 CA, 1 C per residue
    for res in range(res_start, res_end + 1):
        for atom, x, y, z in [
            ("N", 0.0, 0.0, 0.0),
            ("CA", 1.5, 0.0, 0.0),
            ("C", 2.5, 1.0, 0.0),
        ]:
            pdb_lines.append(
                "ATOM  {serial:5d} {atom:^4} ALA {chain}{res:4d}    {x:8.3f}{y:8.3f}{z:8.3f}  1.00 20.00           {element:>2}".format(
                    serial=atom_serial,
                    atom=atom,
                    chain=chain_id,
                    res=res,
                    x=x + res * 3,
                    y=y,
                    z=z,
                    element=atom[0],
                )
            )
            atom_serial += 1

    if ligand:
        # Use ligand_chain_id if provided, else fall back to protein chain_id
        lig_cid = ligand_chain_id if ligand_chain_id is not None else chain_id
        # Add a simple ligand (e.g., "LIG" with 2 atoms)
        for i, (atom, x, y, z) in enumerate(
            [
                ("C1", 11.0, 0.5, 0.0),
                ("O1", 12.0, 1.0, 0.0),
            ]
        ):
            pdb_lines.append(
                "HETATM{serial:5d} {atom:^4} LIG {chain}{res:4d}    {x:8.3f}{y:8.3f}{z:8.3f}  1.00 30.00           {element:>2}".format(
                    serial=atom_serial,
                    atom=atom,
                    chain=lig_cid,
                    res=res_end + 1,
                    x=x,
                    y=y,
                    z=z,
                    element=atom[0],
                )
            )
            atom_serial += 1

    pdb_lines.append("END\n")
    with open(path, "w") as f:
        f.write("\n".join(pdb_lines))


def test_combine_pdbs():
    # make two mock PDBS for testing
    create_mock_pdb("pdb1.pdb", chain_id="A", ligand=False)
    create_mock_pdb("pdb2.pdb", chain_id="A", ligand=False)

    chain_map = combine_pdbs(["pdb1.pdb", "pdb2.pdb"], "combined.pdb", gap=1000)

    # Validate chain mapping structure
    assert "pdb1" in chain_map and "pdb2" in chain_map
    assert isinstance(chain_map["pdb1"], dict)
    assert all(len(v) == 1 for v in chain_map.values())  # Each has 1 chain

    # Ensure renamed chains are distinct
    all_new_chains = set()
    for mapping in chain_map.values():
        all_new_chains.update(mapping.values())
    assert len(all_new_chains) == 2

    # Ensure combined.pdb is not empty
    with open("combined.pdb") as f:
        pdb_content = f.read()
    assert pdb_content.strip() != "", "combined.pdb is empty!"

    # Parse combined.pdb and check chain IDs
    parser = PDBParser(QUIET=True)
    struct = parser.get_structure("combined", "combined.pdb")
    model = next(struct.get_models())
    chains_in_pdb = [chain.id for chain in model.get_chains()]
    assert (
        len(chains_in_pdb) == 2
    ), f"Expected 2 chains, found {len(chains_in_pdb)}: {chains_in_pdb}"

    # Check that the chains in the file match the new chain IDs in chain_map
    mapped_chains = set()
    for mapping in chain_map.values():
        mapped_chains.update(mapping.values())
    assert (
        set(chains_in_pdb) == mapped_chains
    ), f"Chains in file ({chains_in_pdb}) do not match map ({mapped_chains})"

    create_mock_pdb("pdb3_ligand.pdb", chain_id="A", ligand=True, ligand_chain_id="L")
    chain_map_ligand = combine_pdbs(
        ["combined.pdb", "pdb3_ligand.pdb"], "combined_ligand.pdb"
    )

    chain_map_ligand = combine_pdbs(
        ["combined.pdb", "pdb3_ligand.pdb"], "combined_ligand.pdb"
    )

    # 1. File is not empty
    with open("combined_ligand.pdb") as f:
        contents = f.read()
    assert contents.strip(), "combined_ligand.pdb is empty"

    # 2. Parse and check number of chains
    parser = PDBParser(QUIET=True)
    struct = parser.get_structure("combined_ligand", "combined_ligand.pdb")
    model = next(struct.get_models())
    chains = list(model.get_chains())
    chain_ids = [chain.id for chain in chains]
    assert (
        len(chain_ids) == 4
    ), f"Expected at least 2 chains, found {len(chain_ids)}: {chain_ids}"

    # 3. Confirm ligand (HETATM) present
    hetatm_lines = [line for line in contents.splitlines() if line.startswith("HETATM")]
    assert hetatm_lines, "No HETATM (ligand) records found in combined_ligand.pdb"

    # 4. Check that chain_map_ligand keys match input file roots
    assert set(chain_map_ligand.keys()) == {"combined", "pdb3_ligand"}

    # Optionally: check that ligand is on a unique chain or matches mapping
    ligand_chain_ids = set(line[21] for line in hetatm_lines)
    # All ligand chain IDs should be in the chain mapping values
    all_mapped_chains = {
        v for mapping in chain_map_ligand.values() for v in mapping.values()
    }
    assert (
        ligand_chain_ids <= all_mapped_chains
    ), f"Ligand chain IDs {ligand_chain_ids} not in mapped chains {all_mapped_chains}"


def test_parse_msd_residue_range():
    chain, start, end = parse_msd_residue_range("K110-K120")
    assert chain == "K"
    assert start == 110
    assert end == 120


def test_parse_constraints():
    create_mock_pdb("pdb1.pdb", chain_id="A", res_start=1, res_end=3, atom_start=1)
    create_mock_pdb("pdb2.pdb", chain_id="A", res_start=1, res_end=3, atom_start=1)

    chain_map = combine_pdbs(["pdb1.pdb", "pdb2.pdb"], "combined.pdb", gap=1000)
    res_list, betas_list = parse_msd_constraints(
        "pdb1:A1-A3:0.5, pdb2:A1-A3:0.5", chain_map
    )

    assert res_list == [["A1", "B1"], ["A2", "B2"], ["A3", "B3"]]
    assert betas_list == [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]

    create_mock_pdb(
        "pdb3_ligand.pdb",
        chain_id="A",
        res_start=1,
        res_end=3,
        ligand=True,
        ligand_chain_id="L",
    )
    chain_map_ligand = combine_pdbs(
        ["combined.pdb", "pdb3_ligand.pdb"], "combined_ligand.pdb"
    )
    ligand_res_list, ligand_betas_list = parse_msd_constraints(
        "combined:A1-A3:1.0, pdb3_ligand:A1-A3:0.5, combined:B1-B3:1.0; pdb3_ligand:L4:1.0",
        chain_map_ligand,
    )

    assert ligand_res_list == [
        ["A1", "C1", "B1"],
        ["A2", "C2", "B2"],
        ["A3", "C3", "B3"],
        ["L4"],
    ]
    assert ligand_betas_list == [
        [1.0, 0.5, 1.0],
        [1.0, 0.5, 1.0],
        [1.0, 0.5, 1.0],
        [1.0],
    ]
