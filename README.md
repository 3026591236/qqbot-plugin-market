# qqbot-plugin-market

这是 `qqbot-framework` 的一个简单插件商店仓库（market index + 可下载的插件脚本）。

## market.json

- `plugins[].name`：插件名（用于在机器人里安装）
- `plugins[].url`：插件脚本的 raw URL
- `plugins[].sha256`：可选，校验完整性

## 插件脚本

放在 `plugins/` 下。

示例：
- `plugins/market_hello.py` → `/你好`
- `plugins/market_time.py` → `/时间`
