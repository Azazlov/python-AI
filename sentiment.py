from transformers import pipeline

# Загружаем модель (автоматически кэшируется)
classifier = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest",
    tokenizer="cardiffnlp/twitter-roberta-base-sentiment-latest",
    top_k=1  # эквивалент старому return_all_scores=False
)

def get_sentiment(text: str) -> str:
    result = classifier(text)[0]  # [{'label': 'negative', 'score': 0.99}]
    return result[0]['label']  # уже 'negative', 'neutral' или 'positive'

# Примеры
print(get_sentiment("Я в очень плохом настроении"))      # negative
print(get_sentiment("Нормально так, ничего особенного"))  # neutral
print(get_sentiment("Отлично! Спасибо, всё работает!"))  # positive