from pyrogram import Client
from commands import animeReaction, placeholders, googleFind, help
import config
from customClient import CustomClient

# @client.on_message(pyrogram.filters.me & pyrogram.filters.command("type", prefixes=";"))
# def type_command(_, message: pyrogram.types.Message):
#    text = message.text.split(";type", maxsplit=1)[1]
#    typed = list(text)[0]
#    for symbol in list(text):
#        print(symbol)
#        typed += symbol
#        if symbol != "" and symbol != " ":
#            message.edit_text(typed)
#            time.sleep(0.05)



client = CustomClient(session_name=config.session_name, api_id=config.api_id, api_hash=config.api_hash)
# init zone
animeReaction.AnimeReaction(client)
placeholders.PlaceHolders(client)
googleFind.GoogleFind(client)
help.Help(client)
# init zone end

client.run()
