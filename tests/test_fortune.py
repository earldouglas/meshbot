from stub_mesh_interface import StubMeshInterface
import meshbot


def test_ping():

    meshbot.start()

    mesh_interface = StubMeshInterface()

    try:
        rx = mesh_interface.sendAndReceive("Fortune")

        assert rx is not None

        observed = rx.decoded.payload

        assert len(observed) > 0
        assert len(observed) <= 200

    finally:
        mesh_interface.close()
