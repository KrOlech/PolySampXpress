from Python.BaseClass.JsonRead.JsonRead import JsonHandling

import unittest
from unittest.mock import patch, mock_open, MagicMock

class TestJsonRead(unittest.TestCase):

    @patch("Python.BaseClass.JsonRead.JsonRead.JsonHandling.getFileLocation")
    @patch("builtins.open", new_callable=mock_open, read_data='{"Label": {"scalle": {"X": 1.0, "Y": 2.0}}}')
    def test_readRoiLabelScalles(self, mock_open, mock_getFileLocation):
        mock_getFileLocation.return_value = "dummy_path"
        x, y = JsonHandling.readRoiLabelScalles()
        self.assertEqual(x, 1.0)
        self.assertEqual(y, 2.0)

    @patch("Python.BaseClass.JsonRead.JsonRead.JsonHandling.getFileLocation")
    @patch("builtins.open", new_callable=mock_open, read_data='{"borders": {"x": {"min": 0, "max": 10}, "y": {"min": 5, "max": 15}}}')
    def test_readManipulatorMin(self, mock_open, mock_getFileLocation):
        mock_getFileLocation.return_value = "dummy_path"
        x_min, y_min = JsonHandling.readManipulatorMin()
        self.assertEqual(x_min, 0)
        self.assertEqual(y_min, 5)

    @patch("Python.BaseClass.JsonRead.JsonRead.JsonHandling.getFileLocation")
    @patch("builtins.open", new_callable=mock_open, read_data='{"borders": {"x": {"min": 0, "max": 10}, "y": {"min": 5, "max": 15}}}')
    def test_readManipulatorMax(self, mock_open, mock_getFileLocation):
        mock_getFileLocation.return_value = "dummy_path"
        x_max, y_max = JsonHandling.readManipulatorMax()
        self.assertEqual(x_max, 10)
        self.assertEqual(y_max, 15)

    @patch("Python.BaseClass.JsonRead.JsonRead.JsonHandling.getFileLocation")
    @patch("builtins.open", new_callable=mock_open, read_data='{"x": 10, "y": 20}')
    def test_readManipulatorPosition(self, mock_open, mock_getFileLocation):
        mock_getFileLocation.return_value = "dummy_path"
        x, y = JsonHandling.readManipulatorPosition()
        self.assertEqual(x, 10)
        self.assertEqual(y, 20)

    @patch("Python.BaseClass.JsonRead.JsonRead.JsonHandling.getFileLocation")
    @patch("builtins.open", new_callable=mock_open)
    def test_saveManipulatorPosition(self, mock_open, mock_getFileLocation):
        mock_getFileLocation.return_value = "dummy_path"
        with patch("json.dump") as mock_json_dump:
            JsonHandling.saveManipulatorPosition({"x": 30, "y": 40})
            mock_json_dump.assert_called_once()
            saved_data = mock_json_dump.call_args[0][0]
            self.assertEqual(saved_data, {"x": 30, "y": 40})

    @patch("Python.BaseClass.JsonRead.JsonRead.JsonHandling.getFileLocation")
    @patch("builtins.open", new_callable=mock_open, read_data='{"1080P": {"xResolution": "1920","yResolution": "1080","FPS": "40"}}')
    def test_loadResolution(self, mock_open, mock_getFileLocation):
        mock_getFileLocation.return_value = "dummy_path"
        x, y, fps = JsonHandling.loadResolution("1080P")
        self.assertEqual(x, 1920)
        self.assertEqual(y, 1080)
        self.assertEqual(fps, 40)

    @patch("Python.BaseClass.JsonRead.JsonRead.JsonHandling.getFileLocation")
    @patch("builtins.open", new_callable=mock_open, read_data='{"0": {"offsets": {"x": 0.1, "y": 0.2}}}')
    def test_loadOffsetsJson(self, mock_open, mock_getFileLocation):
        mock_getFileLocation.return_value = "dummy_path"
        x_offset, y_offset = JsonHandling.loadOffsetsJson()
        self.assertEqual(x_offset, 0.1)
        self.assertEqual(y_offset, 0.2)

if __name__ == "__main__":
    unittest.main()

