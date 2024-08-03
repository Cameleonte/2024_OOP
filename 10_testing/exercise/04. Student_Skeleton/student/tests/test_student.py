from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student1 = Student('PIP', {'Algebra': ['Excellent', '3 weeks']})
        self.student2 = Student('Pinko')

    def test_init_courses_is_none(self):
        self.assertEqual('Pinko', self.student2.name)
        self.assertEqual({}, self.student2.courses)

    def test_init_courses_is_not_none(self):

        self.assertEqual('PIP', self.student1.name)
        self.assertEqual({'Algebra': ['Excellent', '3 weeks']}, self.student1.courses)

    def test_enroll_existing_course_in_dict_and_update_notes_returns_message(self):
        result = self.student1.enroll("Algebra", ['n1', 'n2'], "Y")
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({'Algebra': ['Excellent', '3 weeks', 'n1', 'n2']}, self.student1.courses)

        result = self.student1.enroll("Algebra", ['n3', 'n4'], "N")
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({'Algebra': ['Excellent', '3 weeks', 'n1', 'n2', 'n3', 'n4']}, self.student1.courses)

    def test_enroll_non_existing_course_and_update_notes_with_y(self):
        result = self.student1.enroll("Python", ['1', '2'], "Y")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertTrue('Python', self.student1.courses)
        self.assertEqual(['1', '2'], self.student1.courses['Python'])

    def test_enroll_non_existing_course_and_update_notes_with_empty_string(self):
        result = self.student1.enroll("Python", ['1', '2'], "")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertTrue('Python', self.student1.courses)
        self.assertEqual(['1', '2'], self.student1.courses['Python'])

    def test_enroll_in_not_existing_course_without_adding_notes(self):
        result = self.student2.enroll("Python", ['1', '2'], "N")
        self.assertEqual("Course has been added.", result)
        self.assertTrue('Python', self.student2.courses)
        self.assertEqual([], self.student2.courses['Python'])

    def test_add_notes_to_existing_course(self):
        self.student2.enroll('Python', ['n1', 'n2'])
        result = self.student2.add_notes('Python', 'n3')

        self.assertEqual("Notes have been updated", result)
        self.assertEqual(['n1', 'n2', 'n3'], self.student2.courses['Python'])

    def test_add_notes_to_not_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student2.add_notes('C#', ['n1', 'n2'])

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_existing_course(self):
        result = self.student1.leave_course('Algebra')
        self.assertEqual("Course has been removed", result)
        self.assertNotIn('Algebra', self.student1.courses)

    def test_leave_non_existing_course_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student1.leave_course('C#')

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == '__main__':
    main()
