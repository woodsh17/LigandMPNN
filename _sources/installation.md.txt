# Installation
<!--
If you're using a system with an AMD architecture, we recommend using the available [Docker image](docker.rst).
-->

## System Requirements and Prerequesites
The model weights and repository will take about 1G of space on your system.

## Installation Guide
The recommended way to install RosettaMPNN is via [uv](https://docs.astral.sh/uv/), however installation via a [miniforge](https://github.com/conda-forge/miniforge) environment is available as well. See the dropdowns below for step-by-step instructions. 

1. Clone and enter the repository:
    ```
    git clone git@github.com:woodsh17/RosettaMPNN.git
    cd RosettaMPNN
    ```
1. Download the model weights - including the weights for HyperMPNN:
    ```
    bash get_model_params.sh model_params
    ```
    *For more information on model weights see the documentation page on [model weights](model_weights_ref.md)*

<details>
<summary><strong>Installation using <code>uv</code> </strong></summary>

3. If you do not have `uv` installed, run:
    ```
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
    1. (Optional) Create an alias (if necessary) to call `uv` without giving the full path:
        When `uv` is installed on your system it will specify the path that it is installed to. Use that path to make the alias. 
        ```
        alias uv=/path/to/installation/of/uv
        ```
        You can add this path to your `bash.rc` or `.zshrc` to have the alias automatically set when you use your terminal. 
1. Create a virutal environment using Python 3.11 and activate it
    ```
    uv venv rosettampnn_venv --python 3.11
    source rosettampnn_venv/bin/activate
    ```
    **You will need to activate this environment whenever you run RosettaMPNN**
1. Install the dependencies: 
    - If CUDA is available: 
        ```
        uv pip install -e .[cuda]
        ```
    - If CUDA is not available:
        ```
        uv pip install -e .
        ```

1. Add RosettaMPNN to your PYTHONPATH:
    ```
    export PYTHONPATH=/path/to/RosettaMPNN:$PYTHONPATH
    ```
    *If you do not complete this step you will likely see a `ModuleNotFoundError: No module named 'openfold'` error.*

</details>

<details>
<summary><strong>Iinstallation using miniforge</strong></summary>

3. Create a conda environment and activate it:
    ```
    conda create -n rosettampnn_env python=3.11
    conda activate rosettampnn_env
    ```
    **You will need to activate this environment whenever you run RosettaMPNN**
1. Install the dependencies:
    - If CUDA is available:
        ```
        pip install -r requirements.txt
        pip install -e .
        ```
    - If CUDA is not availiable: 
        ```
        pip install -r requirementts_no_nvidia_cuda.txt
        ```
1. *(Optional but recommended)* Add RosettaMPNN to your PYTHONPATH:
    ```
    export PYTHONPATH=/PATH/TO/RosettaMPNN:$PYTHONPATH
    ```
</details>
