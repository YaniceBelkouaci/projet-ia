import numpy as np
import pandas as pd

# Données : Heures de révision vs Note
data = {
    'Heures_Revision': [1, 2, 5, 10, 15, 20],
    'Note_Examen': [5, 8, 12, 15, 18, 20]
}

df = pd.DataFrame(data)

print("--- Tes données de révision ---")
print(df)

# Calcul de la corrélation (Maths : Coefficient de Pearson)
correlation = df['Heures_Revision'].corr(df['Note_Examen'])
print(f"\nIndice de corrélation : {correlation:.2f}")

if correlation > 0.9:
    print("Résultat : Corrélation forte détectée !")