import re

import exactextract


def test_version():

    assert re.match("[0-9]+[.][0-9]+[.][0-9]+", exactextract.__version__)
