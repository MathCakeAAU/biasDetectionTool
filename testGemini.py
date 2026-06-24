from Tariff import Tariff
from tariffs import tariffs
from generatePrompt import generatePrompt
from askGemini import askGemini
from random import randint
import csv
import os
import time
import subprocess

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
    response = askGemini(question, temprt=temprt)
    time.sleep(4)

    ID = int(response)

    responseControlGroup = askGemini(promptControlGroup, temprt = temprt)
    time.sleep(4)

    IDControlGroup = int(responseControlGroup)

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

directory = 'geminiCSVfiles'
path = os.path.join(directory, f'gemini_3dot1_Flash_Lite_tariffs_experiment{counter}_temperature{temprttxt}.csv')

with open(path, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

# create CSV file control group
directory = 'geminiCSVfilesControlGroup'
pathC = os.path.join(directory, f'gemini_3dot1_Flash_Lite_tariffs_experimentControlGroup{counter}_temperature{temprttxt}.csv')

with open(pathC, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(dataControlGroup)


# modify testrmdfile
rmd_template_path = "testrmdfile.Rmd"
pdf_output_name = f"Test{counter}_Gemini.pdf"
report_title = "Tariff Bias Analysis (Gemini 3.1 Flash Lite)"
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
