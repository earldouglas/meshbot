from pubsub.pub import subscribe
from re import IGNORECASE
from re import fullmatch
from typing import Optional


def on_receive_message(packet, interface) -> None:

    mesh_interface = interface

    del packet["raw"]

    def reply(text) -> None:
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

    if "decoded" in packet and "text" in packet["decoded"]:
        if fullmatch(
            r"^\s*ping\s*$",
            packet["decoded"]["text"],
            flags=IGNORECASE,
        ):
            text = "Pong"
            reply(text)


def start() -> None:
    subscribe(on_receive_message, "meshtastic.receive.text")
