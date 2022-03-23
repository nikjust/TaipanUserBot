from pyrogram import Client


class CustomClient(Client):
    commandsHelp = []

    def add_command_description(self, name, description, usage):
        self.commandsHelp.append({"name": name, "description": description, "usage": usage})
        return self

    def get_commands(self):
        return self.commandsHelp
