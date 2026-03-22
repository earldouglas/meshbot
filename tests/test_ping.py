from meshbot import Meshbot
from stub_mesh_interface import StubMeshInterface


def test_ping():

    meshbot = Meshbot(qth=None)
    meshbot.start()

    mesh_interface = StubMeshInterface()

    try:
        rx = mesh_interface.sendAndReceive("Ping")

        assert rx is not None

        observed = rx.decoded.payload
        expected = b"Pong"

        assert observed == expected

    finally:
        mesh_interface.close()
