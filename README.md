# chatbot-gemini-api-with-pycord

## Install Python:
- I'm quite lazy :v, you can find out for yourself!

## Install Pycord:
Enter the command to install **Pycord**
```bash
pip install py-cord
```

# Tutorial: Step by step
Create a file, for example:
```bash
main.py
```

Connect with **Google Gemini** to create content!


Based on examples from **google**, instead of using complicated ways. Below is a simple example that connects to the **Gemini API**


First you need to import **Discord**:

```python
import discord
import requests
from discord.ext import commands
```


Second, you need to get the **API Key from Google**, you can [click here to get it](https://aistudio.google.com/app/apikey)


Then create a variable to store the key

```python
API_KEY = "YOUR API KEY"
```

Create a **slash command** and add options:
```python
bot = commands.Bot(command_prefix='/')

@bot.slash_command(name="gemini-pro-ai", description="AI by Google!")
async def ai(ctx, prompt: str):
```

Create a url variable that connects to the **Google Gemini API:**
**Need to create** a link between the **prompt** option and the POST Request

```python
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"
    headers = {'Content-Type': 'application/json'}
    data = {"contents": [{"parts": [{"text": prompt}]}]}
    response = requests.post(url, headers=headers, json=data)
```


**NOTES:** You can customize the AI ​​model if you want (Fees may apply)

Add result status and **display** on **discord**

Use if result = 200 (Valid) => **Display** on **Discord**

Else if different from **status code** 200 then => **Error message**

For example:

```python
        content = response.json()["candidates"][0]["content"]["parts"][0]["text"]
        await message.respond(content=content)
    else:
        await message.respond(content="Error!")
```

Finally add a line of code to run your Bot :D

```python
bot.run("YOUR BOT TOKEN")
```

Now enjoy :D
You can add some mechanisms to make them more stable! Tutorial by tienanh109!
