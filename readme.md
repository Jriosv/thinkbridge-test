##

## Execution

Create a virtual environment to manage the project dependencies indepently of your computer  
>python -m venv venv

After that, turn on the virtual environment, in my case I'm using a bash terminal so I activate the venv in this way:  
>source venv/Scripts/activate

Once your virtual environment is running, install the dependencies with the following command:
>pip install -r requirements.txt

After thath, we need to download new browser drivers with the following command:
>playwright install
