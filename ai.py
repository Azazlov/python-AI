from transformers import AutoModelForCausalLM, AutoTokenizer

# Глобальные переменные для модели и токенизатора
_model = None
_tokenizer = None

def load_model(model_name: str = "Qwen/Qwen3-0.6B"):
    """Загружает модель и токенизатор один раз и сохраняет в глобальные переменные."""
    global _model, _tokenizer
    if _model is None or _tokenizer is None:
        print("Загрузка модели и токенизатора...")
        _tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
        _model = AutoModelForCausalLM.from_pretrained(
            model_name,
            dtype="auto",
            device_map="auto",
            trust_remote_code=True
        )
        print("Модель загружена.")
    return _model, _tokenizer

def chat_with_model(prompt: str, max_new_tokens: int = 2048):
    """
    Генерирует ответ модели на заданный промпт.
    
    Возвращает словарь:
    {
        "thinking": "...",  # (может быть пустым)
        "content": "..."
    }
    """
    global _model, _tokenizer
    if _model is None or _tokenizer is None:
        raise RuntimeError("Модель не загружена. Вызовите load_model() сначала.")

    # Формируем сообщение в формате чата
    messages = [{"role": "user", "content": prompt}]
    
    # Применяем шаблон чата
    text = _tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=True  # Включаем режим размышлений
    )

    # Токенизируем
    model_inputs = _tokenizer([text], return_tensors="pt").to(_model.device)

    # Генерация
    generated_ids = _model.generate(
        **model_inputs,
        max_new_tokens=max_new_tokens,
        pad_token_id=_tokenizer.eos_token_id
    )

    # Отделяем сгенерированный ответ от входного промпта
    input_length = model_inputs.input_ids.shape[1]
    output_ids = generated_ids[0][input_length:].tolist()

    # Идентификатор токена </think> (может отличаться — убедитесь!)
    THINK_END_TOKEN_ID = 151668

    # Извлекаем thinking и content
    try:
        # Ищем последнее вхождение </think>
        reversed_output = output_ids[::-1]
        pos = reversed_output.index(THINK_END_TOKEN_ID)
        index = len(output_ids) - pos
    except ValueError:
        # Токен </think> не найден — весь вывод считаем основным контентом
        index = 0

    thinking_ids = output_ids[:index]
    content_ids = output_ids[index:]

    thinking_content = _tokenizer.decode(thinking_ids, skip_special_tokens=True).strip()
    content = _tokenizer.decode(content_ids, skip_special_tokens=True).strip()

    return {
        "thinking": thinking_content,
        "content": content
    }

if __name__=='__main__':
    load_model()
    import sys
    import time
    import threading
    from loading import loading_animation
    while True:
        prompt = input('Запрос: ')
        stop_loading = threading.Event()
        loader_thread = threading.Thread(target=loading_animation, args=(stop_loading, "Обработка"))
        loader_thread.start()
        result = chat_with_model(prompt=prompt)
        think = result['thinking']
        content = result['content']
        stop_loading.set()
        loader_thread.join()
        print(f'Мысли: {think}')
        print(f'Ответ: {content}')