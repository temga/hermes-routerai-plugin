# Плагин RouterAI для Hermes Agent

[![GitHub](https://img.shields.io/badge/GitHub-temga%2Fhermes--routerai--plugin-blue)](https://github.com/temga/hermes-routerai-plugin)

[RouterAI](https://routerai.ru/) — российский OpenAI-совместимый API-агрегатор, предоставляющий доступ к GPT, Claude, Gemini, Grok, DeepSeek и сотням других моделей через единый API. Оплата в рублях, без VPN.

## Установка

### Standalone

`hermes plugins install` клонирует репозиторий плоско в `~/.hermes/plugins/routerai-provider/`, но Provider Registry сканирует только `~/.hermes/plugins/model-providers/<name>/`. Без симлинка провайдер не появится в `hermes model`:

    hermes plugins install temga/hermes-routerai-plugin --enable
    ln -s ~/.hermes/plugins/routerai-provider ~/.hermes/plugins/model-providers/routerai

### Через hermes-ru-ecosystem

Если у вас несколько плагинов российской экосистемы, `install.sh` создаст симлинк автоматически:

    curl -fsSL https://raw.githubusercontent.com/temga/hermes-ru-ecosystem/main/install.sh | bash

## Настройка

Hermes хранит секреты в `~/.hermes/.env`. Добавьте туда:

    ROUTERAI_API_KEY=ваш-api-ключ

Или запустите `hermes setup` — мастер настройки запросит ключ автоматически.

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

## Известные особенности

### Предупреждение о дорогой модели (EXPENSIVE MODEL WARNING)

RouterAI отдаёт цены в рублях через свой `/models` API. Hermes предполагает, что все цены указаны в долларах США, поэтому рублёвые цены интерпретируются как долларовые. Из-за этого при выборе некоторых моделей может появляться предупреждение:

```
!!! EXPENSIVE MODEL WARNING !!!
z-ai/glm-5.2 has known pricing above Hermes safety threshold.
Input tokens: $74.19/M
Output tokens: $233.17/M
```

Реальная цена: ~74 ₽/M вход (~$0.85) и ~233 ₽/M выход (~$2.70) — пороги не превышаются.

**Решение:** просто подтвердите выбор («Switch anyway»). Предупреждение появляется один раз при смене модели и не влияет на работу. Отключить проверку без модификации исходного кода Hermes нельзя — в `model_cost_guard.py` пороги захардкожены ($20/M вход, $100/M выход).

## Как это работает

Плагин регистрирует `ProviderProfile` в реестре провайдеров Hermes Agent. Поскольку API RouterAI полностью совместим с форматом OpenAI Chat Completions, дополнительные хуки или переопределения не требуются — базовый профиль обрабатывает всё автоматически.

## Репозиторий

- **GitHub:** https://github.com/temga/hermes-routerai-plugin

## Лицензия

MIT
