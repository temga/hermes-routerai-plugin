# Плагин RouterAI для Hermes Agent

[RouterAI](https://routerai.ru/) — российский OpenAI-совместимый API-агрегатор, предоставляющий доступ к GPT, Claude, Gemini, Grok, DeepSeek и сотням других моделей через единый API. Оплата в рублях, без VPN.

## Установка

Скопируйте директорию `routerai/` в папку плагинов Hermes:

    cp -r routerai ~/.hermes/plugins/model-providers/

## Настройка

Установите API-ключ RouterAI как переменную окружения:

    export ROUTERAI_API_KEY="ваш-api-ключ"

Или добавьте в профиль оболочки (~/.bashrc / ~/.zshrc) для сохранения между сессиями.

## Использование

Запустите Hermes и выберите RouterAI в качестве провайдера:

    hermes model

Выберите `routerai` из списка, затем выберите модель. Переключать модели в любой момент:

    /model routerai:claude-sonnet-5

## Доступные модели

RouterAI предоставляет доступ к 300+ моделям. Популярные:

- Claude Sonnet 5 — 204 / 1023 ₽ за 1М токенов
- GPT-5.6 Sol — 511 / 3069 ₽ за 1М токенов
- Gemini 3.1 Pro Preview — 204 / 1227 ₽ за 1М токенов
- DeepSeek V4 Pro — 62 / 124 ₽ за 1М токенов

Полный список: routerai.ru/models

## Как это работает

Плагин регистрирует `ProviderProfile` в реестре провайдеров Hermes Agent. Поскольку API RouterAI полностью совместим с форматом OpenAI Chat Completions, дополнительные хуки или переопределения не требуются — базовый профиль обрабатывает всё автоматически.

## Лицензия

MIT
