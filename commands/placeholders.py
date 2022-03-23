import datetime
import random
import re

import pyrogram

from customClient import CustomClient


class PlaceHolders:
    def __init__(self, client: CustomClient):
        print("placeHolders module init!")

        client.add_command_description("now", "insert now time and date", "{{now}}")
        client.add_command_description("now:time", "inserts now time", "{{now:time}}")
        client.add_command_description("now:date", "inserts now date", "{{now:date}}")
        client.add_command_description("random", "inserts random number", "{{random:[from]:[to]}}")

        @client.on_message(pyrogram.filters.me & pyrogram.filters.regex("{{now}}"))
        def now_placeholder(_, message: pyrogram.types.Message):
            message.edit_text(message.text.replace("{{now}}", str(datetime.datetime.now())))

        @client.on_message(pyrogram.filters.me & pyrogram.filters.regex("{{now:time}}"))
        def now_time_placeholder(_, message: pyrogram.types.Message):
            message.edit_text(
                message.text.replace("{{now:time}}", str(datetime.datetime.time(datetime.datetime.now()))))

        @client.on_message(pyrogram.filters.me & pyrogram.filters.regex("{{now:date}}"))
        def now_date_placeholder(_, message: pyrogram.types.Message):
            message.edit_text(
                message.text.replace("{{now:date}}", str(datetime.datetime.date(datetime.datetime.now()))))

        @client.on_message(pyrogram.filters.me & pyrogram.filters.regex("{{random:[0-9]+:[0-9]+}}"))
        def random_placeholder(_, message: pyrogram.types.Message):
            regex = re.search(r"({{random:([0-9]+):([0-9]+)}})", message.text, re.IGNORECASE)

            # for i in range(len(regex.groups())):
            #   print(f"{i}: {regex.groups()[i]}")

            command = regex.groups()[0]
            from_random = int(regex.groups()[1])
            to_random = int(regex.groups()[2])
            need_random = True
            number = to_random

            if from_random > to_random:
                from_random, to_random = to_random, from_random
            elif from_random == to_random:
                need_random = False

            if need_random:
                number = random.randint(from_random, to_random)

            message.edit_text(message.text.replace(command, str(number)))

        # @client.on_message(pyrogram.filters.me & pyrogram.filters.regex("({{rainbow:(.+)}})"))
        # def rainbow_placeholder(_, message: pyrogram.types.Message):
        #    regex = re.search("({{rainbow:(.+)}})", message.text, re.IGNORECASE)
        #    all = regex.groups()[0]
        #    string = regex.groups()[1]
        #
        #
        #    text = message.text.replace(all, f"{colorama.Fore.RED}{string}")
        #    message.edit_text(text)
