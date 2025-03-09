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

# Vytvoření boxplotu pro analýzu vztahu mezi věkem a povědomím o Technotrase
plt.figure(figsize=(10, 6))
sns.boxplot(x=awareness_column, y=age_column, data=df, palette="coolwarm")
plt.xlabel("Povědomí o Technotrase")
plt.ylabel("Věk respondentů")
plt.title("Vztah mezi věkem a povědomím o Technotrase")
plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()