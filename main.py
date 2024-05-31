"""
REMEMBER, THE CODE IS COMPLETELY PROVIDED BY TIENANH109
"""
import discord
import requests
from discord.ext import commands

API_KEY = "YOUR API KEY"

bot = commands.Bot(command_prefix='/')

@bot.slash_command(name="gemini-pro-ai", description="AI by Google!")
async def ai(ctx, prompt: str):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"
    headers = {'Content-Type': 'application/json'}
    data = {"contents": [{"parts": [{"text": prompt}]}]}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        content = response.json()["candidates"][0]["content"]["parts"][0]["text"]
        await ctx.defer()
        await ctx.respond(content=content)
    else:
        await ctx.respond(content="Error!")

bot.run("YOUR BOT TOKEN")
