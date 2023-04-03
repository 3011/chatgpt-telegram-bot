# chatgpt-telegram-bot
在 Telegram 上使用 ChatGPT。

# 使用方法
1. 设置`main.py`中的`bot_token`与`allowed_users`
2. 安装依赖`pip install --upgrade python-telegram-bot revChatGPT`
3. 运行`python main.py`
4. `https://chat.openai.com/api/auth/session`获取 Access token，向 bot 发生`/set_access_token <accessToken>`