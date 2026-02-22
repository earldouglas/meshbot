from re import IGNORECASE
from re import fullmatch
from typing import Optional


def get_reply(packet) -> Optional[str]:

    reply: Optional[str] = None

    if "decoded" in packet and "text" in packet["decoded"]:
        if fullmatch(r"^\s*ping\s*$", packet["decoded"]["text"], flags=IGNORECASE):
            reply = "Pong"

    return reply
