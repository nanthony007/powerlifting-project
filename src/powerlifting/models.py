from __future__ import annotations

from datetime import datetime
import typing

from pydantic import BaseModel, Field, validator


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


class MainModel(BaseModel):
    @validator('*', pre=True)
    def empty_str_to_none(cls, v):
        if v == '':
            return None
        return v


class Lift(MainModel):
    lift1: typing.Optional[float] = None
    lift2: typing.Optional[float] = None
    lift3: typing.Optional[float] = None
    lift4: typing.Optional[float] = None




# old standard
# Name,Place,Sex,WeightClassKg,Age,Division,Best3SquatKg,Best3BenchKg,Best3DeadliftKg,TotalKg,Equipment,Event

# PREFERRED; gold standard, newer
# Place,Name,State,WeightClassKg,BodyweightKg,BirthDate,Age,Squat1Kg,Squat2Kg,Squat3Kg,Best3SquatKg,Bench1Kg,Bench2Kg,Bench3Kg,Best3BenchKg,Deadlift1Kg,Deadlift2Kg,Deadlift3Kg,Best3DeadliftKg,TotalKg,Bench4Kg,Deadlift4Kg,Event,Equipment,Sex,Division,Tested


# currently only supporting PREFERRED format
class Athlete(MainModel):
    name: typing.Optional[str] = None
    place: typing.Optional[str] = None
    state: typing.Optional[str] = None
    weight_class: typing.Optional[float] = None
    body_weight: typing.Optional[float] = None
    age: typing.Optional[int] = None
    best_squat: typing.Optional[float] = None
    best_bench: typing.Optional[float] = None
    best_deadlift: typing.Optional[float] = None
    total: typing.Optional[float] = None
    event: typing.Optional[str] = None # SBD, B, DL, etc. = None
    equipment: typing.Optional[str] = None  # raw, multi-ply, single-ply
    sex: typing.Optional[str] = None  # m or f
    division: typing.Optional[str] = None
    squats: typing.Optional[Lift] = None
    benches: typing.Optional[Lift] = None
    deadlifts: typing.Optional[Lift] = None
    birth_date: typing.Optional[str] = None


    @classmethod
    def New(cls, info: dict[str, str]) -> Athlete:
        squat = Lift(
            lift1=info.get("Squat1Kg"),
            lift2=info.get("Squat2Kg"),
            lift3=info.get("Squat3Kg"),
            lift4=info.get("Squat4Kg"),
        )
        bench = Lift(
            lift1=info.get("Bench1Kg"),
            lift2=info.get("Bench2Kg"),
            lift3=info.get("Bench3Kg"),
            lift4=info.get("Bench4Kg"),
        )
        dl = Lift(
            lift1=info.get("DeadLift1Kg"),
            lift2=info.get("DeadLift2Kg"),
            lift3=info.get("DeadLift3Kg"),
            lift4=info.get("DeadLift4Kg"),
        )
        return cls(
            name=info['Name'].replace("#1", "").strip(),
            place=info['Place'],
            state=info['State'],
            weight_class=info["WeightClassKg"].replace("+", "").strip(),
            body_weight=info["BodyweightKg"],
            birth_date=info["BirthDate"],
            age=info["Age"],
            division=info["Division"],
            total=info["TotalKg"],
            sex=info["Sex"],
            equipment=info["Equipment"],
            event=info["Event"],
            best_squat=info["Best3SquatKg"],
            best_bench=info["Best3BenchKg"],
            best_deadlift=info["Deadlift3Kg"],
            deadlifts=dl,
            benches=bench,
            squats=squat,
        )


class AthleteList(MainModel):
    athletes: list[Athlete]


# TODO: write validators  @nanthony007
# assert max_squat == best_squat
# consider enums for some choices



