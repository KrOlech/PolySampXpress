import os
import sys

from src.BaseClass.Logger.Logger import Loger


class AbstractStandaManipulator(Loger):

    # Specifies the current directory.
    cur_dir = os.path.abspath(os.path.dirname(__file__))

    # Formation of the directory name with all dependencies.
    ximc_dir = os.path.join(cur_dir, "..", "..", "..", "ximc")

    # Formation of the directory name with python dependencies.
    ximc_package_dir = os.path.join(ximc_dir, "crossplatform", "wrappers", "python")

    # add pyximc.py wrapper to python path
    sys.path.append(ximc_package_dir)

    user_name = "root"
    key_esc = "esc"

    @property
    def ok(self):
        return 0

    @property
    def error(self):
        return -1

    @property
    def not_implemented(self):
        return -2

    @property
    def value_error(self):
        return -3

    @property
    def no_device(self):
        return -4
