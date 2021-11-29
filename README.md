# Data Sience Laboratory

In this folder save every step of my workprocess. Minimal Work Effort(MWE) is contained here.

## Data structure:  
- EDA: Stands for Explorational Data Analysis. It's reason to understand the data
- src: Sorce for python codes and notebooks. For data preparation, model creation, etc.
- figures: Inside this repo, the figures are saved.
- results: Inside this repo, the results are saved, for example: models, model parameters.
- data: In this repo, the data is saved, if it is too big, it will contain link for the container or some description of the data, I dunno yet.

### Eda
- Loadnc.ipynb : Load and understand the data format. Not necesarry for reproduction, but esential for understanding  
- Pandasread.ipynb : The data converted into pandas Dataframe. Visualization of the mostion of a specific Eddy. And the longevity.

### Results
- EDA.md : The results of EDA and some additional information.

### SRC
Sorce codes, it might contain an other README.md with deeper explanation.

### Dependencies
Containing yet, only the enviroment.yml

### ABT_creator
This Notebook calls some Functions and create an ABT

## Author:
Dudás Bence

## Project name:
Mesoscale Ocean Eddies along the U.S. West Coast

## How to use it:
### Step 1
First you have to create an environment. If you are using anaconda, it is the following command:  
<center> conda env create -f environment.yml </center>  
Note: you have to go into the dependecies folder, but after it, this will work  
In the kooplex you need to consult with the teachers.

### Step 2
(Optional for users)  
Understanding the data. Go into the EDA folder. There are 2 notebooks, which were used to understand the data. It is mandatory for later work.

### Step 3
Feature engineering  
This is a pretty long process, took some hours, so I upload the data into this repo

### Step 4 
To recreate the results you must go to the main.ipynb and run all cells. The only 2 package which can have problems is shap and catboost.  
To install shap, you need the following in anaconda:  
- conda install -c conda-forge shap  
- conda install -c conda-forge/label/cf201901 shap  
- conda install -c conda-forge/label/cf202003 shap  
  
To install catboost:   
- conda config --add channels conda-forge  
- conda install catboost  

Installig catboost dashboard(optional):  
- pip install ipywidgets  
- jupyter nbextension enable --py widgetsnbextension  

