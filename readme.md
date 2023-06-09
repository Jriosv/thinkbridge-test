##

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
