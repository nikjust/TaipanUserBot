import pyrogram
from customClient import CustomClient


class Help:
    def __init__(self, client: CustomClient):
        print("help module init!")

        client.add_command_description("help", "this command", ";help")

        @client.on_message(pyrogram.filters.me & pyrogram.filters.command("help", prefixes=";"))
        def command(_, message: pyrogram.types.Message):
            commands = client.get_commands()

            string = ""
            for command_object in commands:
                string += f'**{command_object["name"]}**\n' \
                          f'{command_object["description"]}\n' \
                          f'```{command_object["usage"]}```\n\n'

            print(string)
            message.edit_text(string)
