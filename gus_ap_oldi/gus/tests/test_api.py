from __future__ import unicode_literals
import os

import pytest
from gus import GUS, ApiAtr, ReportTypes
from gus import __version__

@pytest.fixture
def client():
    return GUS(api_atr=ApiAtr(), version=__version__)
