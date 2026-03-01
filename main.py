from pyrogram import Client

api_id = int(33204832)
api_hash = 3c1c907d23f2c5684f21d936d95bcde9
bot_token = 8725093104:AAHptGG1sQjFlUnczLCLF4nVpGtifkN3ao4

app = Client("musicbot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message()
async def start(client, message):
    await message.reply("🔥 Aura Music Bot Online 🔥")

app.run()
