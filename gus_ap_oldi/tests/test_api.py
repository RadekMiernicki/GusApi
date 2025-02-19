# -*- coding: utf-8
from __future__ import unicode_literals
import os

import pytest
import zeep

from gus import GUS, ApiAtr, ReportTypes

api_atr = ApiAtr()

@pytest.fixture
def client():
    return GUS(api_atr=api_atr)


def test_service(client):
    assert type(client.service) == zeep.proxy.ServiceProxy

def test_get_regon_using_nip(client, nip='5261040828'):
    assert client._get_regon(nip) == '00033150100000'

def test_get_regon_using_regon(client, regon='00033150100000'):
    assert client._get_regon(regon=regon) == '00033150100000'


