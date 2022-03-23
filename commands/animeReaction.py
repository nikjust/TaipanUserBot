import pyrogram
import requests

from customClient import CustomClient


class AnimeReaction:
    def __init__(self, client: CustomClient):
        print("animeReaction module init!")
        client.add_command_description("reaction", "Send anime reaction gif", ";reaction {reaction}")

        @client.on_message(pyrogram.filters.me & pyrogram.filters.command("reaction", prefixes=";"))
        def command(_, message: pyrogram.types.Message):
            reaction_list = ['waifu', 'neko', 'shinobu', 'megumin', 'bully', 'cuddle', 'cry', 'hug', 'awoo', 'kiss',
                             'lick', 'pat', 'smug', 'bonk', 'yeet', 'blush', 'smile', 'wave', 'highfive', 'handhold',
                             'nom', 'bite', 'glomp', 'slap', 'kill', 'kick', 'happy', 'wink', 'poke', 'dance', 'cringe']

            print(message)
            try:
                arg = message.command[1]
            except IndexError:
                return message.reply(f"No argument; list: {reaction_list}")

            if not (arg in reaction_list):
                return message.reply(f"Bad argument; list: {reaction_list}")

            res = requests.get(f"https://api.waifu.pics/sfw/{arg}")
            url = res.json()["url"]
            print(url)

            client.send_animation(message.chat.id, url)
            message.delete()
