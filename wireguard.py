import json
import subprocess
from subprocess import CompletedProcess
import re
import sys

CONFIG_PATH = "/etc/wireguard/svin822.conf"
WG_INTERFACE = re.search(r'/([^/]+)\.conf$', CONFIG_PATH).group(1)  # type: ignore


def run_command(command) -> CompletedProcess:
    result = subprocess.run(command.split(), capture_output=True, text=True)

    return result


def wireguard_status() -> bool:
    command = "ip link"
    run_command(command)

    return WG_INTERFACE in run_command(command).stdout


def print_wireguard_status() -> None:
    data = {}

    if wireguard_status() is True:
        data['text'] = " "
        print(json.dumps(data))
    else:
        data['text'] = " "
        print(json.dumps(data))


def wireguard_toggle() -> None:
    data = {}

    if wireguard_status() is True:
        command = f"wg-quick down {WG_INTERFACE}"
        run_command(command)
        data['text'] = " "
        print(json.dumps(data))
    else:
        command = f"wg-quick up {WG_INTERFACE}"
        run_command(command)
        data['text'] = " "
        print(json.dumps(data))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print_wireguard_status()
    else:
        wireguard_toggle()
