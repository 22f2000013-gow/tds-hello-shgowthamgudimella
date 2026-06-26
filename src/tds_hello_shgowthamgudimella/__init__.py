"""tds-hello-shgowthamgudimella"""

from importlib.metadata import version as _v

__version__ = _v("tds-hello-shgowthamgudimella")


def greet(name: str = "world") -> str:
    if not isinstance(name, str):
        raise TypeError("name must be a str")

    return f"Hello, {name}! — from tds-hello v{__version__}"
