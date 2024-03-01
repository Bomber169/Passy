# Passy The Password Strength Analyzer

A machine learning-based tool to analyze the strength of passwords, utilizing a dataset of 14 million RockYou passwords to determine whether a password is cracked or not.

# Features

Utilizes machine learning algorithms to analyze password strength.
Determines whether a password is cracked or not based on a large dataset.
Provides insights into the strength of passwords.

# Installation

To install the Password Strength Analyzer, follow these steps:

Clone the repository:

Install dependencies:

    pip install -r requirements.txt

# Usage
1)Train the model and dump it locally on your pc using dill for that go the directory of repository run the script passy_v1.5.py using command below:

# For Linux
    python3 passy_v1.5.py
# For Windows
    py passy_v1.5.py
    
2)To analyze the strength of a password, run the passy_v1.5(CLI).py script in terminal for cli version and input the password when prompted. The tool will then provide feedback on the strength of the password or for web interface enter the command below:
    
    uvicorn app:app --reload

# Dataset

The dataset used for training and testing the password strength analyzer consists of 14 million passwords obtained from the RockYou dataset. Preprocessing steps were applied to clean and prepare the data for training.

# Technologies Used

Python
scikit-learn
fastapi
jinja2
XGB Classifier
uvicorn

    



