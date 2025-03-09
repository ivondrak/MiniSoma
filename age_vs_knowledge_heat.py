import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Načtení Excel souboru (změň cestu podle umístění souboru)
file_path = "survey-data-technotrasa.xlsx"  # Uprav podle potřeby
xls = pd.ExcelFile(file_path)
df = xls.parse(xls.sheet_names[0])

# Zkontroluj názvy sloupců
print(df.columns)

# Vyber relevantní sloupce
age_column = "Jaký je Váš věk?"  # Uprav podle názvu ve tvém souboru
awareness_column = "Jak hodnotíte Vaše povědomí o zážitkové trase s názvem Technotrasa v Moravskoslezském kraji?"  # Uprav podle názvu

# Zkontroluj hodnoty ve sloupcích
print(df[age_column].value_counts())
print(df[awareness_column].value_counts())

# Vytvoření kontingenční tabulky
pivot_table = pd.crosstab(df[age_column], df[awareness_column])

# Vytvoření heatmapy
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table, annot=True, fmt="d", cmap="coolwarm", cbar=True)
plt.xlabel("Povědomí o Technotrase")
plt.ylabel("Věk respondentů")
plt.title("Heatmapa vztahu mezi věkem a povědomím o Technotrase")
plt.xticks(rotation=45)
plt.yticks(rotation=0)

# Nastavení většího okraje nalevo
plt.gcf().subplots_adjust(left=0.3, right=0.9, top=0.9, bottom=0.2)

plt.show()