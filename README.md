# Python + Appium для тестирования мобильных приложений

## Описание проекта
Автоматизация для Smoke Android BZ

## Структура репозитория

***element_locators*** - директория локаторами.
***page*** - директория с классами приложений
***tests*** - директория с тестами

## Использование
1. **Установка зависимостей**: Перед запуском кода убедитесь, что у вас установлены все необходимые зависимости. Рекомендуется использовать виртуальное окружение Python.
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

2. **Настройка Appium**: Установите Appium используя документацию из ресурсов.
3. **Установка Android Studio**: Установите Android Studio используя документацию из ресурсов.

4. **Запуск примеров**:
   - Запустите эмулятор или подключите реальное устройства к пк.
   - В терминале запустите Appium командой 'appium'
   - Запустите Android Studio
   - Введите в терминал команду 'pytest -u'

## Ресурсы
- [Документация Appium](https://appium.io/docs/en/latest/quickstart/install/)
- [Документация Python](https://docs.python.org/3/)
- [Официальный сайт Python](https://www.python.org/)
- [Официальный сайт Appium](http://appium.io/)
- [Официальный cайт Android Studio](https://developer.android.com/studio)


