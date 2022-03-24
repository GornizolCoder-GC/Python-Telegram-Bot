import telegram

bot = telegram.Bot(token="1948264467:AAGuGshN7CSkW8VyfR6s7W_ENfaTWEv48Nw")

print(bot.get_me())

updates = bot.get_updates()

bot.send_message(chat_id = 1890885019, text="salom")
i=0
print(type(updates))
print(len(updates))
for update in updates:
    i+=1
    print(i)
    print(update)