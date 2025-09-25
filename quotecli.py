#!/usr/bin/env python3
import requests
import time
import sys

def get_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random")
        if response.status_code == 200:
            data = response.json()
            # FIX: Access the first item in the list `data[0]`
            # and use the correct keys 'q' and 'a'.
            quote = data[0]['q']
            author = data[0]['a']
            return f'"{quote}"\n— {author}'
        else:
            return "Failed to fetch quote. Try again later."
    except Exception as e:
        return f"Error: {e}"

def animate_quote_display(text):
    # Animate quote like typing effect
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print("\n")

def main():
    quote_text = get_quote()
    animate_quote_display(quote_text)

if __name__ == "__main__":
    main()