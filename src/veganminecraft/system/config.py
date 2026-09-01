"""!/bin/python3
config.py  The purpose of this program is to provide the primary configuration.

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

import os
from typing import Any, Dict

from dotenv import load_dotenv


class Config:

    _config = None

    @classmethod
    def get_config(cls) -> Dict[str, Any]:
        load_dotenv()
        _config = {
            "bot_api_key": os.environ["BOT_API_KEY"],
            "client_id": os.environ["CLIENT_ID"],
            "client_secret": os.environ["CLIENT_SECRET"],
            "redirect_uri": os.environ["REDIRECT_URI"],
            "discord_owner_id": int(os.environ["DISCORD_OWNER_ID"]),
            "logging_level": os.environ["LOGGING_LEVEL"],
        }
        _config["release_mode"] = str(os.environ.get("RELEASE_MODE")).lower() in (
            "1",
            "true",
        )
        return _config
