import requests
from bs4 import BeautifulSoup
from itertools import zip_longest
import streamlit as st

#read in searchterms
searchterm = 'iphone+11'
bad_terms = ('face id', 'water damaged', 'ic locked', 'icloud')
url = (f'https://www.ebay.co.uk/sch/i.html?_dcat=9355&_fsrp=1&_from=R40&_nkw={searchterm}&_sacat=0&LH_ItemCondition=7000&_sop=15')

st.title("IBot the eBay scraper")
st.write('This is a Streamlit application made to visualize the data of average prices and listings scraped from eBay')

def scrape_site(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    names = [name.text.lower() for name in soup.find_all("span", {"role": "heading"})]
    prices = [price.text for price in soup.find_all("span", {"class": "s-item__price"})]
    links = [link['href'] for link in soup.find_all("a", {"class": "s-item__link"})]

    # Calculate the maximum length of the three lists
    clean_names = []
    for name in names:
        if any(term in name for term in bad_terms):
            continue
        clean_names.append(name)

    # Calculate the maximum length of the three lists
    max_len = max(len(clean_names), len(prices), len(links))

    # Pad the lists with "N/A" values so they all have the same length
    clean_names = list(zip_longest(clean_names, fillvalue="N/A"))
    prices = list(zip_longest(prices, fillvalue="N/A"))
    links = list(zip_longest(links, fillvalue="N/A"))

    return clean_names, prices, links

names, prices, links = scrape_site(url)

def stream(names, prices, links):
    for n, p, l in zip(names, prices, links):
        st.markdown(f"- **{n}**: {p} ({l})")

    st.write(names)
    st.write(prices)
    st.write(links)

stream(names, prices, links)


#def write():