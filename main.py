import pandas as pd
import numpy as np

def create_dataframe():
    try:
        dataframe = pd.read_csv('data.csv')
        return dataframe
    except FileNotFoundError:
        data = {
            'Имя': [
            "Иван Петров",
            "Мария Смирнова",
            "Александр Иванов",
            "Анна Кузнецова",
            "Дмитрий Попов",
            "Екатерина Васильева",
            "Сергей Соколов",
            "Ольга Михайлова",
            "Алексей Новиков",
            "Татьяна Федорова"
        ],
            'Математика': np.random.randint(2, 6, 10),
            'Физика': np.random.randint(2, 6, 10),
            'Химия': np.random.randint(2, 6, 10),
            'Биология': np.random.randint(2, 6, 10),
            'История': np.random.randint(2, 6, 10),
        }

        dataframe = pd.DataFrame(data)
        dataframe.to_csv('data.csv', index=False)
        return dataframe

df = create_dataframe()

print(df.head())

avg_math = df['Математика'].mean()
avg_physics = df['Физика'].mean()
avg_chemistry = df['Химия'].mean()
avg_bio = df['Биология'].mean()
avg_history = df['История'].mean()

median_math = df['Математика'].median()
median_physics = df['Физика'].median()
median_chemistry = df['Химия'].median()
median_bio = df['Биология'].median()
median_history = df['История'].median()

Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)

IQR_math = Q3_math - Q1_math

std_deviation = df.iloc[:, 1:].std()

print(f'Средний балл по математике - {avg_math}, медиана - {median_math}')
print(f'Средний балл по физике - {avg_physics}, медиана - {median_physics}')
print(f'Средний балл по химии - {avg_chemistry}, медиана - {median_chemistry}')
print(f'Средний балл по биологии - {avg_bio}, медиана - {median_bio}')
print(f'Средний балл по истории - {avg_history}, медиана - {median_history}')
print(f'Q1_math = {Q1_math}, Q3_math = {Q3_math}, IQR_math = {IQR_math}')
print(f'Среднее отклонение:\n{std_deviation}')