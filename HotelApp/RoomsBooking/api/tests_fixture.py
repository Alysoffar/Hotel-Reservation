import uuid  # Import uuid for unique usernames
from django.contrib.auth.models import User # type: ignore
import pytest # type: ignore

@pytest.fixture
def create_unique_user():
    user=User.object.create(username='lihekal',password='12345678910')
    return user