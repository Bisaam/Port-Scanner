# Port Scanner

A simple TCP port scanner written in Python using only the standard library.

It takes a hostname or IP address, resolves it to an IPv4 address, and attempts a
TCP connection to every port from 0 to 65534. Any port that accepts the connection
is reported as open.

## Requirements

- Python 3 (no external dependencies)

## Usage

```bash
python3 scanner.py <target>
```

The target can be an IP address or a hostname:

```bash
python3 scanner.py 192.168.10.1
python3 scanner.py example.com
```

Example output:

```
Port 22 is open
Port 80 is open
Port 443 is open
```

Press `Ctrl+C` at any time to stop the scan.

## How it works

For each port, the script opens an `AF_INET` / `SOCK_STREAM` socket and calls
`connect_ex()` with a 1 second timeout. A return value of `0` means the handshake
succeeded, so the port is open; anything else is treated as closed or filtered and
the socket is closed.

The scan is single-threaded and sequential, so a full 65k sweep takes a while —
it is best pointed at a single host on a local network rather than used as a
general purpose scanner.

## Use cases

- Checking which services are exposed on a machine you own
- Verifying that a firewall rule or port forward is actually in effect
- Confirming a service came up on the port you expect after a deploy
- Learning how TCP connect scanning works under the hood

## Disclaimer

Only scan hosts you own or have explicit permission to test. Port scanning systems
without authorization is illegal in many jurisdictions.
