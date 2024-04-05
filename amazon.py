import streamlit as st
import requests
from bs4 import BeautifulSoup
import bs4
# Dictionary mapping product names to their Amazon URLs
product_urls = {
    "samsung galaxy s24": "https://www.amazon.in/Samsung-Galaxy-Smartphone-Yellow-Storage/dp/B0CQYGPGPP?th=1",
    "iphone 15 pro": "https://www.amazon.in/Apple-iPhone-15-Pro-128/dp/B0CHX2DRGV",
    "motorola razr 40":'https://www.amazon.in/Motorola-Storage-External-Display-Android/dp/B0C7QGVVW4?th=1',
    "oneplus 12 5g":'https://www.amazon.in/OnePlus-Silky-Black-256GB-Storage/dp/B0CQPM5WMB/ref=sr_1_1?dib=eyJ2IjoiMSJ9.quLsCOG8oHjpvtRcmTr8-mAs7wMk8NTjk0ro5_Diu8Y6KD0JZaf6yIg50nIs_Nbhs7zU7w0hRIkGl9OfGvgUJe5mi25S_nxxzLxyoHcnBbDH36AeMHCNSmjJK8o2c8FFpZL74CWzX9_vOEj5Q8_XFRuHwNK7Wny-IxsccmP9ns9vnWLG-uyY2Rfg0vwfXejWcBXJKgADebRGlZNU_kft8p_4IRfkTV0NfB1pey9DMAU._awIjMBWurP63twB3rn1cFxJ3bWUc73yd18_gG5jolE&dib_tag=se&keywords=oneplus%2B12&qid=1712297385&sr=8-1&th=1',
    "xiaomi 12 pro":'https://www.amazon.in/Renewed-Xiaomi-12-Snapdragon-Flagship/dp/B0B6RPMW8Y/ref=sr_1_2?crid=2DVEPPHZVOX89&dib=eyJ2IjoiMSJ9.yjBwe2_bXqV3cU3jdh3kTqKo8FDglYKWbXQjx6PYFIID35sqsFht3vHXJZoC0EZhcgo5zVUdeRqgSOKOc8v9PXUhZos2V89Xxa634kiNk0XnZM99N_7koEx3ionWt1In6iCMT0tSCbiHPFVC-ZmDL1s-8bIKKPsBIAeCGb4uYR3gK684lWe-qq4EZlT0gDofl0_A7ZLK7rtKYE7w0n3XKQtCTGl9ehU3le2KPk3tEy4.fOZnnyAR2K5T18CwsFcxsGRvPi6kK9N-uofK1CdaQSs&dib_tag=se&keywords=xiaomi+12+pro&qid=1712210217&sprefix=xiaomi+1%2Caps%2C2007&sr=8-2',
    "google pixle 8 pro":'https://www.amazon.in/Pixel-128GB-Storage-Obsidian-Black/dp/B0CYKSDWX9/ref=sr_1_2?dib=eyJ2IjoiMSJ9.vd5qnzk-LUSLThrzQW5Oy3K-ny4e-5Eb8vyy4t_yGj6-g8EIzi2HwF7LesqjQjegeCbbkF6uOm6N2v0JxjdhdT3XU4PW4kUsl6dDsXXwGVJ0JhbFDMkdCLI3dtFGvSYFCXvjRs0UOzOKUtluQqz9PohFmUtxdtxm_uolwlvuU9s0M6pNeSAneaUk-hsdgccDKIUMn8SdJOy4P9mucidH_JRWptluACygqKQmShKlIWg.Jue-eL-oH3kM4PNuqcjNy-OB9x37Hlw96l-PEKy7cbE&dib_tag=se&keywords=google+pixel+8+pro&qid=1712297123&sr=8-2',
    "nord 2t 5g":'https://www.amazon.in/OnePlus-Nord-Shadow-Storage-256GB/dp/B0B3CZ7P4V/ref=sr_1_1?crid=2TFFMPEJUNZWN&dib=eyJ2IjoiMSJ9.LMB6RdPypKuEQrY8Bl3FrsP0NNdULByQ6s3rLii-efrWVMNjTorQKQ7NTY0GVODld-SzHElAFLaHkyozx_Pkf1Qr4nKUQ-sCvz6Sxfnlsb2Yin-kZEE6eCDvmD36bso_6Opk46RDaD88DbxR2qCfVaquD639KlDnb8xT47CUKFvK7ruHf1aiMMgxrTrakW8uSDKHMXovL6dVO2jf18epuNLyGhzG5JOFKmWMLJUGfro.bmuCl4CA9392klzWn0EFluv9PA2KfD-2-3eB_qfOeQc&dib_tag=se&keywords=nord+2t+5g&qid=1712210415&sprefix=nord+2t+5g%2Caps%2C492&sr=8-1',
    "redmi note 5 pro":'https://www.amazon.in/Redmi-Note-Pro-Black-Storage/dp/B07FK4DNRS'
    # Add more products as needed
    # Add more products as needed
}
flipkart_product_urls = {
    "iphone 15 pro": 'https://www.flipkart.com/apple-iphone-15-pro-black-titanium-128-gb/p/itm96f61fdd7e604',
    "samsung galaxy s24": 'https://www.flipkart.com/samsung-galaxy-s24-ultra-5g-titanium-gray-256-gb/p/itm12ef5ea0212ed?pid=MOBGX2F3RQKKKTAW&lid=LSTMOBGX2F3RQKKKTAWKAVWET&marketplace=FLIPKART&q=Samsung+Galaxy+S24+Ultra+5G&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&iid=e03eb47f-b3f6-451f-af9b-29e99cc67e64.MOBGX2F3RQKKKTAW.SEARCH&ssid=f0ahdyweg00000001711936639445&qH=4e51b526262813e3',
    "motorola razr 40": 'https://www.flipkart.com/motorola-razr-40-vanilla-cream-256-gb/p/itm2e006f5ffc5da?pid=MOBGRZGG4TEDXYM2&lid=LSTMOBGRZGG4TEDXYM2FZT8AD&marketplace=FLIPKART&q=MOTO+Razr+40+Ultra+5G&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=6db74c57-5b80-490e-81c6-75ab04090df9.MOBGRZGG4TEDXYM2.SEARCH&ppt=pp&ppn=pp&ssid=3895pb29ls0000001711938468987&qH=9ae5e1f44d536858',
    "oneplus 12 5g": 'https://www.flipkart.com/oneplus-12r-cool-blue-256-gb/p/itm347349f7db2f2?pid=MOBGXGT7HKG8JFGU&lid=LSTMOBGXGT7HKG8JFGURHLJM9&marketplace=FLIPKART&q=oneplus+12+5g&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=2ae321f0-898f-4e00-a975-9f42a374c8d0.MOBGXGT7HKG8JFGU.SEARCH&ppt=pp&ppn=pp&ssid=cek3gp0g8w0000001711938653358&qH=243fab4fddbfe007',
    "xiaomi 12 pro": 'https://www.flipkart.com/xiaomi-12-pro-5g-noir-black-256-gb/p/itm67bddf0d43d59?pid=MOBGDZ84RS67ZTEP&marketplace=FLIPKART',
    "google pixle 8 pro": 'https://www.flipkart.com/google-pixel-8-pro-bay-128-gb/p/itm51f9522df8e95',
    "nord 2t 5g": 'https://www.flipkart.com/oneplus-nord-ce-2-lite-5g-black-dusk-128-gb/p/itm537fc2aa73747?pid=MOBGHBZHB7YJT5HF&lid=LSTMOBGHBZHB7YJT5HFFAN8HA&marketplace=FLIPKART&q=nord+2t+5g&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=5ed130c6-d203-4ea3-8c0e-4cf30330efa5.MOBGHBZHB7YJT5HF.SEARCH&ppt=pp&ppn=pp&ssid=meqskdns6o0000001711939212711&qH=4e2e6fbb815cd661',
    "redmi note 5 pro": 'https://www.flipkart.com/redmi-note-5-pro-black-64-gb/p/itmf2fc3xgmxnhpx?pid=MOBF28FTQPHUPX83&lid=LSTMOBF28FTQPHUPX83H7IIOZ&marketplace=FLIPKART&q=redmi+note+5+pro&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=914d9ac5-7ca4-490c-92ca-ba677703b52b.MOBF28FTQPHUPX83.SEARCH&ppt=pp&ppn=pp&ssid=hg1ny3cs5s0000001711939261314&qH=286b43aac83aafdc',   
    # Add more products as needed
}
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip',
        'DNT': '1',  # Do Not Track Request Header
        'Connection': 'close'
    }
