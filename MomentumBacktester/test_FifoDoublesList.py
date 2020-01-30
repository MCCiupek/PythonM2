from unittest import TestCase
from FifoDoublesList import FifoDoublesList


class TestFifoDoublesList(TestCase):
    def test_return_values(self):
        tested_instance = FifoDoublesList(6)
        # Fill instance
        tested_instance.put(1)
        tested_instance.put(2)
        tested_instance.put(3)
        tested_instance.put(1)
        tested_instance.put(1)
        tested_instance.put(1)

        # Test with Assert
        self.assertEqual(6, tested_instance.size)
        self.assertEqual([1, 2, 3, 1, 1, 1], tested_instance.return_values)

        # move on case up
        tested_instance.put(7)
        self.assertEqual([2, 3, 1, 1, 1, 7], tested_instance.return_values)

        # self.fail()
