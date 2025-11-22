import sys
import time
import threading

def loading_animation(stop_event, message="Загрузка"):
    """Отображает анимацию загрузки в терминале."""
    spinner = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    i = 0
    while not stop_event.is_set():
        sys.stdout.write(f"\r{message}... {spinner[i % len(spinner)]}")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    # Очищаем строку после завершения
    sys.stdout.write("\r" + " " * (len(message) + 10) + "\r")
    sys.stdout.flush()

# Пример использования
if __name__ == "__main__":
    stop_loading = threading.Event()
    loader_thread = threading.Thread(target=loading_animation, args=(stop_loading, "Обработка"))
    loader_thread.start()

    # Имитация работы (замените на вашу реальную задачу)
    time.sleep(3)

    # Остановка анимации
    stop_loading.set()
    loader_thread.join()

    print("✅ Готово!")