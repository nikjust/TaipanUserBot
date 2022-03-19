from pyrogram import Client

class CustomClient(Client):
    commandsHelp = []

    def addCommandDescription(self, name, description, usage):
        self.commandsHelp.append({"name":name, "description":description, "usage":usage})
        return self

    def getCommands(self):
        return self.commandsHelp