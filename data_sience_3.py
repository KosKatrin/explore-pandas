import pandas as pd
df = pd.read_csv('GoogleApps.csv')

# 1 Сколько всего приложений с категорией ('Category') 'BUSINESS'?
print(df['Category'].value_counts())

# 2 Чему равно соотношение количества приложений для подростков ('Teen') и для детей старше 10 ('Everyone 10+')?
# Ответ запиши с точностью до сотых.
temp = df['Content Rating'].value_counts()
print(round(temp['Teen'] / temp['Everyone 10+'], 3))


# 3.1 Чему равен средний рейтинг ('Rating') платных ('Paid') приложений? 
# Ответ запиши с точностью до сотых.

# с помощью фильтрации данных
print(round(df[df['Type'] == 'Paid']['Rating'].mean(), 2))

# c помощью метода groupby
temp = df.groupby('Type')['Rating'].mean()
print(round(temp['Paid'], 2))


# 3.2 На сколько средний рейтинг ('Rating') бесплатных ('Free') приложений меньше среднего рейтинга платных ('Paid')?
# Ответ запиши с точностью до сотых.

# с помощью фильтрации данных
print(round(df[df['Type'] == 'Paid']['Rating'].mean() - df[df['Type'] == 'Free']['Rating'].mean(), 2))

# c помощью метода groupby
print(round(temp['Paid'] - temp['Free'], 2))


# 4 Чему равен минимальный и максимальный размер ('Size') приложений в категории ('Category') 'COMICS'?
# Запиши ответы с точностью до сотых.

# с помощью группировки
print(round(df.groupby('Category')['Size'].agg(['min', 'max']), 2))

# с помощью фильтрации данных
print(round(df[df['Category'] == 'COMICS']['Size'].agg(['min', 'max']), 2))


# Бонус 1. Сколько приложений с рейтингом ('Rating') строго больше 4.5 в категории ('Category') 'FINANCE'?
#не работает
#print(df[(df['Category'] == 'FINANCE') & (df['Rating'] > 4.5)])

print(df[df['Rating'] > 4.5]['Category'].value_counts())


# Бонус 2. Чему равно соотношение бесплатных ('Free') и платных ('Paid') игр с рейтингом ('Rating') больше 4.9?
temp = df[(df['Rating'] > 4.9) & (df['Category'] == 'GAME')]['Type'].value_counts()
print(temp['Free'] / temp['Paid'])
