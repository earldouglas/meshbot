from meshbot import Meshbot
from stub_mesh_interface import StubMeshInterface
from throttle import Throttle


def test_throttle():

    meshbot = Meshbot(qth=None)
    meshbot.start()

    throttle = Throttle(StubMeshInterface(), 0.1)

    try:
        rx1 = throttle.mesh_interface.sendAndReceive("Ping", 0.05)
        rx2 = throttle.mesh_interface.sendAndReceive("Ping", 0.05)
        rx3 = throttle.mesh_interface.sendAndReceive("Ping", 0.05)

        assert rx2 is None
        assert rx3 is not None

        observed = rx3.decoded.payload
        expected = b"Pong"

        assert observed == expected

    finally:
        throttle.mesh_interface.close()
