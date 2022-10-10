import unittest
from elevator import Elevator
from elevator import Passenger
from elevator import elevator_move

class TestElevator(unittest.TestCase):
    def test_elevator(self):
        elevator_move(passenger.passenger_position, passenger.passenger_needed_floor)
        self.assertEqual(elevator.elevator_position, passenger.passenger_needed_floor)
    def setUp(self):
        elevator = Elevator(16,300)
        passenger = Passenger(60,1,12)
if __name__ == '__main__':
    unittest.main()
