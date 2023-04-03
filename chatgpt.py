from revChatGPT.V1 import Chatbot


bot = Chatbot(config={"access_token": ""})


def set_access_token(access_token):
    bot.set_access_token(access_token)


def reset_chat():
    bot.reset_chat()


# def get_reply(prompt):
#     response = ""
#     for data in bot.ask(prompt):
#         response = data["message"]
#     return response


def get_reply_stream(prompt):
    prev_text = ""
    for data in bot.ask(prompt):
        prev_text = data["message"]
        yield False, prev_text
    yield True, prev_text
