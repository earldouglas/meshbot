from pubsub.pub import subscribe
from re import IGNORECASE
from re import fullmatch
from repliers import ping
from repliers import test
from typing import Callable
from typing import List
from typing import Optional


def on_receive_message(packet, interface) -> None:

    mesh_interface = interface

    def send_reply(text) -> None:
        if packet["toId"] == "^all":
            channel = 0
            if "channel" in packet:
                channel = packet["channel"]
            mesh_interface.sendText(
                channelIndex=channel, replyId=packet["id"], text=text
            )
        else:
            mesh_interface.sendText(
                destinationId=packet["fromId"], replyId=packet["id"], text=text
            )

    for get_reply in [
        lambda: ping.get_reply(packet),
        lambda: test.get_reply(packet, mesh_interface),
    ]:
        reply: Optional[str] = get_reply()
        if reply is not None:
            send_reply(reply)


def start() -> None:
    subscribe(on_receive_message, "meshtastic.receive.text")
