# card_manager.py

class CardManager:
    def __init__(self):
        # Імітація бази даних карток: (id, category, text, age_rating)
        self.cards = [
            (1, "Світська бесіда", "Прогноз погоди на завтра чудовий.", 12),
            (2, "Світська бесіда", "Штучний інтелект розвивається шаленими темпами.", 16),
            (3, "Побачення", "Перша кінокартина тривала всього 2 секунди.", 16),
            (4, "Бізнес", "Продажі компанії зросли на 200%.", 18),
        ]

    def filter_cards(self, category: str, user_age: int) -> list:
        """Метод 1: Фільтрація карток за категорією та віковим обмеженням."""
        if not category or user_age < 0:
            raise ValueError("Некоректні вхідні дані")
        
        result = []
        for card_id, cat, text, rating in self.cards:
            if cat == category and user_age >= rating:
                result.append(text)
        return result

    def calculate_reading_time(self, text: str) -> float:
        """Метод 2: Розрахунок часу читання картки (слів за секунду)."""
        if not text:
            return 0.0
        
        words = text.split()
        word_count = len(words)
        
        # Середня швидкість: 3 слова на секунду
        reading_time = word_count / 3.0
        return round(reading_time, 2)

    def get_premium_content(self, is_premium: bool, tokens: int) -> str:
        """Метод 3: Доступ до преміум-тем на основі підписки або токенів."""
        if is_premium:
            return "Повний доступ до преміум-контенту"
        
        if tokens >= 5:
            return "Одноразовий доступ за токени"
        elif 0 <= tokens < 5:
            return "Недостатньо токенів для доступу"
        else:
            raise ValueError("Кількість токенів не може бути негативною")