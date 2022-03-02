from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import enum

# enum for states?

@dataclass
class Meet:
    federation: str
    date_: datetime
    country: str
    state: str
    town: str
    name: str

    # class method, goes on `Meet`
    @classmethod
    def New(cls, info: dict[str, str]) -> Meet:
        return cls(
            federation=info["Federation"],
            date_=datetime.strptime(info["Date"], "%Y-%m-%d"),
            country=info["MeetCountry"],
            state=info["MeetState"],
            town=info["MeetTown"],
            name=info["MeetName"]
        )

    # SAMPLES, DELETE LATER AFTER LEARNING
    
    # object property, read only, goes on `meet`
    @property
    def is_fun(self):
        return True

    # object method, read only, goes on `meet` & needs `()`
    def in_florida(self):
        return self.state == 'FL'

    def is_in_year(self, year):
        return self.date_.year == year