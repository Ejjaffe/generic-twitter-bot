# generic-twitter-bot-template
Secure generic template for python twitter bots.

## Setup
### Fork the repo!
Or do something with templates if I've set that up.

### API Tokens
Get your [Twitter API tokens](https://developer.twitter.com/en/support/twitter-api).

### Config File
Create a copy of `template.ini` inside `configs/`. Edit the copy to have your twitter API keys in it. The dir `configs/` is untracked by git to prevent you uploading your keys to github. You know how it is. From the root directory, you can run the following bash command:

```bash
cp template.ini configs/myconfig.ini
```

### Conda Env
In the root directory of the project, create the conda env with:
```bash
conda env create -f generic_twitter_bot.yml
```

## Running The Code
```bash
conda activate generic_twitter_bot
python client.py --config configs/myconfig.ini
```

## Development
### Python Env update - Adding new packages to the Env
While inside the activated conda env:
```bash
conda install {package}
# or, as a last resort:
python -m pip install {package}
```
If you are reinstalling `python-twitter`, you will have to use the last resort option (`pip`). It is not available on conda yet.
### Python Env update - Making your package changes available to others
Storing your changes to the python env from inside the activated conda env:
```bash
conda env export > generic_twitter_bot.yml
```
### Generic Workflow
The main idea is to add modules to `src/` (or another dir/project entirely) and then import them into `client.py` as needed. One pattern I've found to be effective for rapid development is creating a single API object in `client.py` and passing it into instances of an abstract base (or just base) "skill" class that takes the API and does things with it. You can set up a listener or some sort of control flow class this way. Neat Bonus: This way you can also set up a testing account to run your tests on. 

If you've got a better pattern for this, open an issue and let me know. I'm sure there's probably a nicer way to do it.

## Tips / Troubleshooting
### Visual Studio Code `import` / `no package found` Errors
Open the command palate (CTRL + SHIFT + P) and look for `Python: Select Interpreter`. If the conda env for this project (`generic_twitter_bot` by default) cannot be selected, then click `Enter interpreter path`, navigate to your `Anaconda3/envs/` folder, navigate to the folder for your conda environment, and select the `python.exe` file. This will let python know what packages are available in your environment, and automatically activate the env in VSCode terminal windows.

### Relevant Documentation
The documentation you'll need while developing the bot is here:
 - [Twitter Developer Homepage](https://developer.twitter.com/en)
 - [Twitter Standard API V1.1 Docs](https://developer.twitter.com/en/docs/twitter-api/v1)
 - [Python-Twitter Github](https://github.com/bear/python-twitter)
 - [Python-Twitter Docs](https://python-twitter.readthedocs.io/en/latest/)
