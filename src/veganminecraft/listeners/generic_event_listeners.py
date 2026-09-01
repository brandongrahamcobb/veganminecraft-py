"""!/bin/python3
generic_event_listeners.py A discord.py cog containing generic event listeners for the VeganMinecraft bot.

Copyright (C) 2026  https://github.com/brandongrahamcobb/veganminecraft-py.git

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import asyncio
from datetime import datetime, timezone

import discord
from discord.ext import commands

from veganminecraft.bot.discord_bot import DiscordBot
from veganminecraft.socket import handler

class GenericEventListeners(commands.Cog):
    def __init__(self, bot: DiscordBot):
        self.__bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> discord.Message | None:
        if message.author.bot:
            return
        bot: DiscordBot = DiscordBot.get_instance()
        if message.channel.id == bot.config["MINECRAFT_CHANNEL_SNOWFLAKE"]:
            handler.send_to_minecraft(message.author.display_name, message.content)

async def setup(bot: DiscordBot):
    await bot.add_cog(GenericEventListeners(bot))
 
