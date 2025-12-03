<img width="1920" height="1080" alt="изображение" src="https://github.com/user-attachments/assets/064011c0-bdea-4c62-8989-f6a88e46b829" />

<img width="1920" height="1080" alt="изображение" src="https://github.com/user-attachments/assets/9a507cb2-4c2d-4450-90cf-d50bcd1adf62" />

Информация для ученика 
1. Для запуска сервера ввести в терминал команду `python ./main.py` находясь в корне проекта
2. В случае возникновения ошибок обратиться к тьютору

Информация для тьютора
1. Для установки всех зависимостей ввести в терминал команду `pip install -r ./requirements.txt`.
   Для установки основных зависисмостей ввести в терминал команду `pip install -r ./minimal-requirements.txt`.
2. Если возникает ошибка "HINT: This error might have occurred since this system does not ha ve Windows Long Path support enabled. You can find information on how to enable this at https://pip-pypa.io/warnings/enable-long-paths", то нужно открыть powershell ОТ ИМЕНИ АДМИНИСТРАТОРА (win+r для быстрого ввода, ввести в строку `powershell` и открыть через ctrl+shift+enter) и ввести команду `Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1`
3. В случае возникновения ошибки OSError: [WinError1114] скачать C++ с сайта майкрософт https://learn.microsoft.com/ru-ru/cpp/windows/latest-supported-vc-redist?view=msvc-170#latest-supported-redistributable-version или сразу по ссылке https://aka.ms/vc14/vc_redist.x64.exe
   Установка производится ОТ ИМЕНИ АДМИНИСТРАТОРА
4. Проверить работоспособность с помощью команды `python ./main.py`
5. В случае возникновения писать в тг @azazlov с конкретными сообщениями ошибки

Примечание
Давать права на доступ в локальную сеть для пайтон НЕОБЯЗАТЕЛЬНО. Это нужно лишь для подключения по локальной сети с других компьютеров к хостингу