from __future__ import annotations

from datetime import datetime, timezone

from app.core.plugin import CommandPlugin, PluginMeta

plugin = CommandPlugin(
    name="market-time",
    command="/时间",
    description="market demo time",
    meta=PluginMeta(name="market-time", version="1.0.0", author="qqbot-plugin-market", description="示例市场插件：/时间"),
)


@plugin.handle
async def on_time(ctx):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    await ctx.reply(f"当前时间：{now}")
