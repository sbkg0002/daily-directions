#!/usr/bin/env python3
import googlemaps
import os
from datetime import datetime
from notify_run import Notify

GOOGLE_KEY = os.environ["GOOGLE_KEY"]
NOTIFY_KEY = os.environ["NOTIFY_KEY"]

FROM = os.environ["FROM"]
TO = os.environ["TO"]

gmaps = googlemaps.Client(key=GOOGLE_KEY)

now = datetime.now()

directions_result = gmaps.directions(FROM,
                                     TO,
                                     mode="driving",
                                     departure_time=now)

summary = directions_result[0]['summary']

notify = Notify()
notify.send(summary)
