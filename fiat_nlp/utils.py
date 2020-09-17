from .cars import CARS


def parse_entities(data):
    entities = []
    for entity in data["entities"]:
        data = {
            "entity": entity["type"],
            "sentiment": entity["sentiment"]["score"],
            "mention": entity["text"],
        }
        entities.append(data)
    return entities


class Recommendation:
    """Logic to recommend a car model based on NLU information."""

    def __init__(self, current_car, entities):
        self.current_car = self.set_model(current_car)
        self.worst = self.get_worst_sentiment(entities)

    def set_model(self, car):
        model = car.replace(" ", "").upper()
        return model

    def get_worst_sentiment(self, entities):
        if entities:
            worst = min(entities, key=lambda x: x["sentiment"])
            if worst["sentiment"] < 0:
                return worst
        return None

    def get(self):
        if self.worst:
            return self.get_recommendation()
        return ""

    def get_recommendation(self):
        if self.current_car in CARS.keys():
            CARS.pop(self.current_car)
        worst_entity = self.worst["entity"]
        best_car = max(CARS.values(), key=lambda x: x[worst_entity])
        return best_car["MODELO"]
