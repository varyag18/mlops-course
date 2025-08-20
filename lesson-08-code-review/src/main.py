# Обе функции импортированы, но не используются. Плохо влияет на чистоту кода и може привести к проблемам с производительностью. Рекомендую их брать из кода
import os
import pandas as pd
# Рекомендуется минимизировать использование глобальных переменных и предпочитать передачу данных через аргументы функций и возврат значений. Использование глобальных перемен усложняет отладку и приводит к конфликтам имен.
from src.data import load_data, split_data
from src.features import add_time_features
from src.model import TaxiFareModel

# Глобальная переменная. Рекомендую указать правильный путь до uber.csv.
DATA_PATH = "data/main.csv"

# Загрузка и обработка данных
raw_data = load_data(DATA_PATH)
processed_data = add_time_features(raw_data)
X_train, X_test, y_train, y_test = split_data(processed_data)

# Обучение модели
model = TaxiFareModel()
model.fit(X_train, y_train)

# Оценка
score = model.model.score(X_test, y_test)
print(f"R²: {score:.2f}")
# Нет новой строки в конце файла. Влияет на совместимость и читабельность. Необходимо ее добавить.