# chatgpt-telegram-bot
Use ChatGPT on Telegram.

## Instructions
1. Set `bot_token` and `allowed_users` in `main.py`.
2. Installation depends on `pip install --upgrade python-telegram-bot revChatGPT`
3. Run `python main.py`
4. `https://chat.openai.com/api/auth/session` gets the Access token, and sends `/set_access_token <accessToken>` to the bot
5. Use ChatGPT on Telegram

## Bot commands
- `/start` - Reset chat
- `/set_access_token <accessToken>` - Set access token

# chatgpt-telegram-bot
在 Telegram 上使用 ChatGPT。

## 使用方法
1. 设置`main.py`中的`bot_token`与`allowed_users`。
2. 安装依赖`pip install --upgrade python-telegram-bot revChatGPT`
3. 运行`python main.py`
4. `https://chat.openai.com/api/auth/session`获取 Access token，向 bot 发送`/set_access_token <accessToken>`
5. 在 Telegram 上使用 ChatGPT

## 机器人命令
- `/start` - 重置聊天
- `/set_access_token <accessToken>` - 设置 Access token