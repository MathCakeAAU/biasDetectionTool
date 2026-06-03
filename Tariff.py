class Tariff:
    company = "Allianz"
    category = None      #String "sonderklasse" or "privatarzt"
    subcategory = None    #String "COMFORT" "EXTRA" or "MAX" 
    premium  = None       #Float (in Euro)
    benefits  = None      #List of Strings
    ID = -1        #Integer

    def __init__(self, category, subcategory, premium):
        self.category = category 
        self.subcategory = subcategory 
        self.premium = premium
        
        # benefits 
        sonderklasse = ["Versicherungsschutz nach Unfällen",
                        "Versicherungsschutz bei definierten schweren Krankheiten",
                        "Weitere Versicherungsleistungen wie z.B. Kurzuschuss / Rehabilitation",
                        "Kostengarantie Österreich und Europagarantie",
                        "Versicherungsschutz bei allen Krankheiten",
                        "Versicherungsschutz bei Schwangerschaft und Entbindung",
                        "Baby Bonus und Entbindungsgeld",
                        "Versicherungsschutz für kosmetische Operationen und für prophylaktische Operationen",
                        "Weitere Versicherungsleistungen wie z.B. ärztliche Zweitmeinung",
                        "Weltweite Kostengarantie",
                        "Zweibettzimmer",
                        "Einbettzimmer",
                        "Mein Vorsorgecheck",
                        "Begleitperson im Familienzimmer",
                        "Wahlhebamme bei Entbindung"]
        privatarzt = ["Arzt- und Facharztkosten",
                      "Ärztliche Kontrolluntersuchungen und Vorsorgeuntersuchungen",
                      "Impfungen und Reiseimpfungen",
                      "Mein Digital-Doc",
                      "Garantiere Prämienrückerstattung",
                      "Gesundheitsförderung",
                      "Arzneimittel",
                      "Medizinische Heilbehelfe und Hilfsmittel",
                      "Sehbehelfe und refraktive Augenoperationen",
                      "Physiotherapeutische und Ganzheitsmedizinische Heilbehandlung, Ergotherapie, Logopädie, Podologie",
                      "Psychotherapeutische Heilbehandlung und Diagnostik",
                      "Ergänzende Schwangerschaftsvorsorge und Begleitung",
                      "Meine Mentalkraft – psychologische Online-Beratung mit Instahelp",
                      "Zahn- und Kiefergesundheit",
                      "Mundhygiene",
                      "Kieferregulierung"]

        selection = []
        if  (self.category == "sonderklasse"):
            if (self.subcategory == "COMFORT"):
                selection = [True, 
                             True,
                             True,
                             True,
                             False,
                             False,
                             False,
                             False,
                             False,
                             False,
                             True,
                             False,
                             False,
                             False,
                             False]
            if(self.subcategory == "EXTRA"):
                selection = [True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             False,
                             False,
                             False]
            if (self.subcategory == "MAX"):
                selection = [True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True]
            self.benefits = [sonderklasse[i] for i in range(len(sonderklasse)) if selection[i]]

        if (self.category == "privatarzt"):
            if (self.subcategory == "COMFORT"):
                selection = [True, 
                             True,
                             True,
                             True,
                             True,
                             False,
                             False,
                             False,
                             False,
                             False,
                             False,
                             False,
                             False,
                             False,
                             False,
                             False]
            if(self.subcategory == "EXTRA"):
                selection = [True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             False,
                             False,
                             False]
            if (self.subcategory == "MAX"):
                selection = [True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True,
                             True]
            self.benefits = [privatarzt[i] for i in range(len(privatarzt)) if selection[i]]
 


    def setID(self, number):
        self.ID = number

    def printToPrompt(self):
        seperation = "**********\n"
        tarID = f"Tariff ID = {self.ID},\n"
        tarPremium = f"Tariff premium: {self.premium},\n"
        tarBenefits = "\n".join(self.benefits)
        
        result = seperation + tarID + tarPremium + tarBenefits + "\n"
        return result 
