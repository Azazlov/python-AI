from flask import Flask, request, render_template
from ai import chat_with_model, load_model
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
load_model()

messages = []

@app.route('/')
def home():
    return render_template('index.html', messages=messages)

# Добавить еще один роутинг с qr-кодом на гитхаб

@app.route('/req', methods=['POST'])
def req():
    req = request.form.get('req')
    print(f'Получен запрос: {req}')
    # True изменить на получение состояния checkbox в html
    result = loading(chat_with_model, req, True)
    print(f'Запрос обработан')
    think = result['thinking']
    content = result['content']
    messages.append([req, think, content])
    print(f'Отправляю результат')

    return home()

app.run(debug=True, host="0.0.0.0", port=5005)