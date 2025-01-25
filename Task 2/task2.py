import json
from collections import defaultdict

# Функция для анализа данных
def analyze_data(file_path):
    category_count = defaultdict(int)
    category_sum = defaultdict(int)

    with open(file_path, 'r') as file:
        data = json.load(file)

        for item in data:
            category = item['category']
            price = item['price']

            category_count[category] += 1
            category_sum[category] += price

    return category_count, category_sum

# Основной запуск программы
if __name__ == "__main__":
    file_path = "f.json"  # Замените на путь к вашему файлу

    category_count, category_sum = analyze_data(file_path)

    print("Количество предметов по категориям:", dict(category_count))
    print("Общая сумма продаж по категориям:", dict(category_sum))
