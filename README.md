## “The Impact of Socioeconomic Factors and Municipal Spending on Public School District Performance in Massachusetts”

A data science capstone project that investigates how socioeconomic factors and resource allocation impact public school district graduation rates in Massachusetts.  This project applies machine learning and statistical modeling techniques to identify key predictors of graduation rates, helpful for providing actionable insights for school district leaders and state level policymakers.


## Table of Contents
- [Background](#background)
- [Requirements](#requirements)
- [Installation](#installation)
- [Data](#data)
- [Notebooks](#notebooks)
- [Deliverables](#deliverables)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)        


### Background
Public school districts across the United States continue to face significant challenges, including budget cuts, delayed funding, and contentious contract negotiations.  These pressures often widen inequities between districts and create inconsistent opportunities for students.  Prior research has shown that outcomes such as high school graduation are closely linked to socioeconomic status as well as a district’s ability to fund schools.

**Research Question** <br>
Given the socioeconomic challenges and educational needs that school districts cannot control, how can they best use their available resources to improve graduation rates?

**Hypothesis** <br>
School districts can benefit from allocating more funds to student-facing resources to improve graduation rates because increased investment in areas such as teacher experience, class size, and school performance correlates with improved student outcomes and reduced dropout rates.

**Predictions** <br>
1) School districts that spend less per pupil will have lower graduation rates.
2) School districts with a higher percentage of experienced, certified teachers will have higher graduation rates.
3) School districts meeting or exceeding state improvement targets will have higher graduation rates.
4) School districts with a lower student-to-teacher ratio will have higher graduation rates.

### Requirements
- Use Python 3.11 or higher
- For package dependencies, see [requirements.txt](requirements.txt)

### Installation
1) Clone the repository
```bash
git clone https://github.com/felixtry/DSE6311OM_Group3.git
```
2) Install dependencies
```bash
pip install -r requirements.txt
```

### Data
The dataset used in this project comes from the following sources:
1. **Massachusetts Department of Elementary and Secondard Education (DESE):**  
district-level graduation rates, accountability classifications, student demographics, financial inputs, and teacher data  
Datasets in `Data/` folder from DESE: [Accountability.xlsx](Data/Accountability.xlsx), [PerPupilExpenditures.xlsx](Data/PerPupilExpenditures.xlsx), [gradrates.xlsx](Data/gradrates.xlsx), [teacherdata.xlsx](Data/teacherdata.xlsx)
    
2. **Massachusetts Department of Revenue (DOR):**  
municipal income per capita  
Datasets in `Data/` folder from DOR: [DOR_Income_EQV_Per_Capita.xlsx](Data/DOR_Income_EQV_Per_Capita.xlsx)  
  
3. **MassGIS:**  
geographic and municipal data  
Datasets in `Data/` folder from MassGIS: [schooldistricts_Town.csv](Data/schooldistricts_Town.csv), [schooldistricts_charter.csv](Data/schooldistricts_charter.csv)
  
4. **Additional Dataset:**  
Dataset in `Data/` folder: [Missing Regional Schools.xlsx](https://github.com/felixtry/DSE6311OM_Group3/blob/e34f89bbce30356adc7b1030a2fc43e24451b201/Data/Missing%20Regional%20Schools.xlsx)
   


### Notebooks
The analysis is organized across a series of Juypyter notebooks located in the `Notebook/` folder.  
They should be run in order for the best results:  
[1_Data](Notebook/1_Data.ipynb): merge datasets, data cleaning  
[2_EDA](Notebook/2_EDA.ipynb): handle missing values, descriptive statistics & visualization, correlation checks, initial insights  
[3_Preprocessing_and_Feature_Engineering](Notebook/3_Preprocessing_and_Feature_Engineering.ipynb): encode categorical values, identify outliers, feature engineering  
[4_Model_trials](Notebook/4_Model_trials.ipynb): train and test split, feature scaling, null model, preliminary Random Forest model  
[5_Split_models](Notebook/5_Split_models.ipynb): including Random Forest model with different feature sets  
[6_OLS_model](Notebook/6_OLS_model.ipynb): OLS model (with attempts to improve), Ridge Regression model, baseline OLS model  
[7_regression_models](Notebook/7_regression_models.ipynb): Random Forest model (with hyperparameter tuning), XGBoost model (with hyperparameter tuning), Support Vector Regression, CatBoost model  
[8_regression_models_latest](Notebook/8_regression_models_latest.ipynb): Final tuning and analysis of Random Forest model,  XGBoost model, Support Vector Regression, CatBoost model


### Contributing
Contributions are welcome!
If you have anys suggestions, please fork the repo and create a pull request or open an issue. <br>

1) Fork the repository
2) Create a new branch (git checkout -b feature-name)
3) Commit your changes (git commit -m "Add feature")
4) Push to the branch (git push origin feature-name)
5) Open a Pull Request  
  
Please note that we follow the [Contributor Covenant Code of Conduct](http://contributor-covenant.org/version/1/3/0/)

### Deliverables
- [Final Report]
- [Presentation Slides](https://drive.google.com/file/d/1SIjCxUSnnImaJNqD9ohsQCvLM_JT34Uq/view?usp=drive_link)

### Acknowledgements
**Team Members:** <br>
              Amanda Frithsen <br>
              Felix Rajappan <br>
              Ertugrul Turkseven <br>
              <br>
**Instructor:** Christopher Healey
