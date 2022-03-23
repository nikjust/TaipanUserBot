import re
import urllib.parse

import googlesearch
import pyrogram

from customClient import CustomClient


class GoogleFind:
    def __init__(self, client: CustomClient):

        client.add_command_description("google", "Google any query", ";google [query] lang={lang}")
        print("googleFind module init!")

        @client.on_message(pyrogram.filters.me & pyrogram.filters.command("google", prefixes=";"))
        def command(_, message: pyrogram.types.Message):
            message.edit_text("started search")

            lang = "en"
            args = message.command

            regex = re.compile(r"lang=(.+)")
            if re.match(regex, args[-1]):
                lang = re.search(regex, args.pop(-1)).groups()[0]
            args.pop(0)
            search = " ".join(args)

            search_uri = urllib.parse.quote(search)

            searched = googlesearch.search(search_uri, num_results=5, lang=lang)

            text = f"results for {search}:"
            for result_id, result in enumerate(searched):
                text += f"\n{result_id + 1}: {result}\n"

                # print(result)
            message.edit_text(text)
