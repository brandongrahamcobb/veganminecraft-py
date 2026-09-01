"""!/bin/python3
scheduled_tasks.py A discord.py cog containing scheduled tasks for the VeganMinecraft bot.

Copyright (C) 2026  https://github.com/brandongrahamcobb/Vyrtuous.git

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

import time

import discord
from discord.ext import commands, tasks

from veganminecraft.bot.discord_bot import DiscordBot
from veganminecraft.socket import handler


class ScheduledTasks(commands.Cog):
    def __init__(self, bot: DiscordBot):
        self.__bot = bot
        self._ws_task = None

    async def cog_load(self) -> None:
        if self._ws_task is None:
            self._ws_task = self.__bot.loop.create_task(handler.start_ws_server())
            self.__bot.logger.debug(f"Started ws server.")

async def setup(bot: DiscordBot):
    await bot.add_cog(ScheduledTasks(bot))
