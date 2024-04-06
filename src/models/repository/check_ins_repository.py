from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from src.models.settings.connection import db_connection_handle
from src.models.entities.check_ins import CheckIns

from src.errors.error_types.http_conflict import HttpConflictError

class CheckInRepository:
  def insert_check_in(self, attendee_id: str) -> str:
    with db_connection_handle as database:
      try:
        check_in = (CheckIns(attendeeId=attendee_id))

        database.session.add(check_in)     
        database.session.commit()
      
        return attendee_id
      except IntegrityError:
        raise HttpConflictError('Check-In already registered!')
      
      except Exception as exception:
        database.session.rollback()
        raise exception
    