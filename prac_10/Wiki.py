import wikipedia

search_phrase = input("Enter a page title or search phrase: ")
while search_phrase != "":
    try:
        page = wikipedia.page(search_phrase)
        print(page.title)
        print(page.content)
        print(page.url)
        search_phrase = input("Enter a page title or search phrase: ")
    except wikipedia.exceptions.DisambiguationError as error:
        print(error.options)