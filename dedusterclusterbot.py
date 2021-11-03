# bot.py
import os
import sqlite3
import discord
import time
from requests import get
from random import randrange, choice, randint
from datetime import datetime
import pytz
import asyncio
import re
conn = sqlite3.connect("database.db")
c = conn.cursor()
TOKEN = ('MjAyMzAyODIxOTg5NzQ0NjQx.V4SHLw.ywjIYXKL0Kct4EieqzQS1zbZbmU')
client = discord.Client()
droppers = []
ban = []
finished = []
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
@client.event
async def on_message(message):
    vipnotify = message.guild.get_role(904547297583587338)
    humannotify = message.guild.get_role(904547265585221722)
    print("0")
    global ban, finished
    if message.channel.name == "❗vip-drop💸" or message.channel.name == "❗humans-only-drop💸":
        print("1")
        if "$airdrop" in str(message.content):
            print("2")
            if message.id not in ban:
                print("5")
                droplog = client.get_channel(905111515219238963)
                text = message.content.split()
                print(text)
                removewords = ['for', 'users']
                for word in list(text):  # iterating on a copy since removing will mess things up
                    if word in removewords:
                        text.remove(word)
                print(text)
                value = text[1]
                currency = text[2]
                if "$" in value:
                    value = (re.sub('[a-z$]', '', value))
                    value = float(value)
                    print(value)
                    print("this is the value before checking")
                    if value >= .02:
                        new = str(value)
                        value = "$" + new
                        if len(text) < 5:
                            ban.append(message.id)
                            if message.channel.name == "❗vip-drop💸":
                                await droplog.send("{} in {} was just airdropped in {} from {} {}".format(value, currency, message.channel.name, message.author.mention, vipnotify.mention))
                            if message.channel.name == "❗humans-only-drop💸":
                                await droplog.send("{} in {} was just airdropped in {} from {} {}".format(value, currency, message.channel.name, message.author.mention, humannotify.mention))

                        elif len(text) == 5:
                            users = text[4]
                            ban.append(message.id)
                            if message.channel.name == "❗vip-drop💸":
                                await droplog.send("{} in {} was just airdropped in {} from {} for {} users {}".format(value, currency,message.channel.name, message.author.mention, users, vipnotify.mention))
                            if message.channel.name == "❗humans-only-drop💸":
                                await droplog.send("{} in {} was just airdropped in {} from {} for {} users.{}".format(value, currency,message.channel.name, message.author.mention, users, vipnotify.mention))

                else:
                    print("failure")
@client.event
async def on_message_edit(before, after):
    global ban
    if after.author.id == 617037497574359050:
        if after.id in ban:
            if after.id not in finished:
                finished.append(after.id)
                ban.append(after.id)
                print("Drop over.")
        else:
            return
        


client.run(TOKEN)
