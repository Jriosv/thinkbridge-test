## Explanation
- I visited some web pages to extract the url and build a simple CSV.  
- I used playwright but also bs4 since I don't have a lot of experience with the proposed tool, however, it was an interesting challenge for me.  
- My web scraping consists in open every company details web page, first bypassing cloudflare human verification, after that took the html and extract some useful data with bs4 to store it in a CSV file.  
NOTE: There are a lot of things to improve but today I was working in my current job so I only had a couple hours to finish this challenge.

## Execution

Create a virtual environment to manage the project dependencies:
>python -m venv venv

After that, turn on the virtual environment, in my case I'm using a bash terminal so I activate the venv in this way:  
>source venv/Scripts/activate  

If you don't know how to activate the virtual environment in your pc, search for an easy tutorial in internet, in this case I recommend you check this web page: https://pythonforundergradengineers.com/virtualenv-in-osx-linux-windows.html

Once your virtual environment is running, install the dependencies with the following command:
>pip install -r requirements.txt

After that, we need to download new browser drivers with the following command:
>playwright install
