# RouterAI Plugin for Hermes Agent

[RouterAI](https://routerai.ru/) — russian OpenAI-compatible API aggregator providing access to GPT, Claude, Gemini, Grok, DeepSeek and hundreds of other models via a single API. Pay in rubles, no VPN required.

## Installation

Copy the routerai/ directory to your Hermes plugins folder:

    cp -r routerai ~/.hermes/plugins/model-providers/

## Configuration

Set your RouterAI API key as an environment variable:

    export ROUTERAI_API_KEY="your-api-key"

Or add it to your shell profile (~/.bashrc / ~/.zshrc) for persistence.

## Usage

Start Hermes and select RouterAI as your provider:

    hermes model

Choose routerai from the list, then pick a model. You can also switch models at any time with:

    /model routerai:claude-sonnet-5

## Available Models

RouterAI provides access to 300+ models. Some popular ones:

- Claude Sonnet 5 — 204 / 1023 RUB per 1M tokens
- GPT-5.6 Sol — 511 / 3069 RUB per 1M tokens
- Gemini 3.1 Pro Preview — 204 / 1227 RUB per 1M tokens
- DeepSeek V4 Pro — 62 / 124 RUB per 1M tokens

Full list: routerai.ru/models

## How It Works

The plugin registers a ProviderProfile in Hermes Agent provider registry. Since RouterAI is fully OpenAI Chat Completions compatible, no custom hooks or overrides are needed — the base profile handles everything.

## License

MIT
