from meshtastic.mesh_interface import MeshInterface
from meshtastic.protobuf.mesh_pb2 import MeshPacket
from meshtastic.protobuf.mesh_pb2 import MyNodeInfo
from meshtastic.protobuf.mesh_pb2 import ToRadio
from queue import Empty
from queue import Queue
from stub_packet import stub_packet
from typing import Optional


class StubMeshInterface(MeshInterface):

    send_queue: Queue

    def sendAndReceive(
        self: MeshInterface, payload: str, timeout: float = 0.1
    ) -> Optional[MeshPacket]:

        tx = stub_packet(self.myInfo.my_node_num, payload)
        self._handlePacketFromRadio(tx)

        rx: MeshPacket = None

        try:
            rx = self.send_queue.get(timeout=timeout)
            self.send_queue.task_done()
        except Empty:
            pass

        return rx

    def _sendToRadio(self: MeshInterface, toRadio: ToRadio) -> None:
        if "packet" in toRadio:
            self.send_queue.put(toRadio.packet)

    def __init__(self: MeshInterface) -> None:
        super().__init__()

        self.send_queue: Queue = Queue()

        my_node_id = "!00000001"
        my_node_num = 1
        my_node = {
            "num": my_node_num,
            "user": {
                "id": my_node_id,
                "longName": "My Node",
                "shortName": "MN",
                "macaddr": "foo",
                "hwModel": "FOO",
            },
            "position": {},
            "lastHeard": 123,
        }

        their_node_id = "!00000002"
        their_node_num = 2
        their_node = {
            "num": their_node_num,
            "user": {
                "id": their_node_id,
                "longName": "Their Node",
                "shortName": "TN",
                "macaddr": "bar",
                "hwModel": "BAR",
            },
            "position": {},
            "lastHeard": 123,
        }

        self.nodes = {
            my_node_id: my_node,
            their_node_id: their_node,
        }

        self.nodesByNum = {
            my_node_num: my_node,
            their_node_num: their_node,
        }

        myInfo = MyNodeInfo()
        self.myInfo = myInfo
        self.myInfo.my_node_num = my_node_num

        self._connected()
