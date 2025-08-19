# Pandas импортирована, но не используется. Плохо влияет на чистоту кода и може привести к проблемам с производительностью.

import pandas as pd
from src.data import load_data
# Ожидается разделение на 2 строки. Лучшие практики оформления кода
def test_load_data():
    df = load_data("data/uber.csv")
    assert not df.empty
