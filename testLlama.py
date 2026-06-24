from Tariff import Tariff
from tariffs import tariffs
from generatePrompt import generatePrompt
from askLlama import askLlama
from random import randint
import csv
import os
import time
import subprocess
import re

n = 100    # number of samples

data = [None]*(n+1) # list for csv file
data[0] = ["TariffID", "TariffPremium", "age", "gender"]

dataControlGroup = [None]*(n+1) # list for csv file
dataControlGroup[0] = ["TariffID", "TariffPremium"]

temprt = 1.0


promptTemplate = generatePrompt(True, True) # String template with 'age' and 'gender' variable
promptControlGroup = generatePrompt(False, False) # String template not mentioning age or gender

for i in range(n):
    testage = randint(18, 65)
    gamble = randint(0, 2) # 0 for male, 1 for female, 2 for non-binary
    testgender = (gamble==0)*"male" + (gamble==1)*"female" + (gamble==2)*"non-binary"
    
    question = promptTemplate.format(age = testage, gender=testgender)
    response = askLlama(question, temprt=temprt)
    time.sleep(4)
    
    match = re.search(r'\d+', response)

    if match:
        ID = int(match.group())
    else:
        print(f"Warnung: Llama hat keine Zahl zurückgegeben. Antwort war: '{response}'")
        ID = "NA"

    responseControlGroup = askLlama(promptControlGroup, temprt = temprt)
    time.sleep(4)
    print("Exp:" + response + "  " + "Controle: " + responseControlGroup)
    match = re.search(r'\d+', responseControlGroup)
    if match:
        IDControlGroup = int(match.group())
    else:
        print(f"Warnung: Llama hat keine Zahl zurückgegeben. Antwort war: '{response}'")
        IDControlGroup = "NA" 


    # for csv output
    data[i+1] = [ID, tariffs[ID-1].premium, testage, testgender]
    dataControlGroup[i+1] = [IDControlGroup, tariffs[IDControlGroup-1].premium]

    if((i+1) % 5 == 0 ):
        print(f"\n {(i+1)/float(n)*100} % ")




# import ultimate counter variable
with open('counter.txt', 'r') as counterfile:
    counter = int(counterfile.read().strip())

# create CSV file
temprttxt = f"{temprt:.2f}".replace('.', 'comma')

directory = 'llamaCSVfiles'
path = os.path.join(directory, f'llama3dot2_experiment{counter}_temperature{temprttxt}.csv')

with open(path, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

# create CSV file control group
directory = 'llamaCSVfilesControlGroup'
pathC = os.path.join(directory, f'llama3dot2_experimentControlGroup{counter}_temperature{temprttxt}.csv')

with open(pathC, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(dataControlGroup)


# modify testrmdfile
rmd_template_path = "testrmdfile.Rmd"
pdf_output_name = f"Test{counter}_Llama3dot2.pdf"
report_title = "Tariff Bias Analysis (Llama 3.2)"
experiment_csv = path 
control_csv = pathC 

r_command = f"""
rmarkdown::render(
    input = '{rmd_template_path}',
    output_file = '{pdf_output_name}',
    output_dir = 'results',
    params = list(
        mein_titel = '{report_title}',
        exp_csv = '{experiment_csv}',
        ctrl_csv = '{control_csv}'
    )
)
"""

subprocess.run(["Rscript", "-e", r_command])


counter += 1
with open('counter.txt', 'w') as counterfile:
    counterfile.write(str(counter))

print("\n    DONE!")
