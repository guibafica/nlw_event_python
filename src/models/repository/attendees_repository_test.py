import pytest

from src.models.settings.connection import db_connection_handle
from .attendees_repository import AttendeesRepository

db_connection_handle.connect_to_db()

@pytest.mark.skip(reason="New database registration")
def test_insert_attendee():
  event_id = "e85b93c8-6207-43fd-8598-b169aeaf1af6"
  attendees_info = {
    "uuid": "secret-uuid-test",
    "name": "Name test",
    "email": "testemail@email.com",
    "event_id": event_id,
  }
  
  attendees_repository = AttendeesRepository()
  response = attendees_repository.insert_attendee(attendees_info)

  print(response)

@pytest.mark.skip(reason="Return database registration by id")
def test_get_attendee_badge_by_id():
  attendee_id = "my-secret-attendee-uuid"
  
  attendees_repository = AttendeesRepository()
  response = attendees_repository.get_attendee_badge_by_id(attendee_id)

  print(response)