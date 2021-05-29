from pylib.SpeechToText import SpeechConverter

def test_converter():
    assert SpeechConverter().getText('three dollars') == '$3'