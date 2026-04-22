from __future__ import annotations

from app.core.plugin import CommandPlugin, PluginMeta

plugin = CommandPlugin(
    name="market_hello",
    command="/你好",
    description="market demo hello",
    meta=PluginMeta(name="market_hello", version="1.0.0", author="qqbot-plugin-market", description="示例市场插件：/你好"),
)


@plugin.handle
async def on_hello(ctx):
    await ctx.reply("你好！这是从插件商店安装的示例插件。")
