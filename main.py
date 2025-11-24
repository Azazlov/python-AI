from flask import Flask, request, render_template
from ai import QwenChatbot
from loading import loading


# ДОПИСАТЬ ФУНКЦИЮ ВЫГРУЗКИ СООБЩЕНИЙ В ПЕРЕМЕННУЮ messages ПРИ ЗАПУСКЕ СЕРВЕРА
# def read_messages():
#     with open('messages.json', 'r+') as file:
#         messages_JSON = file.read()
        
#     return messages

#  ДОПИСАТЬ ФУНКЦИЮ СОХРАНЕНИЯ СООБЩЕНИЙ В ФАЙЛ .JSON
# def write_messages():
#     with open('messages.json', 'w+') as file:
#         file.write(messages_JSON)

app = Flask(__name__)
chatbot = QwenChatbot()

messages = []

@app.route('/')
def home():
    return render_template('index.html', messages=messages)

# Добавить еще один роутинг на страницу с qr-кодом на гитхаб (свой)

@app.route('/req', methods=['POST'])
def req():
    req = request.form.get('req')
    # добавить переменную, получающую данные из формы по имени 'check'
    print(f'Получен запрос: {req}')
    # вывести 'Запрошено мышление: [Да/Нет]
    # при "Да" изменить запрос, добавив в конце /think, при "Нет" добавить на конце /no_think
    result = loading(chatbot.generate_response, req)
    print(f'Запрос обработан')
    # think = ????
    content = result
    messages.append([req, '', content])
    # метод добавления списка в список заменить на добавление словаря в список
    # примеры ключей: 'request', 'thinking', 'content'
    print(f'Отправляю результат')

    return home()

# добавить роутинг, возвращающий страницу для шифрования текста для переписок в макс (по желанию)

app.run(debug=True, host="0.0.0.0", port=5005)