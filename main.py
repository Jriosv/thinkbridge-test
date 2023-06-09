import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import time
import pandas as pd

async def visit_page_and_return_html(url):
    print('visiting web page..')
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)

        page = await browser.new_page()
                
        #await page.set_extra_http_headers({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"})
        await page.goto(url)
        

        #Bypass the cloudflare verification
        for retry in range(3):
            try:
                locator = page.frame_locator("iframe").get_by_role("checkbox")
                await locator.set_checked(True)
                break
            except:
                print('Bypass failed.trying again...')
                

        
        time.sleep(10) #BAD PRACTICE!!! But it was my last option before the day finish
        
        try:
            #Wait until this element appears
            page.frame_locator('iframe').get_by_text('Save to My Lists')
        except:
            #iframe always appear
            print('Locating page elemente failed')
            page.frame_locator('iframe')
        
        # Get the HTML content using Playwright
        html_content = await page.content()

        return html_content

async def handle_html(html_content):
    print('Extracting data..')
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    name_element = soup.find('div', {'itemprop': 'name'})

    try:
        name = name_element.text
    except:
        print('Element not found by bs4: div itemprop=name')
        name = ''
    
    url_element = soup.find('a', {'itemprop': 'url'})
    
    try:
        url = url_element['href']
    except:
        print('Element not found by bs4: a itemprop=url')
        url=''
        
    
    # Return the extracted data
    return name,url


async def main():

    df = pd.read_csv('g2-data.csv')
    
    urls = df['url'].tolist()
    
    names = []
    original_urls = []
    
    for url in urls:    
        html_content = await visit_page_and_return_html(url)

        name,url = await handle_html(html_content)

        names.append(name)
        original_urls.append(url)

    df_new = pd.DataFrame({'Original names': names, 'Original urls': original_urls})
    
    # Save the DataFrame to a CSV file
    df_new.to_csv('scraped_data.csv', index=False)
                   
asyncio.run(main())