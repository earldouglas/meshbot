from meshtastic.mesh_interface import MeshInterface
from meshtastic.protobuf.mesh_pb2 import MeshPacket
from re import IGNORECASE
from re import fullmatch
from typing import Optional


def _get_hop_count(packet: MeshPacket) -> Optional[int]:
    if "hopStart" in packet and "hopLimit" in packet:
        return packet["hopStart"] - packet["hopLimit"]
    else:
        return None


def _get_node_name(mesh_interface: MeshInterface, node_id: int) -> Optional[str]:
    try:
        return mesh_interface.nodesByNum[node_id]["user"]["shortName"]
    except KeyError:
        return None


def get_reply(packet, mesh_interface) -> Optional[str]:

    reply: Optional[str] = None

    if "decoded" in packet and "text" in packet["decoded"]:
        if fullmatch(r"^\s*test\s*$", packet["decoded"]["text"], flags=IGNORECASE):
            print(f"received test from {packet["fromId"]}")

            rx_snr = packet["rxSnr"]
            rx_rssi = packet["rxRssi"]
            rx_time = packet["rxTime"]

            hop_string = ""

            hop_count = _get_hop_count(packet)
            if hop_count is not None:
                hop_string = f" after {hop_count} hops"

            name = _get_node_name(mesh_interface, packet["from"])
            if name is None:
                name = packet["fromId"]

            reply = f"{name}: Received{hop_string}.\nSNR {rx_snr}dB  RSSI {rx_rssi}dBm"

    return reply
