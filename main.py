from telethon.sync import TelegramClient,events

api_id = #тут число
api_hash = ""
client = TelegramClient('AndrewHelicopterParcer', api_id, api_hash).start()
channel = ["@writeBotMassage"]#можно установить несколько
sendTo = ""


def main():
    file = open('./words.txt', "r", encoding="utf-8")
    words = [str(line.replace("\r", "").replace("\n", "")) for line in file]
    file.close()
    print("--word list start--")
    for word in words:
        print(word)
    print("--word list end--")
    @client.on(events.NewMessage(chats=channel))
    async def normal_handler(event):
        flag = True
        for word in words:
            if word in str(event.message):
                flag = False
                await client.forward_messages(sendTo, event.message)
                print("new notification")
        if(flag == True):
                print("no coincidences")
    client.start()
    print("|Bot run|")
    client.run_until_disconnected()
    print("Bot closed")
if __name__ == '__main__':
    main()