import unittest
from classes.FileHistoryGenerator import FileHistoryGenerator


class FileHistoryGeneratorTestCase(unittest.TestCase):
    def test_module(self):
        sample_file_path = "samples/sample_1.py"
        file_history_generator = FileHistoryGenerator(sample_file_path)

        self.assertEqual(file_history_generator.file_loader.source_file_path, sample_file_path)
        self.assertEqual(file_history_generator.file_loader.content, open(sample_file_path, 'r').read())


if __name__ == '__main__':
    unittest.main()
