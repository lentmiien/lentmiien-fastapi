class DummyModel:
    def predict(self, data):
        return [x * 2 for x in data]
