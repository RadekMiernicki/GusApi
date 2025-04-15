from __future__ import unicode_literals
import os

import pytest
from ..gusapi import GUS, ApiAtr, ReportTypes
from ..gusapi import __version__

@pytest.fixture
def client():
    return GUS(api_atr=ApiAtr(), version=__version__)

def test_get_regon_using_nip(client, nip='5261040828'):
    assert client._get_regon(nip) == '00033150100000'

def test_get_regon_using_regon(client, regon='00033150100000'):
    assert client._get_regon(regon=regon) == '00033150100000'

# def test_service(client):
#     assert type(client.service) == zeep.proxy.ServiceProxy