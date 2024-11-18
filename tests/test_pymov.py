import pytest
from unittest.mock import MagicMock
from unittest.mock import patch
import serial
from pymov.pymov import Valves


@patch("serial.Serial")
def test_init(mock_serial):
    mock_serial_instance = MagicMock()
    mock_serial.return_value = mock_serial_instance

    valves = Valves()
    
    # Check initial attributes
    assert valves.valves_available == ["1", "2", "3", "4"]
    assert valves.valve_status == ["0", "0", "0", "0", "0"]
    assert valves.port == "/dev/tty.usbmodem12201"
    assert valves.baudrate == 9600

    # Ensure serial.Serial was called with expected parameters
    mock_serial.assert_called_once_with(
        "/dev/tty.usbmodem12201",
        9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=0,
        xonxoff=False,
    )

@patch("serial.Serial")
def test_open_valve(mock_serial):
    mock_serial_instance = MagicMock()
    mock_serial.return_value = mock_serial_instance

    valves = Valves()
    valves.open_valve("12")

    # Check valve status
    assert valves.valve_status == ["1", "1", "0", "0", "0"]

    # Ensure correct command sent to serial
    mock_serial_instance.write.assert_called_once_with(b"11000")


@patch("serial.Serial")
def test_close_valve(mock_serial):
    mock_serial_instance = MagicMock()
    mock_serial.return_value = mock_serial_instance

    valves = Valves()
    valves.open_valve("1234")  # Open all valves
    valves.close_valve("24")  # Close valves 2 and 4

    # Check valve status
    assert valves.valve_status == ["1", "0", "1", "0", "0"]

    # Ensure correct command sent to serial
    assert mock_serial_instance.write.call_count == 2
    mock_serial_instance.write.assert_called_with(b"10100")


@patch("serial.Serial")
def test_stop(mock_serial):
    mock_serial_instance = MagicMock()
    mock_serial.return_value = mock_serial_instance

    valves = Valves()
    valves.open_valve("1234")  # Open all valves
    valves.stop()  # Stop (close all valves)

    # Check valve status
    assert valves.valve_status == ["0", "0", "0", "0", "0"]

    # Ensure correct command sent to serial
    assert mock_serial_instance.write.call_count == 2
    mock_serial_instance.write.assert_called_with(b"00000")