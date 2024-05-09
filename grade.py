import pandas as pd
import os

def kid_grade(score):
    if score >= 80:
        return 'A'
    elif score >= 70:
        return 'B'
    elif score >= 60:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'F'

def sai_grades(file):
 
    df = pd.read_excel(file)

    df['คะแนน'] = pd.to_numeric(df['คะแนน'], errors='coerce')
    
    df['เกรด'] = df['คะแนน'].apply(kid_grade)
  
    df.sort_values(by='คะแนน', inplace=True, ascending=False)
    
    df.to_excel(file ,index=False)

    print('Success')

    os.system('start excel.exe {}'.format(file))

sai_grades('grades_with_grades.xlsx')
