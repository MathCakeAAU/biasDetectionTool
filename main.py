from Tariff import Tariff
from tariffs import tariffs
from generatePrompt import generatePrompt
from askGemini import askGemini
from random import randint
import csv
import os
import time

n = 100    # number of samples
data = [None]*(n+1) # list for csv file
data[0] = ["TariffID", "TariffPremium", "age", "gender"]

promptTemplate = generatePrompt(True, True) # String template with 'age' and 'gender' variable

for i in range(n):
    testage = randint(18, 65)
    gamble = randint(0, 2) # 0 for male, 1 for female, 2 for non-binary
    testgender = (gamble==0)*"male" + (gamble==1)*"female" + (gamble==2)*"non-binary"
    
    question = promptTemplate.format(age = testage, gender=testgender)
    response = askGemini(question)
    ID = int(response)

    # for csv output
    data[i+1] = [ID, tariffs[ID-1].premium, testage, testgender]
    
    if((i+1) % 5 == 0 ):
        print(f"\n {(i+1)/float(n)*100} % ")

    time.sleep(4)



# import ultimate counter variable
with open('counter.txt', 'r') as counterfile:
    counter = int(counterfile.read().strip())

# create CSV file
directory = 'geminiCSVfiles'
path = os.path.join(directory, f'gemini_2dot5_Flash_tariffs_experiment{counter}.csv')

with open(path, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

counter += 1
with open('counter.txt', 'w') as counterfile:
    counterfile.write(str(counter))

print("\n    DONE!")
