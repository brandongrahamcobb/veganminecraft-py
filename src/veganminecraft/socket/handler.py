"""!/bin/python3
handler.py  The purpose of this program is to handle the Minecraft connection.

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
import json
import websockets
from mcrcon import MCRcon

from veganminecraft.bot.discord_bot import DiscordBot

async def handle_mc_connection(websocket):
    bot: DiscordBot = DiscordBot.get_instance()
    async for raw in websocket:
        try:
            data = json.loads(raw)
            player = data["player"]
            message = data["message"]
        except (json.JSONDecodeError, KeyError):
            continue
        channel = bot.get_channel(bot.config["minecraft_channel_snowflake"])
        if channel:
            await channel.send(f"**{player}**: {message}")

async def start_ws_server():
    async with websockets.serve(handle_mc_connection, "0.0.0.0", 8765):
        await asyncio.Future()

def send_to_minecraft(username, content):
    bot: DiscordBot = DiscordBot.get_instance()
    RCON_HOST = bot.config["rcon_host"]
    RCON_PORT = 25575
    RCON_PASSWORD = bot.config["rcon_password"]
    try:
        with MCRcon(RCON_HOST, RCON_PASSWORD, port=RCON_PORT) as mcr:
            safe_content = content.replace('"', '\\"')
            mcr.command(f'tellraw @a {{"text":"[Discord] {username}: {safe_content}"}}')
    except Exception as e:
        print(f"RCON error: {e}")
