Shop
====

Установка под ubuntu.

1. virtualenv env -p /usb/bin/python3

2. Чтобы установить Pillow, надо
http://stackoverflow.com/questions/34631806/fail-during-installation-of-pillow-python-module-in-linux

3. . env/bin/activate

4. pip install -r requirements.txt

5. Скопировать и переименовать файл myshop/settings.py.dist в myshop/settings.py

6. Поменять реквизиты базы


Установка новых пакетов

1. pip install Package

2. pip freeze > requirements.txt
