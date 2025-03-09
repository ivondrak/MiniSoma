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
    "Znáte zážitkovou trasu s názvem Technotrasa v Moravskoslezském kraji? x Ano ",
    "Znáte zážitkovou trasu s názvem Technotrasa v Moravskoslezském kraji? x Ne",
    "Znáte zážitkovou trasu s názvem Technotrasa v Moravskoslezském kraji? x Rádio",
    "Znáte zážitkovou trasu s názvem Technotrasa v Moravskoslezském kraji? x Webové stránky Technotrasy",
    "Znáte zážitkovou trasu s názvem Technotrasa v Moravskoslezském kraji? x Od přátel nebo rodiny",
    "Znáte zážitkovou trasu s názvem Technotrasa v Moravskoslezském kraji? x Informační letáky nebo plakáty",
    "Znáte zážitkovou trasu s názvem Technotrasa v Moravskoslezském kraji? x Sociální sítě",
    "Znáte zážitkovou trasu s názvem Technotrasa v Moravskoslezském kraji? x Turistická informační centra",
    "Znáte zážitkovou trasu s názvem Technotrasa v Moravskoslezském kraji? x Jiné"
]

# Vytvoření kontingenční tabulky
pivot_table = pd.DataFrame()

for col in info_columns:
    pivot_table[col.replace("Znáte zážitkovou trasu s názvem Technotrasa v Moravskoslezském kraji? x ", "")] = df[age_columns].multiply(df[col], axis=0).sum()

# Vytvoření heatmapy
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table.T, annot=True, fmt="d", cmap="coolwarm", cbar=True)
plt.xlabel("Věk respondentů")
plt.ylabel("Znalost o Technotrase")
plt.title("Heatmapa vztahu mezi věkem a znalostí o Technotrase")
plt.yticks(rotation=0)

# Nastavení většího okraje nalevo
plt.gcf().subplots_adjust(left=0.3, right=0.9, top=0.9, bottom=0.2)

plt.show()