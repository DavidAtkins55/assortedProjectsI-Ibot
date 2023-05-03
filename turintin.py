import os
import requests
import json
from bs4 import BeautifulSoup

file_path = '/Users/nathancassells/Documents/test.txt.rtf'

with open(file_path, 'r') as file:
    text = file.read()

search_results = ['']

total_words = len(text.split())
search_words = 0

for result in search_results:
    response = requests.get(result)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    search_words += len(soup.get_text().split())

percentage = search_words / total_words * 100

print(f"Percentage of text taken from search results: {percentage}%")