def get_product_info(product_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip',
        'DNT': '1',  # Do Not Track Request Header
        'Connection': 'close'
    }
    
    page = requests.get(product_url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    st.write("Selected Product URL AMAZON:", product_url)
    # Extracting product title
    title = soup.find(id='productTitle').get_text().strip()
    st.write("Product Title:", title)
    
    # Extracting price
    price = soup.find('span', class_='a-price-whole').get_text().strip()
    st.write("Price:", price)
    
    # Extracting discount
    discount = soup.find(id='itembox-NoCostEmi').get_text().strip()
    st.write("Discount:", discount)

    # Extracting bank offers
    bank = soup.find(id='itembox-InstantBankDiscount').get_text().strip()
    st.write("Discount:", bank)
    
    # Extracting partner offers
    partner = soup.find(id='itembox-Partner').get_text().strip()
    st.write("Discount:", partner)
    st.write("---------------------------------")
def get_product_info_flipkart(product_url1):
        st.write("Selected Flipkart Product URL:", product_url1)
        result = requests.get(product_url1,headers=headers)
        soup = bs4.BeautifulSoup(result.content, 'html.parser')
        title = soup.find_all('h1', {"class": "yhB1nd"})
        price = soup.find_all('div', {"class": "_30jeq3 _16Jk6d"})
        discount = soup.find_all('li', {"class": "_16eBzU col"})
    # Display the fetched data
        st.write("\nSearching in flipkart....")
        st.write("Flipkart:")
        for item in title:
            st.write("Product title:",item.text)
        for pr in price:
            st.write("Price:",pr.text)
        for d in discount:
            st.write("Discount:",d.text)
        st.write("---------------------------------")
    
# Streamlit app
st.title("Product Information from Amazon and Flipkart")

# Dropdown to select product name
product_name = st.selectbox("Select a product:", list(product_urls.keys()))

if product_name:
    # Get the corresponding URL for the selected product name
    product_url = product_urls[product_name]
    product_url1 = flipkart_product_urls[product_name]
    # st.write("Selected Product URL AMAZON:", product_url)
    # st.write("Selected Product URL FLIPKART:", product_url1)
    # Fetch product information
    get_product_info(product_url)
    get_product_info_flipkart(product_url1)
