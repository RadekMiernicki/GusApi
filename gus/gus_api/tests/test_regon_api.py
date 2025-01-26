import pytest
from vcr import VCR

from regon.exceptions import RegonAPIError
from regon.api import RegonAPI

from tests.utils import (
    check_structure_base_data,
    check_structure_address,
    check_structure_contact,
    check_structure_pkd,
)

@pytest.fixture
def api():
    return RegonAPI(api_key=None)

def test_required_lockup(api):
    with pytest.raises(
        AttributeError, match=r"At least one parameter \(nip, regon, krs\) is required."
        ):
        api.find_by()