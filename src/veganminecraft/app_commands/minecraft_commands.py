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
from typing import Literal, Optional, Union

from discord import app_commands

import asyncio
from datetime import datetime, timezone

import discord
from discord.ext import commands

from veganminecraft.bot.discord_bot import DiscordBot
from veganminecraft.socket import handler

class MinecraftCommands(commands.Cog):
    def __init__(self, bot: DiscordBot):
        self.__bot = bot

    @app_commands.command(name="say", description="Speak in minecraft.")
    @app_commands.describe(message="Specify a message.")
    async def say_a_message_app_command(
        self,
        interaction: discord.Interaction,
        message: str,
    ):
        if interaction.channel.id == self.__bot.config["minecraft_channel_snowflake"]:
            handler.send_to_minecraft(interaction.user.display_name, message)
        await interaction.response.send_message(f"{interaction.user.mention} said: {message}")


    @app_commands.describe(
        spec="Specify directly to the guild (~), global to guild (*), clear and sync (^) and global sync (None).",
        guild="Specify which guild to sync.",
    )
    async def sync_app_command(
        self,
        interaction: discord.Interaction,
        spec: Optional[Literal["~", "*", "^"]] = None,
        guild: discord.Guild | None = None,
    ) -> discord.Message:
        if interaction.guild is None:
            return await interaction.response.send_message(
                "This command must be used in a server.", ephemeral=True
            )
        if interaction.channel is None:
            return await interaction.response.send_message(
                "This command must be used in a server channel.", ephemeral=True
            )
        bot: DiscordBot = DiscordBot.get_instance()
        ret = 0
        synced = []
        if not guild:
            if spec == "~":
                synced = await self.__bot.tree.sync(guild=interaction.guild)
            elif spec == "*":
                if interaction.guild is None:
                    return await interaction.response.send_message(
                        "This command must be executed in a server.",
                        ephemeral=True,
                    )
                self.__bot.tree.copy_global_to(guild=interaction.guild)
                synced = await self.__bot.tree.sync(guild=interaction.guild)
            elif spec == "^":
                self.__bot.tree.clear_commands(guild=interaction.guild)
                await self.__bot.tree.sync(guild=interaction.guild)
            else:
                synced = await self.__bot.tree.sync()
            try:
                if spec is None:
                    msg = f"Synced {len(synced)} commands globally."
                else:
                    msg = f"Synced {len(synced)} commands to the current server."
                return await interaction.response.send_message(msg)
            except Exception as e:
                return await interaction.response.send_message(str(e).capitalize())
        else:
            if isinstance(guild.target, discord.Guild):
                guild_obj = guild.target
            else:
                return await interaction.response.send_message(
                    "This command must target a valid server.", ephemeral=True
                )
            try:
                await self.__bot.tree.sync(guild=guild_obj)
            except discord.HTTPException:
                pass
            else:
                ret += 1
        return await interaction.response.send_message(f"Synced the tree to {ret}.")

    @commands.command(name="sync", help="Sync app commands.")
    async def sync_text_command(
        self,
        ctx: commands.Context,
        spec: Optional[Literal["~", "*", "^"]] = None,
        *,
        guilds: Union[commands.Greedy[discord.Object], None] = None,
    ) -> discord.Message:
        if ctx.guild is None:
            return await ctx.send("This command must be used in a server.")
        if ctx.channel is None:
            return await ctx.send(
                "This command must be used in a server channel."
            )
        bot: DiscordBot = DiscordBot.get_instance()
        synced = []
        if not guilds:
            if spec == "~":
                synced = await ctx.bot.tree.sync(guild=ctx.guild)
            elif spec == "*":
                ctx.bot.tree.copy_global_to(guild=ctx.guild)
                synced = await ctx.bot.tree.sync(guild=ctx.guild)
            elif spec == "^":
                ctx.bot.tree.clear_commands(guild=ctx.guild)
                await ctx.bot.tree.sync(guild=ctx.guild)
            else:
                synced = await ctx.bot.tree.sync()
            try:
                if spec is None:
                    msg = f"Synced {len(synced)} commands globally."
                else:
                    msg = f"Synced {len(synced)} commands to the current server."
                return await ctx.send(msg)
            except Exception as e:
                return await ctx.send(str(e).capitalize())
        ret = 0
        for guild in guilds:
            try:
                await ctx.bot.tree.sync(guild=guild)
            except discord.HTTPException:
                pass
            else:
                ret += 1
        return await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")



 
async def setup(bot: DiscordBot):
    await bot.add_cog(MinecraftCommands(bot))
 
