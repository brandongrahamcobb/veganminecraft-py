"""!/bin/python3
main.py The purpose of this program is to be the primary executable for VeganMinecraft.

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

from veganminecraft.bot.discord_bot import DiscordBot
from veganminecraft.inc.helpers import DISCORD_COGS, PATH_LOG
from veganminecraft.system.config import Config
from veganminecraft.system.logger import logger, setup_logging


async def main():

    config = Config().get_config()
    setup_logging(config, PATH_LOG)
    discord_bot = DiscordBot(
        config=config, initial_extensions=DISCORD_COGS, logger=logger
    )
    await discord_bot.start(config["bot_api_key"])


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Shutting down bots and server...")
