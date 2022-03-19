import pyrogram
from customClient import CustomClient

class Help:
    def __init__(self, client: CustomClient):
        print("help module init!")

        client.addCommandDescription("help", "this command", ";help")

        @client.on_message(pyrogram.filters.me & pyrogram.filters.command("help", prefixes=";"))
        def command(_, message: pyrogram.types.Message):
            commands = client.getCommands()

            string = ""
            for command in commands:
                string += f'**{command["name"]}**\n' \
                          f'{command["description"]}\n' \
                          f'```{command["usage"]}```\n\n'

            print(string)
            message.edit_text(string)