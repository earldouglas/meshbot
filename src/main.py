#!/usr/bin/env python3

import meshbot
from meshtastic.serial_interface import SerialInterface
from time import sleep


def main() -> None:

    mesh_interface = SerialInterface()

    meshbot.start()

    while True:
        sleep(1)

    mesh_interface.close()


if __name__ == "__main__":
    main()
