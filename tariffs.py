from Tariff import Tariff

__all__ = ['tariffs']

tariffs = [Tariff("sonderklasse", "COMFORT", 46.63),
           Tariff("sonderklasse", "EXTRA", 114.48),
           Tariff("sonderklasse", "MAX", 160.33),
           Tariff("privatarzt", "COMFORT", 37.67),
           Tariff("privatarzt", "EXTRA", 82.90),
           Tariff("privatarzt", "MAX", 119.35)]
tariffs.sort(key=lambda tar: tar.premium)

count = 1
for tariff in tariffs:
    tariff.ID = count
    count += 1

