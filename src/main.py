#!/usr/bin/env python3

from meshtastic.serial_interface import SerialInterface
from os import getenv
from throttle import Throttle
from meshbot import Meshbot


def main() -> None:
    qth = getenv("QTH")

    throttle = Throttle(SerialInterface(), 10)
    meshbot = Meshbot(qth=qth)
    meshbot.start()
    throttle.join()
    throttle.mesh_interface.close()


if __name__ == "__main__":
    main()
