
import unittest
from unittest.mock import patch, mock_open
from datetime import datetime

from Python.BaseClass.Logger.Logger import Loger


class TestLogger(unittest.TestCase):

    @patch("builtins.print")
    @patch("builtins.open", new_callable=mock_open)
    def test_logStart(self, mock_file, mock_print):
        logger = Loger()
        logger.logStart()

        mock_print.assert_called()
        log_filename = f"{datetime.now().day}-{datetime.now().year}-{datetime.now().month}.log"
        mock_file.assert_called_with(log_filename, "a")

    @patch("builtins.print")
    @patch("builtins.open", new_callable=mock_open)
    def test_logEnd(self, mock_file, mock_print):
        logger = Loger()
        logger.logEnd()

        mock_print.assert_called()
        log_filename = f"{datetime.now().day}-{datetime.now().year}-{datetime.now().month}.log"
        mock_file.assert_called_with(log_filename, "a")

    @patch("builtins.print")
    @patch("builtins.open", new_callable=mock_open)
    def test_Loggerror(self, mock_file, mock_print):
        logger = Loger()
        with patch("Python.BaseClass.Logger.Logger.stack", return_value=[unittest.mock.Mock(function="test_function")]):
            logger.logError("Test error message")

        mock_print.assert_called()
        log_filename = f"{datetime.now().day}-{datetime.now().year}-{datetime.now().month}.log"
        mock_file.assert_called_with(log_filename, "a")

    @patch("builtins.print")
    @patch("builtins.open", new_callable=mock_open)
    def test_logWarning(self, mock_file, mock_print):
        logger = Loger()
        logger.logWarning("Test warning message")

        mock_print.assert_called()
        log_filename = f"{datetime.now().day}-{datetime.now().year}-{datetime.now().month}.log"
        mock_file.assert_called_with(log_filename, "a")

    @patch("builtins.print")
    @patch("builtins.open", new_callable=mock_open)
    def test_abstractmetod(self, mock_file, mock_print):
        logger = Loger()
        logger.abstractmetod("test_method")

        mock_print.assert_called()
        log_filename = f"{datetime.now().day}-{datetime.now().year}-{datetime.now().month}.log"
        mock_file.assert_called_with(log_filename, "a")

    @patch("builtins.print")
    def test_isDebuggerActive(self, mock_print):
        with patch("sys.gettrace", return_value=True):
            self.assertTrue(Loger.isDebuggerActive())

        with patch("sys.gettrace", return_value=None):
            self.assertFalse(Loger.isDebuggerActive())


if __name__ == "__main__":
    unittest.main()
