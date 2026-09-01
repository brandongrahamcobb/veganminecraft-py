"""!/bin/python3
discord_bot.py This is essentially a stripped version of Rapptz advanced_startup.py.

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

import logging
from typing import Self, cast

import discord
from discord.ext import commands

class DiscordBot(commands.Bot):
    _instance = None

    def __init__(
        self,
        *,
        config,
        initial_extensions: list[str],
        logger: logging.Logger,
        **kwargs,
    ):
        DiscordBot._instance = self
        intents = discord.Intents.all()
        self.config = config
        if self.config["release_mode"] is False:
            intents.message_content = False
            intents.presences = False
            intents.members = False
        super().__init__(
            command_prefix="!",
            help_command=None,
            intents=intents,
            **kwargs,
        )
        self.__initial_extensions = initial_extensions
        self.logger = logger

    async def setup_hook(self) -> None:
        for ext in self.__initial_extensions:
            await self.load_extension(ext)


    @classmethod
    def get_instance(cls) -> Self:
        if cls._instance is None:
            raise RuntimeError("DiscordBot instance has not been created yet")
        return cast(Self, cls._instance)
