import re
import urllib.parse
import pyrogram
import googlesearch
from customClient import CustomClient

class GoogleFind:
    def __init__(self, client: CustomClient):

        client.addCommandDescription("google", "Google any query", ";google [query] lang={lang}")
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


            searchURI = urllib.parse.quote(search)

            searched = googlesearch.search(searchURI, num_results=5, lang=lang)

            str = f"results for {search}:"
            for id, result in enumerate(searched):
                str += f"\n{id+1}: {result}\n"

                #print(result)
            message.edit_text(str)

