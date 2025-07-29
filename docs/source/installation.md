# Installation Guide

If you're using a system with an AMD architecture, we recommend using the available [Docker image](docker.rst).

## System Requirements and Prerequesites

An installation of [Conda or Miniconda](https://www.anaconda.com/download/success) is required to follow this installation guide. 

The repository and all of the model parameter files will take about 1G of storage space.

For a full list of software and library dependencies:
- If your system has NVIDIA GPUs equipped with CUDA libraries see `requirements.txt`
- For all other systems see `requirements_no_nvidia_cuda.txt` 

## Installation instructions

1. Clone the repository: <mark>THIS WILL NEED TO BE UPDATED</mark>
    ```
    git clone git@github.com:woodsh17/RosettaMPNN.git
    ```
1. Download the model weights and place them in a direcotry called `model_params`. this will also download the weights for HyperMPNN
   ````
   cd RosettaMPNN
   bash get_model_params.sh model_params
1. Create a conda environment and activate it
    ```
    conda create -n rosettampnn_env python=3.11
    conda activate rosettampnn_env
    ```
    **Make sure to activate this environment whenever you want to run RosettaMPNN**
1. Install all of the dependencies of ProteinMPNN: 
    - If your system has NVIDIA GPUs equipped with CUDA libraries:
        ```
        pip install -r requirements.txt
        ```
    - For all other systems: 
        ```
        pip install -r requirements_no_nvidia_cuda.txt
        ```
1. *(Optional)* To make it easier to call RosettaMPNN, it is recommended to add the repository location to your PYTHONPATH:
   ```
   export PYTHONPATH=$PYTHONPATH:/path/to/RosettaMPNN