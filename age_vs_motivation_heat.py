import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Načtení Excel souboru (změň cestu podle umístění souboru)
file_path = "survey-data-technotrasa-numeric.xlsx"  # Uprav podle potřeby
xls = pd.ExcelFile(file_path)
df = xls.parse(xls.sheet_names[0])

# Zkontroluj názvy sloupců
print(df.columns)

# Vyber relevantní sloupce
age_columns = [
    "18 - 24 let", 
    "25 - 34 let", 
    "35 - 44 let",
    "45 - 54 let",
    "55 - 64 let",
    "65 a více let"
]
info_columns = [
    "Co Vás motivuje k návštěvě turistické destinace? x Historické a kulturní památky",
    "Co Vás motivuje k návštěvě turistické destinace? x Přírodní krásy a krajiny",
    "Co Vás motivuje k návštěvě turistické destinace? x Místní gastronomické speciality",
    "Co Vás motivuje k návštěvě turistické destinace? x Dobrodružné aktivity a zážitky",
    "Co Vás motivuje k návštěvě turistické destinace? x Různé formy odpočinku a relaxace",
    "Co Vás motivuje k návštěvě turistické destinace? x Nákupy a místní produkty",
    "Co Vás motivuje k návštěvě turistické destinace? x Jiné "
]

# Vytvoření kontingenční tabulky
pivot_table = pd.DataFrame()

for col in info_columns:
    pivot_table[col.replace("Co Vás motivuje k návštěvě turistické destinace? x ", "")] = df[age_columns].multiply(df[col], axis=0).sum()

# Vytvoření heatmapy
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table.T, annot=True, fmt="d", cmap="coolwarm", cbar=True)
plt.xlabel("Věk respondentů")
plt.ylabel("Motivace k návštěvě turistické destinace")
plt.title("Heatmapa vztahu mezi věkem a motivací k návštěvě turistické destinace")
plt.xticks(rotation=45)
plt.yticks(rotation=0)

# Nastavení většího okraje nalevo
plt.gcf().subplots_adjust(left=0.3, right=0.9, top=0.9, bottom=0.2)

plt.show()