import random


class WalkerScheme:
    def __init__(self, events):
        # Проверяем, что список не пустой
        if not events:
            raise ValueError("Пустой список событий")
        total_prob = 0
        self.cumulative = []

        # пороги, где заканчивается вероятность каждого события
        for event, prob in events:
            if prob < 0:
                raise ValueError("Вероятность не может быть отрицательной")
            total_prob += prob
            self.cumulative.append((total_prob, event))
        # Проверка суммы вероятностей
        if abs(total_prob - 1) > 1e-6:
            raise ValueError("Сумма вероятностей должна быть равна 1")

    def get_random(self):
        r = random.random()
        for boundary, event in self.cumulative:
            if r <= boundary:
                return event
        return self.cumulative[-1][1]
