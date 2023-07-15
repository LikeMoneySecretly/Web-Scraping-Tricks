from bs4 import BeautifulSoup
import time
import asyncio
from playwright.async_api import async_playwright

     
#Proof of concept for killing event listeners that are listening for things you don't want
#Using google dev tools console to do the dirty work for us
    


async def killEventListener():
    async with async_playwright() as playwright:
        chromium = playwright.chromium # does not work for "firefox" or "webkit".
        browser = await chromium.connect_over_cdp("http://localhost:9222")
        time.sleep(0.2)
        browser_contexts = browser.contexts[0]
        for page in browser_contexts.pages:
            title = await page.title()
            title = str(title).lower()
            #will navigate to the guardian page and attempt to kill a event listener
            #Ensure your browser is running on port 9222 (add --remote-debugging-port=9222 to the exe in windows)
            if title.__contains__("guardian"):
 
                await page.bring_to_front()
                #await page.wait_for_selector("selector",timeout=10000)
            if title.__contains__("devtools"):
                #Ensure you have devtools already open for the target tab in undocked (separate window) mode
                await page.bring_to_front()
                javascript = 'document.querySelector("#console-prompt > div > div.console-prompt-editor-container > devtools-text-editor").shadowRoot.querySelector("div > div.cm-scroller > div.cm-content.cm-lineWrapping > div").click()'
                await page.evaluate(f"""() => {{{javascript}}}""")
                targetEventListener = "message"
                javascript = 'Object.keys(getEventListeners(window)).forEach(function (name) {var listeners = getEventListeners(window)[name];listeners.forEach(function (object) {if (name === "'+targetEventListener+'"){window.removeEventListener(name, object.listener);}});console.log(name)});'
                
                await page.keyboard.insert_text(javascript)
                await page.keyboard.down("Enter")
                #Solution --> Highjack our good friend the devtools console to do everything for ourselves.
                content = await page.content()
                #You can now use bs4 for example to read the page content without triggering any
                #Event listeners listening to console bullshit like page.querySelector etc
                #e.g.
                """ soup = BeautifulSoup(content,'html.parser')
                result =soup.select(chosen selector)
                print("This is the result "+str(result[0].contents)) """

asyncio.run(killEventListener())
