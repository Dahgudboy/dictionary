# README: English Dictionary in Python

## Introduction  
This Python script functions as a simple English dictionary. Given a word as input, it returns its meaning using an API or a pre-defined dictionary dataset.

## Features  
- Fetches word definitions  
- Supports multiple meanings  
- Handles errors for unknown words  
- Provides synonyms and examples (if available)  

## Requirements  
- Python 3.x  
- `requests` module (for API-based dictionary)  

## Installation  
1. Install Python (if not installed).  
2. Install the required module:  
   ```bash
   pip install requests
   ```

## Usage  

### Option 1: Using an API (e.g., Free Dictionary API)  
```python
import requests

def get_meaning(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        meanings = data[0]["meanings"]
        for meaning in meanings:
            print(f"Part of Speech: {meaning['partOfSpeech']}")
            for definition in meaning["definitions"]:
                print(f"- {definition['definition']}")
    else:
        print("Word not found.")

word = input("Enter a word: ")
get_meaning(word)
```

## Error Handling  
- If the word is not found, the script returns a friendly message.  
- API errors are handled using status codes.  

## License  
This project is open-source and free to use.  
