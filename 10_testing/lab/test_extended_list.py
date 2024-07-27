from lab.extended_list import IntegerList

from unittest import TestCase, main


class TestIntegerList(TestCase):
    def setUp(self):
        self.list = IntegerList(8, -1, 12, 3)

    def test_init(self):
        lst = IntegerList()
        self.assertEqual([], lst._IntegerList__data)

        lst = IntegerList(18, 8, 'kks', [1, 0])
        self.assertEqual([18, 8], lst._IntegerList__data)

    def test_get_data(self):
        result = self.list.get_data()
        self.assertEqual(self.list._IntegerList__data, result)
        self.assertEqual(id(self.list._IntegerList__data), id(result))

    def test_add_non_int_value_raises(self):
        self.assertNotIn('ssk0', self.list._IntegerList__data)
        with self.assertRaises(ValueError) as ex:
            self.list.add('ssk0')

        self.assertEqual('Element is not Integer', str(ex.exception))
        self.assertNotIn('ssk0', self.list._IntegerList__data)

    def test_add_int_app_at_the_end(self):
        self.assertEqual([8, -1, 12, 3], self.list._IntegerList__data)

        result = self.list.add(-5)

        self.assertIn(-5, self.list._IntegerList__data)

        self.assertEqual([8, -1, 12, 3, -5], result)

    def test_remove_index_is_equal_or_greater_than_length_raises(self):
        index_to_remove = len(self.list.get_data())
        self.assertEqual([8, -1, 12, 3], self.list._IntegerList__data)

        with self.assertRaises(IndexError) as ex:
            self.list.remove_index(index_to_remove)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual([8, -1, 12, 3], self.list._IntegerList__data)

        # Index is greater than the length
        index_to_remove = len(self.list.get_data()) + 1
        self.assertEqual([8, -1, 12, 3], self.list._IntegerList__data)

        with self.assertRaises(IndexError) as ex:
            self.list.remove_index(index_to_remove)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual([8, -1, 12, 3], self.list._IntegerList__data)

    def test_remove_by_index_removes_element(self):
        self.assertIn(12, self.list._IntegerList__data)

        result = self.list.remove_index(2)

        self.assertNotIn(12, self.list._IntegerList__data)
        self.assertEqual(12, result)

    def test_get_index_is_equal_or_greater_than_length_raises(self):
        index_to_get = len(self.list.get_data())
        self.assertEqual([8, -1, 12, 3], self.list._IntegerList__data)

        with self.assertRaises(IndexError) as ex:
            self.list.get(index_to_get)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual([8, -1, 12, 3], self.list._IntegerList__data)

        # Index is greater than the length
        index_to_get = len(self.list.get_data()) + 1
        self.assertEqual([8, -1, 12, 3], self.list._IntegerList__data)

        with self.assertRaises(IndexError) as ex:
            self.list.get(index_to_get)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual([8, -1, 12, 3], self.list._IntegerList__data)

    def test_get_index(self):
        self.assertEqual([8, -1, 12, 3], self.list._IntegerList__data)
        self.assertIn(12, self.list._IntegerList__data)

        index_to_get = 2
        result = self.list.get(index_to_get)

        self.assertIn(12, self.list._IntegerList__data)
        self.assertEqual(12, result)
        self.assertEqual([8, -1, 12, 3], self.list._IntegerList__data)

    def test_insert_index_is_equal_or_greater_than_length_raises(self):
        index = len(self.list.get_data())
        element_to_insert = 33
        self.assertEqual([8, -1, 12, 3], self.list._IntegerList__data)

        with self.assertRaises(IndexError) as ex:
            self.list.insert(index, element_to_insert)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual([8, -1, 12, 3], self.list._IntegerList__data)

        # Index is greater than the length
        index = len(self.list.get_data()) + 1
        self.assertEqual([8, -1, 12, 3], self.list._IntegerList__data)

        with self.assertRaises(IndexError) as ex:
            self.list.insert(index, element_to_insert)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual([8, -1, 12, 3], self.list._IntegerList__data)

    def test_insert_correct_index_wrong_type_raises(self):
        index = 1
        element_to_insert = 'wrong'
        self.assertEqual([8, -1, 12, 3], self.list._IntegerList__data)

        with self.assertRaises(ValueError) as ex:
            self.list.insert(index, element_to_insert)

        self.assertEqual("Element is not Integer", str(ex.exception))
        self.assertEqual([8, -1, 12, 3], self.list._IntegerList__data)

    def test_insert_correct_index_and_type(self):
        self.assertEqual([8, -1, 12, 3], self.list._IntegerList__data)

        index = 2
        element_to_insert = -27
        result = self.list.insert(index, element_to_insert)

        self.assertIsNone(result)
        self.assertEqual([8, -1, -27, 12, 3], self.list._IntegerList__data)

    def test_get_biggest(self):
        self.assertEqual([8, -1, 12, 3], self.list._IntegerList__data)

        result = self.list.get_biggest()

        self.assertEqual(12, result)
        self.assertEqual([8, -1, 12, 3], self.list._IntegerList__data)

    def test_get_element_index(self):
        self.assertEqual([8, -1, 12, 3], self.list._IntegerList__data)

        result = self.list.get_index(3)
        self.assertEqual(3, result)


if __name__ == '__main__':
    main()
