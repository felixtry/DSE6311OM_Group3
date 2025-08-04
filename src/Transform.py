import pandas as pd 
import numpy as np 
import src.Configuration as config
import src.file_reader as rd
def TransformData():
    df_grads = rd.ReadExcelFile(config.grads,1)
    df_acctblty = rd.ReadExcelFile(config.acctblty, 1)
    df_percapita = rd.ReadExcelFile(config.percapita,  0)
    df_perpupil = rd.ReadExcelFile(config.perpupil, 1)
    df_population = rd.ReadExcelFile(config.population, 1)
    df_teacher = rd.ReadExcelFile(config.teacher,  1)
    df_charterschool = pd.read_csv(config.charterschools,header=0)
    df_townschool = pd.read_csv(config.townschools,header=0)
    # Merge and drop redundant 'District Name' after each merge
    df = df_population.copy()
    df = df.merge(df_acctblty.drop(columns=['District Name']), on='District Code', how='left')
    df = df.merge(df_perpupil.drop(columns=['District Name']), on='District Code', how='left')
    df = df.merge(df_grads.drop(columns=['District Name']), on='District Code', how='left')
    df = df.merge(df_teacher.drop(columns=['District Name']), on='District Code', how='left')
    #Rename columns 
    df.rename(columns={
    'District Name': 'district_name',
    'High Needs%' : 'high_needs_pct',
    'English Learners%' : 'english_learners_pct',
    'First Language Not English%' : 'first_language_not_english_pct',
    'Low Income%': 'low_income_pct',
    'Students with Disabilities%.1': 'students_with_disabilities_pct',
    'Overall Classification': 'overall_classification',
    'Reason for Classification': 'reason_for_classification',
    'Progress Toward Improvement Targets (%)': 'progress_toward_improvement_targets_pct',
    'In-District Expenditures': 'in_district_expenditures',
    'Total In-district FTEs': 'total_in_district_FTEs',
    'In-District Expenditures per Pupil': 'in_district_expenditures_per_pupil',
    'Total Expenditures': 'total_expenditures',
    'Total Pupil FTEs': 'total_pupil_FTEs',
    'Total Expenditures per Pupil': 'total_expenditures_per_pupil',
    '% Graduated': 'graduation_rate_pct',
    '% Still in School': 'still_in_school_pct',
    '% Non-Grad Completers': 'non_grad_completers_pct',
    '% H.S. Equiv.': 'hs_equivalency_pct',
    '% Dropped Out': 'dropout_rate_pct',
    '% Permanently Excluded': 'permanently_excluded_pct',
    'Total # of Teachers (FTE)': 'total_teachers_FTE',
    '% of Teachers Licensed': 'teachers_licensed_pct',
    'Student / Teacher Ratio': 'student_teacher_ratio',
    'Percent of Experienced Teachers': 'experienced_teachers_pct',
    'Percent of Teachers without Waiver or Provisional License': 'teachers_without_waiver_pct',
    'Percent Teaching In-Field': 'teaching_in_field_pct',
    'MEMBERS': 'members', 
    'Population': 'population', 
    'DOR Income Per Capita' : 'DOR_income_per_capita'}, inplace=True)
    is_charter = df['district_name'].str.contains('charter', case=False, na=False)
    df.loc[is_charter, 'CleanedName'] = df.loc[is_charter, 'district_name'].str.replace(r"\s*\(District\)", "", regex=True).str.strip().str.lower()

    df_charterschool['CleanedName'] = (
    df_charterschool['NAME']
    .str.lower()
    .str.replace(r"school", "", regex=True)
    .str.replace(r"\s+", " ", regex=True)  
    .str.strip()
    )


    df = df.merge(
    df_charterschool[['CleanedName', 'MEMBERS']],
    how='left',
    left_on='CleanedName',
    right_on='CleanedName'
    )


    df_townschool['DISTRICT_N'] = df_townschool['DISTRICT_N'].str.strip()
    #left join 
    df = df.merge(df_townschool[['DISTRICT_N', 'MEMBERLIST']].rename(columns={'MEMBERLIST': 'MEMBERS_townschool'}),
    how='left',
    left_on='district_name',
    right_on='DISTRICT_N',
    suffixes=('', '_townschool')
    )


    # This step will populate if the school district has more than 1 towns
    df['MEMBERS'] = df['MEMBERS'].fillna(df['MEMBERS_townschool'])
    # This step is to populate when there is only member town and the member list is empty in schooltown ds
    df['MEMBERS'] = df['MEMBERS'].fillna(df['district_name'])
    df.drop(columns='DISTRICT_N', inplace=True)
    df.drop(columns='MEMBERS_townschool', inplace=True)
    df[['Population', 'DOR Income Per Capita']] = df['MEMBERS'].apply(get_avg_stats, df_percapita=df_percapita)
    return df

def get_avg_stats(members_str, df_percapita):
    
    towns = [t.strip() for t in members_str.split(',')] if pd.notnull(members_str) else []

    matched = df_percapita[df_percapita['Municipality'].isin(towns)]
 
    if not matched.empty:
        return pd.Series({
            'Population': matched['Population'].sum(),
            'DOR Income Per Capita': matched['DOR Income Per Capita'].mean()
        })
    else:
        return pd.Series({'Population': None, 'DOR Income Per Capita': None})
    