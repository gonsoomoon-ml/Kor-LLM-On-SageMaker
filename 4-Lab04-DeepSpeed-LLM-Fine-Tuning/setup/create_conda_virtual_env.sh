#!/bin/bash

#####################################
# Check if an argument is provided
#####################################
if [ $# -eq 0 ]; then
    echo "Error: Please provide name of conda virtual environment as an argument."
    echo "Usage example: ./create_conda_virtual_env.sh MyEnv"
    exit 1
fi

#####################################
# Access the provided argument
#####################################
argument=$1

# Rest of the script
echo "The provided conda virtual environment is: $argument"
# Add your desired script logic here

export VirtualEnv=$argument

#####################################
# Create conda virtual env.
#####################################
conda create -y -n $VirtualEnv python=3.10.14

# wait for  seconds
echo "# Wait for 5 seconds to proceed with next step"
sleep 5

#####################################
# Activate the given $VirtualEnv
#####################################
source activate $VirtualEnv

# show current virtual env.
echo "# show current virtual env"
conda info --envs
which python
echo ""

