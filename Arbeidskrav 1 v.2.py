BF = 7500
# Forsikring bensinbil pa
EF = 5000
# Forsikring elbil pa
TF = 8.38 * 365
# Trafikkforsikringsavgift per dag * 365 dager pa
BD = 1 * 10000
# Drivstoffpris per km * 10 000 km
ED = (0.2 * 10000) * 2
# Strømforbruk per km * 10 000 km * pris
BB = 0.3 * 10000
# Bomavgift per km * 10 000 km
EB = 0.1 * 10000
# Bomavgift per km * 10 000 km
Elbil_kostnad_pa = EF + TF + ED + EB
Bensinbil_kostnad_pa = BF + TF + BD + BB
print ("Elbil_kostnad_pa =", Elbil_kostnad_pa, "Bensinbil_kostnad_pa", Bensinbil_kostnad_pa)
print ("Differanse_kostnad_pa =", Bensinbil_kostnad_pa - Elbil_kostnad_pa)

