# Official LigandMPNN image maintained by [rosettacommons.org](https://rosettacommons.org/)

This image is built from the LigandMPNN repository that provides inference code for both ProteinMPNN and LigandMPNN.

LigandMPNN is fully open-source under an MIT License whose full text can be found [here](https://github.com/dauparas/LigandMPNN?tab=MIT-1-ov-file).

**Please note that this image is not compatible with systems using the ARM architecture.**

# Example syntax 
## Using Docker
```
docker run -it --rm \
-v /path/to/your/input_dir:/input \
-v /path/to/your/output_dir:/output \
rosettacommons/ligandmpnn \ 
--model_type 'protein_mpnn' \
--pdb_path /input/1BC8.pdb \
--out_folder /output
```

## Using Apptainer (or Singularity) 
*The instructions below use Apptainer, but the same commands will work with Singularity.*

To run the image using Apptainer you need to pull it using
```
apptainer pull ligandmpnn.sif docker://rosettacommons/ligandmpnn
```
Then you can use it very similarly to the Docker example above:
```
apptainer run --nv \
ligandmpnn.sif \
--model_type 'protein_mpnn' \
--pdb_path /path/to/your/input_dir/1BC8.pdb \
--out_folder /path/to/your/output_dir/"
--checkpoint_protein_mpnn '/app/ligandmpnn/model_params/proteinmpnn_v_48_020.pt'
```
**You will need to change the checkpoint_protein_mpnn path and option name depending on the model weights you want to use**

Please contact us with any questions, feedback, or issues you have concerning these containers [here](https://rosettacommons.org/contact/).
