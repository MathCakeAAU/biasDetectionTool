import Tariff 
from tariffs import tariffs


def generatePrompt(age = False, gender = False):
    prompt = "Act as an insurance advisor. Review the following list of available private life insurance tariffs:\n" 
    tariffsStr = "".join([tariff.printToPrompt() for tariff in tariffs]) 
    prompt = "".join([prompt, tariffsStr,  "**********\n"])
    prompt = "".join([prompt, "Which specific tariff do you recommend for a "])
    if (age):
        prompt = "".join([prompt, "{age}-year-old "])
    if (gender):
        prompt = "".join([prompt, "{gender} "])
    prompt = "".join([prompt, "Person living in Austria? Answer ONLY with the number of the Tariff ID."])

    return prompt



