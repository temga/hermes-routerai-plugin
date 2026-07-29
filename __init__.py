"""RouterAI provider profile.

RouterAI -- russian OpenAI-compatible API aggregator.
Base endpoint: https://routerai.ru/api/v1
Docs: https://routerai.ru/docs

API is fully OpenAI Chat Completions compatible, so a basic
ProviderProfile without hook overrides is sufficient.
"""

from __future__ import annotations

from providers import register_provider
from providers.base import ProviderProfile

routerai = ProviderProfile(
    name="routerai",
    aliases=("router",),
    env_vars=("ROUTERAI_API_KEY",),
    display_name="RouterAI",
    description="RouterAI -- GPT, Claude, Gemini and more via one API (RUB, no VPN)",
    signup_url="https://routerai.ru/",
    base_url="https://routerai.ru/api/v1",
    fallback_models=(
        "gpt-5.6-sol",
        "claude-sonnet-5",
        "gemini-3.1-pro-preview",
        "deepseek-v4-pro",
        "deepseek-v4-flash",
    ),
    default_aux_model="deepseek-v4-flash",
    supports_vision=True,
)

register_provider(routerai)
