import webbrowser as wb
def webauto():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    URLS = ("https://leetcode.com/","https://github.com/naazkakria/IOT","https://meet.google.com/xms-wzmj-bip?authuser=0&hl=en")
 ## in urls you  just have to paste link of websites you want to get open automaticly 
    for url in URLS:
        wb.get(chrome_path).open(url)
webauto()