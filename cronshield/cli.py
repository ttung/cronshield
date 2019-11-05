# -*- coding: utf-8 -*-

"""Console script for cronshield."""
import subprocess
import sys

import click


@click.command()
@click.argument("command", nargs=-1, required=True, type=str)
def main(command):
    """Console script for cronshield."""
    process = subprocess.run(args=command, capture_output=True)

    if process.returncode == 0:
        sys.exit(0)

    command_text = " ".join(command)

    print(f"cronshield detected failure or error output for the command: {command_text}")
    print(f"")
    print(f"RESULT CODE: {process.returncode}")
    if len(process.stdout) > 0:
        print(f"")
        print(f"OUTPUT:")
        print(f"{process.stdout.decode('latin-1')}")
    if len(process.stderr) > 0:
        print(f"")
        print(f"ERROR:")
        print(f"{process.stderr.decode('latin-1')}")

    sys.exit(process.returncode)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
