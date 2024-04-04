import pytest

from src.models.settings.connection import db_connection_handle
from .events_repository import EventsRepository

db_connection_handle.connect_to_db()

@pytest.mark.skip(reason="New database registration")
def test_insert_event():
  event = {
    "uuid": "my-secret-uuid 2",
    "title": "my title 2",
    "slug": "my slug required 2",
    "maximum_attendees": 20,
  }

  events_repository = EventsRepository()
  response = events_repository.insert_event(event)

  print(response)

@pytest.mark.skip(reason="Return database registration by id")
def test_get_event_by_id():
  event_id = "my-secret-uuid"
  
  events_repository = EventsRepository()
  response = events_repository.get_event_by_id(event_id)

  print(response)
  print(".")
  print("Title: ", response.title)
  print(".")