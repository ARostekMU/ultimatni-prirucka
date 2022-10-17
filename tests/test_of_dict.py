from ultimatni_prirucka.of_dict import OfDict


def test_can_create():
    OfDict(name="FoamFile", content=dict())


def test_can_access_content():
    a = OfDict(name="FoamFile", content=dict())
    a.content


def test_can_use_str():
    a = OfDict(name="FoamFile", content=dict())
    str(a)


def test_can_use_str():
    a = OfDict(name="test_dict", content={"version":2.0})
    output = str(a)
    string = """\
test_dict
{
version 2.0
}"""
    assert output == string


def test_can_use_str_with_list():
    a = OfDict(name="test_dict", content={"version":[2.0,3.0]})
    output = str(a)
    string = """\
test_dict
{
version 2.0 3.0
}"""
    assert output == string