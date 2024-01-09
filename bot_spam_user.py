from telethon.sync import TelegramClient, events
from telethon.tl import functions

api_id = 'api_id'
api_hash = 'api_hash'
bot_token = 'bot_token'

# تكوين العميل
client = TelegramClient('bot_session', api_id, api_hash)

async def main():
    await client.start(bot_token=bot_token)
    
    @client.on(events.NewMessage(pattern='/start'))
    async def start(event):
        await event.respond('مرحبًا بك في البوت! يرجى الضغط هنا /username:')
    
    @client.on(events.NewMessage(pattern='/username'))
    async def get_username(event):
        async with client.conversation(event.chat_id) as conv:
            await conv.send_message('يرجى إدخال اسم المستخدم الهدف:')
            response = await conv.get_response()
            username = response.text
            
            await conv.send_message('أدخل محتوى الرسالة:')
            response = await conv.get_response()
            message_content = response.text
            
            await conv.send_message('أدخل عدد الرسائل:')
            response = await conv.get_response()
            num_messages = int(response.text)
            
            for _ in range(num_messages):
                await client.send_message(username, message_content)
            
            await conv.send_message(f'تم إرسال {num_messages} رسالة إلى {username} بنجاح!')
    
    @client.on(events.NewMessage(pattern='/help'))
    async def help(event):
        await event.respond('يمكنك استخدام الأوامر التالية:\n'
                            '/start - لبدء الدردشة مع البوت\n'
                            '/username - لإرسال رسائل إلى مستخدم آخر\n'
                            '/help - لعرض هذه الرسالة')
    
    await client.run_until_disconnected()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
