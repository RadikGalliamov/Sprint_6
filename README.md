Sprint_6 Page Object
Запуски тестов:
pytest -v  Запуск всех тестов
pytest -v test/test_main_page.py Запуск всех тестов файла test_main_page.py
pytest -k test_click_scooter_yandex_logo_will_be_new_windows_with_main_page_yandex test/test_order_page.py Запуск определенного 
теста в файле test_order_page.py

pytest test --alluredir=allure_results  генерировать Allure-отчёт
allure serve allure_results сформировать отчёт в формате веб-страницы

data.py - URL тестируемых страниц
conftest.py - настройки методов до и после теста
requirements.txt - список установленных библиотек
allure_results - файлы для отчетов Allure
allure-report - отчет Allure
