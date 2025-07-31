# Official ProteinMPNN image maintained by [rosettacommons.org](https://rosettacommons.org/)

This image is built from the [ProteinMPNN](https://github.com/dauparas/ProteinMPNN)repository

ProteinMPNN is fully open-source under an MIT License whose full text can be found [here](https://github.com/dauparas/ProteinMPNN?tab=MIT-1-ov-file).

**Please note that this image is not compatible with systems using the ARM architecture.**

# Example syntax 
## Using Docker
```
docker run -it --rm \
-v /path/to/your/input_dir:/input \
-v /path/to/your/output_dir:/output \
rosettacommons/proteinmpnn \ 
--pdb_path /input/3HTN.pdb \
--pdb_path_chains "A B" \
--out_folder /output
```

Please see below for an example of running a helper scripts from ProteinMPNN. 

```
docker run -it --rm \
--entrypoint python \
-v /path/to/your/input_dir:/input \
-v /path/to/your/output_dir:/output \
rosettacommons/proteinmpnn \
/app/proteinmpnn/helper_scripts/parse_multiple_chains.py \
--input_path=/input/PDB_monomers/pdbs/ \
--output_path=/output/parsed_pdbs.jsonl
```

## Using Apptainer (or Singularity) 
*The instructions below use Apptainer, but the same commands will work with Singularity.*

To run the image using Apptainer you need to pull it using
```
apptainer pull proteinmpnn.sif docker://rosettacommons/proteinmpnn
```
Then you can use it very similarly to the Docker example above:
```
apptainer run --nv \
proteinmpnn.sif \
--pdb_path /path/to/your/input_dir/1BC8.pdb \
--pdb_path_chains "A B" \
--out_folder /path/to/your/output_dir" 
```

Please see the below example for running one of the helper scripts from ProteinMPNN with apptainer.           
```
apptainer exec \
proteinmpnn.sif \
python /app/proteinmpnn/helper_scripts/parse_multiple_chains.py \
--input_path=/path/to/your/input_dir/PDB_monomers/pdbs/ \
--output_path=./parsed_pdbs.jsonl
```


Please contact us with any questions, feedback, or issues you have concerning these containers [here](https://rosettacommons.org/contact/).
