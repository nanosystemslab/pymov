Valves Class
============

The Valves class provides an interface for controlling a series of valves via serial communication. It allows for opening and closing individual or multiple valves sequentially.

.. class:: Valves(port="/dev/tty.usbmodem12201", baudrate=9600, valves_available=None, valve_status=None)

   Initialize the Valves class.

   :param port: The serial port to connect to.
   :type port: str
   :param baudrate: The baud rate for serial communication.
   :type baudrate: int
   :param valves_available: List of available valves. Defaults to ["1", "2", "3", "4"].
   :type valves_available: Optional[List[str]]
   :param valve_status: Initial status of each valve. Defaults to ["0", "0", "0", "0", "0"].
   :type valve_status: Optional[List[str]]

   .. method:: open_valve(mod_valve)

      Opens the specified valve(s).

      :param mod_valve: Valve(s) to open.
      :type mod_valve: str

   .. method:: close_valve(mod_valve)

      Closes the specified valve(s).

      :param mod_valve: Valve(s) to close.
      :type mod_valve: str

   .. method:: stop()

      Closes all valves.

Usage
-----

To use the Valves class:

.. code-block:: python

   from pymov import Valves

   # Initialize the Valves class
   valve = Valves()

   # Open valves 1, 2, 3, and 4
   valve.open_valve("1234")

   # Close valves 2 and 3
   valve.close_valve("23")

   # Open valve 3
   valve.open_valve("3")

   # Close all valves
   valve.stop()
