import sys

from PyQt5.QtCore import QEventLoop
from PyQt5.QtWidgets import QApplication

from Python.Utilitis.GenericProgressClass import GenericProgressClass

# Ensure QApplication is initialized
app = QApplication(sys.argv)

import unittest
from unittest.mock import MagicMock, patch
from Python.BackEnd.Manipulator.Abstract.DialogWindow.AbstractM import AbstractDialogMaster


class TestGenericProgressClass(unittest.TestCase):

    @patch.object(AbstractDialogMaster, 'accept', MagicMock())  # Patch accept() on AbstractDialogMaster
    @patch('Python.BackEnd.ThreadWorker.SimpleThreadWorker.SimpleFunWorker.workFunWorker')
    def setUp(self, mock_accept):
        # Mock the necessary parts of the code
        self.mock_master = MagicMock()
        self.mock_master.stop = MagicMock()
        self.mock_master.manipulatorInterferes.stop = MagicMock()

        self.mock_function = MagicMock()

        # Mock the workFunWorker function
        self.mock_work_fun_worker = MagicMock()

        # Create an instance of GenericProgressClass
        self.generic_progress = GenericProgressClass("TestWindow", self.mock_function, 300, self.mock_master)
        self.mock_accept = mock_accept  # Store the mock accept

    def test_initialization(self):
        # Test initialization of GenericProgressClass
        self.assertEqual(self.generic_progress.windowName, "TestWindow")
        self.assertEqual(self.generic_progress.function, self.mock_function)
        self.assertEqual(self.generic_progress._windowName, "TestWindow")

    def test_window_name_setter_getter(self):
        # Test windowName setter and getter
        self.generic_progress.windowName = "NewWindow"
        self.assertEqual(self.generic_progress.windowName, "NewWindow")

    def test_function_setter_getter(self):
        # Test function setter and getter
        self.generic_progress.function = self.mock_function
        self.assertEqual(self.generic_progress.function, self.mock_function)

    @patch('Python.BackEnd.ThreadWorker.SimpleThreadWorker.SimpleFunWorker.workFunWorker')
    def test_run(self, mock_workFunWorker):
        # Test the run method
        self.generic_progress.run()
        mock_workFunWorker.assert_called_once_with(self.generic_progress, self.mock_function, self.generic_progress.end)

    @patch('Python.BackEnd.ThreadWorker.SimpleThreadWorker.SimpleFunWorker.workFunWorker')
    def test_end(self, mock_workFunWorker):
        # Set up side effect to ensure workFunWorker is called
        self.mock_function.side_effect = self.mock_work_fun_worker

        # Test the end method
        self.generic_progress.end()

        # Use QEventLoop to wait for the thread to finish
        loop = QEventLoop()
        loop.processEvents()

        # Ensure that workFunWorker was called
        mock_workFunWorker.assert_called_once()
        self.mock_accept.assert_called_once()

    def test_okPressed(self):
        # Test okPressed method (although it currently does nothing)
        self.generic_progress.okPressed()
        # No action, just testing if it doesn't raise errors
        self.assertTrue(True)

    @patch.object(AbstractDialogMaster, 'accept')
    def test_accept_called_on_cancel(self, mock_accept):
        # Test cancelPressed method for AbstractDialogMaster
        self.generic_progress.cancelPressed()
        mock_accept.assert_called_once()
        self.mock_master.stop.assert_called_once()
        self.mock_master.manipulatorInterferes.stop.assert_called_once()


if __name__ == "__main__":
    unittest.main()
