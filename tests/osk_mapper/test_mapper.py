import pytest
import pyautogui

from osk_mapper.mapper import KeyLocations
from osk_mapper.exceptions import *


def test_map_using_pixel_difference(monkeypatch):
    def mock_instance_variable():
        class MockZilla:
            def __init__(self):
                self.pixel_space = 25
        return MockZilla()
    monkeypatch.setattr(KeyLocations, '__init__', lambda *args: None)
    test_key1 = (300, 300)
    test_key2 = (100, 100)
    expected = 325, 100
    result = KeyLocations.map_using_pixel_difference(
        mock_instance_variable(), test_key1, test_key2
    )
    assert result == expected


def test_map_using_image_throws_exception_when_no_match_is_found(monkeypatch):
    def mock_instance_variable():
        class MockZilla:
            def __init__(self):
                self.osk_region = (1, 2, 3, 4)
        return MockZilla()
    monkeypatch.setattr(KeyLocations, '__init__', lambda *args: None)
    monkeypatch.setattr(pyautogui, 'locateCenterOnScreen', lambda *args, **kwargs: None)
    with pytest.raises(UnableToDetectKey) as excinfo:
        KeyLocations.map_using_image(mock_instance_variable(), 'foo_key.png')
    assert str(excinfo.value) == "There was no match found on the OSK for the following image: foo_key.png"


def test_detect_osk_icon(monkeypatch):
    monkeypatch.setattr(pyautogui, 'locateCenterOnScreen', lambda *args, **kwargs: None)
    with pytest.raises(UnableToDetectOnScreenKeyboard) as excinfo:
        KeyLocations.detect_osk_icon('test_osk.png')
    assert str(excinfo.value) == "OSK Icon could not be found on the screen."


def test_set_osk_region():
    result = KeyLocations.set_osk_region((100, 100))
    expected = (75, 100, 1000, 800)
    assert result == expected
