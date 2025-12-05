import sys
import time
import threading

def loading_animation(stop_event, message="Загрузка", result='Загружено'):
    """Отображает анимацию загрузки в терминале."""
    spinner = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    i = 0
    while not stop_event.is_set():
        sys.stdout.write(f"\r{message}... {spinner[i % len(spinner)]} {i/10} сек")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1

    sys.stdout.write("\r" + " " * (len(message) + 10) + "\r")
    sys.stdout.flush()
    print(result + f'за {i/10} секунд')

def loading(event, prompt):
    stop_loading = threading.Event()
    loader_thread = threading.Thread(target=loading_animation, args=(stop_loading, "Генерация"))
    loader_thread.start()
    result = event(prompt)
    stop_loading.set()
    loader_thread.join()
    
    return result