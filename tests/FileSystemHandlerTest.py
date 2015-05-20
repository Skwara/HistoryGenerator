import unittest
import shutil
import os
import filecmp
from classes.FileSystemHandler import FileSystemHandler, FileSystemHandlerException


class FileSystemHandlerTestCase(unittest.TestCase):
    def tearDown(self):
        os.remove("file1.py")
        shutil.rmtree("history")

    def test_add_to_history(self):
        shutil.copyfile("samples/sample_1.py", "file1.py")
        self.file_system_handler = FileSystemHandler.add_to_history("file1.py")
        shutil.copyfile("samples/sample_2.py", "file1.py")
        self.file_system_handler = FileSystemHandler.add_to_history("file1.py")

        self.assertRaises(FileSystemHandlerException, FileSystemHandler.add_to_history, "file1.py")

        self.assertTrue(os.path.isdir("history/file1.py"))
        self.assertTrue(os.path.isfile("history/file1.py/1"))
        self.assertTrue(os.path.isfile("history/file1.py/2"))
        self.assertTrue(filecmp.cmp("samples/sample_1.py", "history/file1.py/1"))
        self.assertTrue(filecmp.cmp("samples/sample_2.py", "history/file1.py/2"))

    def test_read_revision_content(self):
        shutil.copyfile("samples/sample_1.py", "file1.py")
        self.file_system_handler = FileSystemHandler.add_to_history("file1.py")
        revision_content = FileSystemHandler.read_revision_content("file1.py", 1)

        self.assertTrue(revision_content)
        self.assertEqual(len(revision_content), 25)


if __name__ == '__main__':
    unittest.main()
