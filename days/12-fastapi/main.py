import datetime
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl, parse_file_as

CHECKINS = "../data/untappd.json"

app = FastAPI()


class Checkin(BaseModel):
    beer_name: str
    brewery_name: str
    beer_type: str
    beer_abv: str | None
    beer_ibu: str | None
    comment: str | None
    venue_name: str | None
    venue_city: str | None
    venue_state: str | None
    venue_country: str | None
    venue_lat: str | None
    venue_lng: str | None
    rating_score: str | None
    created_at: datetime.datetime
    checkin_url: str | None
    beer_url: HttpUrl | None
    brewery_url: HttpUrl | None
    brewery_country: str | None
    brewery_city: str | None
    brewery_state: str | None
    flavor_profiles: str | None
    purchase_venue: str | None
    serving_type: str | None
    checkin_id: str
    bid: str
    brewery_id: str
    photo_url: HttpUrl | None
    global_rating_score: float | None
    global_weighted_rating_score: float | None
    tagged_friends: str | None
    total_toasts: str | None
    total_comments: str | None


def _read_data():
    return parse_file_as(list[Checkin], CHECKINS)


@app.get("/checkins", response_model=list[Checkin])
async def checkins():
    return _read_data()


@app.get("/checkins/{id}", response_model=Checkin)
async def checkin(id: int):
    return _read_data()[id]
