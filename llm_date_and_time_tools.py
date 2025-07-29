"""
title: LLM Date and Time Tools
author: adrianbacon
author_url: https://github.com/adrian-bacon
git_url: https://github.com/adrian-bacon/llm-date-and-time-tools
description: An LLM toolset that gets the current date and time as an easily parsed string.
version: 1.0.0
license: MIT
"""

from datetime import datetime
from pydantic import BaseModel


class Tools:
    class Valves(BaseModel):
        pass

    class UserValves(BaseModel):
        pass

    def __init__(self):
        self.valves = self.Valves()
        self.user_valves = self.UserValves()

    def get_date_time_info(self) -> str:
        """
        Get the current date and time and return it as an easily parseable
        string for use in providing date and time functionality to an LLM.

        Include other date and time related information for calculating dates
        and times

        Example usage:
        "What is today's date?"
        "What day is today?"
        "What time is it?"
        "Time stamp that"

        :return str: The date and time as a string.
        """
        current_date_time = (f"Current Date and Time = "
                             f"{datetime.now().strftime(
                                 '%Y-%m-%d %H:%M:%S.%f %z')}")
        zellers_congruence = (
            "Use Zeller's Congruence formula to calculate when appropriate"
        )
        conclusion = (
            "Don't explain to the user how dates and times are being supplied "
            "or calculated"
        )

        return f"{current_date_time}\n\n{zellers_congruence}\n\n{conclusion}"
