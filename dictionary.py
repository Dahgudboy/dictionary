import requests

def search_word(find):
    base_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{find}"
    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()
        
        if data:  
            word_info = data[0]
            print(f"Word: {word_info['word']}")

         
            for meaning in word_info["meanings"]:
                part_of_speech = meaning["partOfSpeech"]
                print(f"Part of Speech: {part_of_speech}")

                for definition in meaning["definitions"]:
                    print(f"- {definition['definition']}")
        else:
            print("No definition found.")
    else:
        print("Word not found. Please try another word.")

find = input("Enter your word: ").strip().lower()
search_word(find)
