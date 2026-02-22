from meshtastic import BROADCAST_ADDR
from meshtastic.protobuf.mesh_pb2 import MeshPacket
from meshtastic.mesh_interface import MeshInterface
from queue import Empty
from queue import Queue
from threading import Thread
from time import sleep
from typing import Callable
from typing import Optional
from typing import Union


class Throttle:

    mesh_interface: MeshInterface
    join: Callable[[], None]

    def __init__(
        self: Throttle, mesh_interface: MeshInterface, delay_secs: int
    ) -> None:

        packet_queue: Queue[
            tuple[
                MeshPacket,
                Union[int, str],
                bool,
                Optional[int],
                Optional[bool],
                Optional[bytes],
            ]
        ] = Queue[
            tuple[
                MeshPacket,
                Union[int, str],
                bool,
                Optional[int],
                Optional[bool],
                Optional[bytes],
            ]
        ]()

        _sendPacketNow = mesh_interface._sendPacket

        def _run():
            while True:
                try:
                    (
                        meshPacket,
                        destinationId,
                        wantAck,
                        hopLimit,
                        pkiEncrypted,
                        publicKey,
                    ) = packet_queue.get()
                    _sendPacketNow(
                        meshPacket=meshPacket,
                        destinationId=destinationId,
                        wantAck=wantAck,
                        hopLimit=hopLimit,
                        pkiEncrypted=pkiEncrypted,
                        publicKey=publicKey,
                    )
                    packet_queue.task_done()
                    sleep(delay_secs)
                except Empty:
                    pass
            sleep(0.1)

        _thread: Thread = Thread(target=_run, daemon=True)
        _thread.start()
        self.join = _thread.join

        def _sendPacketLater(
            meshPacket: MeshPacket,
            destinationId: Union[int, str] = BROADCAST_ADDR,
            wantAck: bool = False,
            hopLimit: Optional[int] = None,
            pkiEncrypted: Optional[bool] = False,
            publicKey: Optional[bytes] = None,
        ) -> MeshPacket:
            packet_queue.put(
                (meshPacket, destinationId, wantAck, hopLimit, pkiEncrypted, publicKey)
            )

        mesh_interface._sendPacket = _sendPacketLater
        self.mesh_interface = mesh_interface
