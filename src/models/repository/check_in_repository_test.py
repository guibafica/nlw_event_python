import pytest

from src.models.settings.connection import db_connection_handle
from .check_ins_repository import CheckInRepository

db_connection_handle.connect_to_db()

@pytest.mark.skip(reason="New database registration")
def test_insert_check_in():
  attendee_id = "my-secret-attendee-uuid"

  check_ins_repository = CheckInRepository()
  response = check_ins_repository.insert_check_in(attendee_id)

  print(response)
