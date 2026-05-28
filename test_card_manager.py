# test_card_manager.py
import pytest
from card_manager import CardManager

# Arrange (Глобальне налаштування для тестів)
@pytest.fixture
def manager():
    return CardManager()

# --- ТЕСТИ ДЛЯ МЕТОДУ 1: filter_cards ---

def test_filter_cards_success(manager):
    # Arrange
    category = "Світська бесіда"
    age = 20
    # Act
    result = manager.filter_cards(category, age)
    # Assert
    assert len(result) == 2  # [EP / Позитивний]
    assert "Прогноз погоди на завтра чудовий." in result

def test_filter_cards_border_age(manager):
    # Arrange
    category = "Світська бесіда"
    age = 12
    # Act
    result = manager.filter_cards(category, age)
    # Assert
    assert len(result) == 1  # [BVA / Позитивний]

def test_filter_cards_underage(manager):
    # Arrange
    category = "Світська бесіда"
    age = 11
    # Act
    result = manager.filter_cards(category, age)
    # Assert
    assert len(result) == 0  # [BVA / Негативний]

def test_filter_cards_invalid_age(manager):
    # Arrange & Act & Assert
    with pytest.raises(ValueError):
        manager.filter_cards("Бізнес", -5)  # [EP / Негативний]


# --- ТЕСТИ ДЛЯ МЕТОДУ 2: calculate_reading_time ---

def test_calculate_time_normal_text(manager):
    # Arrange
    text = "Один два три"
    # Act
    result = manager.calculate_reading_time(text)
    # Assert
    assert result == 1.0  # [EP / Позитивний]

def test_calculate_time_empty_text(manager):
    # Arrange
    text = ""
    # Act
    result = manager.calculate_reading_time(text)
    # Assert
    assert result == 0.0  # [BVA / Позитивний]


# --- ТЕСТИ ДЛЯ МЕТОДУ 3: get_premium_content ---

def test_premium_user_has_access(manager):
    # Arrange
    is_premium = True
    tokens = 0
    # Act
    result = manager.get_premium_content(is_premium, tokens)
    # Assert
    assert result == "Повний доступ до преміум-контенту"  # [EP / Позитивний]

def test_premium_border_tokens_enough(manager):
    # Arrange
    is_premium = False
    tokens = 5
    # Act
    result = manager.get_premium_content(is_premium, tokens)
    # Assert
    assert result == "Одноразовий доступ за токени"  # [BVA / Позитивний]

def test_premium_border_tokens_not_enough(manager):
    # Arrange
    is_premium = False
    tokens = 4
    # Act
    result = manager.get_premium_content(is_premium, tokens)
    # Assert
    assert result == "Недостатньо токенів для доступу"  # [BVA / Негативний]

def test_premium_negative_tokens(manager):
    # Arrange & Act & Assert
    with pytest.raises(ValueError):
        manager.get_premium_content(False, -1)  # [EP / Негативний]