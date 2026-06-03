#from tariffs import tariffs
#from generatePrompt import generatePrompt
#from askGemini import askGemini
import os
import csv
data = [[1]]*10
with open('counter.txt', 'r') as counterfile:
    counter = int(counterfile.read().strip())

directory = 'geminiCSVfiles'
path = os.path.join(directory, f'gemini_2dot5_Flash_tariffs_experiment{counter}.csv')

with open(path, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

counter += 1
with open('counter.txt', 'w') as counterfile:
    counterfile.write(str(counter))



