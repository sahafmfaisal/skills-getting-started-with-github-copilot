import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


_ORIGINAL_ACTIVITIES = copy.deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Ensure tests are isolated despite shared in-memory activity data."""
    activities.clear()
    activities.update(copy.deepcopy(_ORIGINAL_ACTIVITIES))

    yield

    activities.clear()
    activities.update(copy.deepcopy(_ORIGINAL_ACTIVITIES))


@pytest.fixture
def client():
    return TestClient(app)
