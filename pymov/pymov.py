from time import sleep
from typing import List, Optional

import serial


class Valves:
    def __init__(
        self,
        port: str = "/dev/tty.usbmodem12201",
        baudrate: int = 9600,
        valves_available: Optional[List[str]] = None,
        valve_status: Optional[List[str]] = None,
    ) -> None:
        """
        Initialize the Valves class.

        Args:
            port (str): The serial port to connect to.
            baudrate (int): The baud rate for serial communication.
            valves_available (Optional[List[str]]): List of available valves.
            valve_status (Optional[List[str]]): Initial status of each valve.
        """
        self.valves_available = valves_available or ["1", "2", "3", "4"]
        self.valve_status = valve_status or ["0", "0", "0", "0", "0"]
        self.port = port
        self.baudrate = baudrate
        self.ser = serial.Serial(
            self.port,
            self.baudrate,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=0,
            xonxoff=False,
        )
        sleep(5)

    def open_valve(self, mod_valve: str) -> None:
        """
        Open the specified valve(s).

        Args:
            mod_valve (str): Valve(s) to open.
        """
        sleep(5)
        for valve in mod_valve:
            if valve not in self.valves_available:
                print("Valve not Available")
            else:
                self.valve_status[int(valve) - 1] = "1"
        valve_status_str = "".join(self.valve_status)
        self.ser.write(valve_status_str.encode(encoding="ascii", errors="strict"))

    def close_valve(self, mod_valve: str) -> None:
        """
        Close the specified valve(s).

        Args:
            mod_valve (str): Valve(s) to close.
        """
        sleep(5)
        for valve in mod_valve:
            if valve not in self.valves_available:
                print("Valve not Available")
            else:
                self.valve_status[int(valve) - 1] = "0"
        valve_status_str = "".join(self.valve_status)
        self.ser.write(valve_status_str.encode(encoding="ascii", errors="strict"))

    def stop(self) -> None:
        """
        Close all valves.
        """
        self.close_valve("1234")


if __name__ == "__main__":
    valve = Valves()
    valve.open_valve("1234")
    valve.close_valve("23")
    valve.open_valve("3")
    valve.stop()
