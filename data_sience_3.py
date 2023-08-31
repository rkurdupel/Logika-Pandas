import pandas as pd
df = pd.read_csv('GoogleApps.csv')

# 1 Скільки всього програм з категорією ('Category') 'BUSINESS'?

# 2 Чому дорівнює співвідношення кількості додатків для підлітків ('Teen') і для дітей старше 10 ('Everyone 10+')?
# Відповідь запиши з точністю до сотих.

# 3.1 Чому дорівнює середній рейтинг ('Rating') платних ('Paid') додатків?
# Відповідь запиши з точністю до сотих.

# 3.2 На скільки середній рейтинг ('Rating') безкоштовних ('Free') додатків менший за середній рейтинг платних ('Paid')?
# Відповідь запиши з точністю до сотих.

# 4 Чому дорівнює мінімальний та максимальний розмір ('Size') додатків у категорії ('Category') 'COMICS'?
# Запиши відповіді з точністю до сотих.
min = df[df["Category"] == "COMICS"]["Size"].min()
max = df[df["Category"] == "COMICS"]["Size"].max()
print(min, max)


# Бонус 1. Скільки додатків з рейтингом ('Rating') більше 4.5 у категорії ('Category') 'FINANCE'?
print(len(df[(df["Category"] == "FINANCE") & (df["Rating"] > 4.5)]["App"]))



# Бонус 2. Чому дорівнює співвідношення безкоштовних ('Free') і платних ('Paid') ігор з рейтингом ('Rating') більше 4.9?
free = df[(df["Type"] == "Free") & (df["Rating"] > 4.9) & (df["Category"] == "GAME")]
paid = df[(df["Type"] == "Paid") & (df["Rating"] > 4.9) & (df["Category"] == "GAME")]
print(len(free) / len(paid))    # len() to get amount length

