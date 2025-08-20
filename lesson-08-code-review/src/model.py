from sklearn.ensemble import GradientBoostingRegressor


class TaxiFareModel:
    def __init__(self):
        self.model = GradientBoostingRegressor()

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
# Нет новой строки в конце файла. Влияет на совместимость и читабельность. Необходимо ее добавить.