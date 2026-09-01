"""!/bin/python3
helpers.py The purpose of this program is to provide generic parameters and functions.

Copyright (C) 2026  https://github.com/brandongrahamcobb/veganminecraft.git

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

from os.path import expanduser, join
from pathlib import Path

import discord
from discord.ext import commands


#### DEVELOPMENT
RELEASE_MODE = False
#### DIRECTORIES
DIR_BASE = Path.cwd().parent.parent
DIR_HOME = expanduser("~")
#### DISCORD
DISCORD_CHARACTER_LIMITS = [2000, 4000]
DISCORD_CHARACTER_LIMIT = 2000
DISCORD_COGS = [
    "veganminecraft.listeners.generic_event_listeners",
    "veganminecraft.listeners.scheduled_tasks",
]
DISCORD_COGS_CLASSES = [
    "GenericEventListeners",
    "ScheduledTasks",
]
#### PATHS
PATH_LOG = join(DIR_BASE, ".log", "discord.log")
