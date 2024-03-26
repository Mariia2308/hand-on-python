"""Testing suite for the Hello World introductory exercise"""

from hello_world import hello

def test_hi_exists():
    """Test to make sure that the program has a method named hi"""
    assert hasattr(hello, "hi")

def test_hi_prints(capsys):
    """Tests that hello.hi prints "Hello World!" """
    hello.hi()
    captured = capsys.readouterr()
    assert captured.out == "Hello World!\n"
