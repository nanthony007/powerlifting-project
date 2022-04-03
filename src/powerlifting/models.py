from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel

# enum for states?

class Meet(BaseModel):
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
