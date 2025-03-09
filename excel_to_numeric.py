import pandas as pd

# Load the dataset
file_path = "survey-data-technotrasa.xlsx"  # Change to your file path
xls = pd.ExcelFile(file_path)
df = xls.parse(xls.sheet_names[0])

# Transform column A (age groups)
age_groups = [
    "18 - 24 let", 
    "25 - 34 let", 
    "35 - 44 let",
    "45 - 54 let",
    "55 - 64 let",
    "65 a více let"
]

# Assign values to age group columns
for group in age_groups:
    df[group] = df['Jaký je Váš věk?'].apply(lambda x: 1 if group in x else 0)

# Drop the original age column
df.drop(columns=['Jaký je Váš věk?'], inplace=True)

# Transform column B (gender)
df['Muž'] = df['Jaké je Vaše pohlaví?'].apply(lambda x: 1 if x == 'Muž' else 0)
df['Žena'] = df['Jaké je Vaše pohlaví?'].apply(lambda x: 1 if x == 'Žena' else 0)

# Drop the original gender column
df.drop(columns=['Jaké je Vaše pohlaví?'], inplace=True)

# Transform column C (employment type)
employment_types = df['Jaká je Vaše současná profesní nebo studijní situace?'].unique()
for employment in employment_types:
    df[employment] = df['Jaká je Vaše současná profesní nebo studijní situace?'].apply(lambda x: 1 if x == employment else 0)

# Drop the original gender column
df.drop(columns=['Jaká je Vaše současná profesní nebo studijní situace?'], inplace=True)

# Transform column D (regions)
regions = df['V jakém kraji žijete?'].unique()
for region in regions:
    df[region] = df['V jakém kraji žijete?'].apply(lambda x: 1 if x == region else 0)

# Drop the original region column
df.drop(columns=['V jakém kraji žijete?'], inplace=True)

# Drop column E
df.drop(columns=['Kde v současnosti žijete? '], inplace=True)

# Transform column U (subconscious types)
subconscious_types = df['Jak hodnotíte Vaše povědomí o zážitkové trase s názvem Technotrasa v Moravskoslezském kraji?'].unique()
for subconscious in subconscious_types:
    df[subconscious] = df['Jak hodnotíte Vaše povědomí o zážitkové trase s názvem Technotrasa v Moravskoslezském kraji?'].apply(lambda x: 1 if x == subconscious else 0)

# Drop the original subconscious column
df.drop(columns=['Jak hodnotíte Vaše povědomí o zážitkové trase s názvem Technotrasa v Moravskoslezském kraji?'], inplace=True)

# Replace "Ano" with 1, "Ne" with 0, and "Nejsem si jistý/á" with 0.5
df.replace({"Ano": 1, "Ano " : 1, "Ne": 0, "Nejsem si jistý/á": 0.5}, inplace=True)

# Convert all columns to numeric, forcing errors to NaN
df_numeric = df.apply(pd.to_numeric, errors='coerce')

# Save the converted dataframe to a new Excel file
df_numeric.to_excel("survey-data-technotrasa-numeric.xlsx", index=False)

print("Conversion to numeric values completed and saved to 'survey-data-technotrasa-numeric.xlsx'.")