from fortune import fortune
from re import IGNORECASE
from re import fullmatch
from typing import Optional


def _get_fortune() -> str:
    x: str = ""
    while len(x) == 0 or len(x) > 200:
        x = fortune()
    return x


def get_reply(packet) -> Optional[str]:

    reply: Optional[str] = None

    if "decoded" in packet and "text" in packet["decoded"]:
        if fullmatch(r"^\s*fortune\s*$", packet["decoded"]["text"], flags=IGNORECASE):
            reply = _get_fortune()

    return reply
