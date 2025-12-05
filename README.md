# Руководство по установке и решению проблем

![Скриншот 1](https://github.com/user-attachments/assets/064011c0-bdea-4c62-8989-f6a88e46b829)
![Скриншот 2](https://github.com/user-attachments/assets/9a507cb2-4c2d-4450-90cf-d50bcd1adf62)

## Для ученика

Чтобы запустить сервер:
1. Откройте терминал.
2. Перейдите в корневую директорию проекта.
3. Выполните команду:
   ```bash
   python ./main.py
   ```

Если возникли ошибки — обратитесь к тьютору.

## Для тьютора

### Установка зависимостей

1. Для установки всех зависимостей выполните:
   ```bash
   pip install -r ./requirements.txt
   ```
2. Для установки основных зависимостей выполните:
   ```bash
   pip install -r ./minimal-requirements.txt
   ```

### Решение распространённых ошибок

#### Ошибка: «HINT: This error might have occurred since this system does not have Windows Long Path support enabled...»

1. Откройте PowerShell **от имени администратора**:
   - Нажмите `Win + R`.
   - Введите `powershell`.
   - Запустите с помощью `Ctrl + Shift + Enter`.
2. Выполните команду:
   ```powershell
   Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1
   ```

#### Ошибка: `OSError: [WinError 1114]`

1. Скачайте Microsoft Visual C++ Redistributable:
   - Перейдите на [официальный сайт](https://learn.microsoft.com/ru-ru/cpp/windows/latest-supported-vc-redist?view=msvc-170#latest-supported-redistributable-version).
   - Или используйте прямую ссылку: [vc_redist.x64.exe](https://aka.ms/vc14/vc_redist.x64.exe).
2. Установите пакет **от имени администратора**.

### Проверка работоспособности

После установки зависимостей и решения возможных ошибок проверьте работоспособность сервера:
```bash
python ./main.py
```

### Обратная связь

Если проблема не решена, напишите в Telegram: [@azazlov](https://t.me/azazlov). Обязательно укажите:
- точное сообщение об ошибке;
- шаги, которые вы выполняли.

## Примечание

Предоставление прав на доступ в локальную сеть для Python **не обязательно**. Это требуется только в случае подключения к хостингу с других компьютеров по локальной сети или, например, с телефона.