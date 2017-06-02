import unittest
import os
import shutil
from isatools.convert import json2magetab
from tests import utils
import tempfile


def setUpModule():
    if not os.path.exists(utils.DATA_DIR):
        raise FileNotFoundError("Could not fine test data directory in {0}. Ensure you have cloned the ISAdatasets "
                                "repository using "
                                "git clone -b tests --single-branch git@github.com:ISA-tools/ISAdatasets {0}"
                                .format(utils.DATA_DIR))


class TestIsaJson2MageTab(unittest.TestCase):

    def setUp(self):
        self._json_data_dir = utils.JSON_DATA_DIR
        self._tab_data_dir = utils.TAB_DATA_DIR
        self._magetab_data_dir = utils.MAGETAB_DATA_DIR
        self._tmp_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self._tmp_dir)

    def test_json2magetab_convert_bii_i_1(self):
        with open(os.path.join(self._json_data_dir, 'BII-I-1', 'BII-I-1.json')) as json_fp:
            json2magetab.convert(json_fp, self._tmp_dir)
            self.assertTrue(os.path.isfile(os.path.join(self._tmp_dir, 'BII-I-1.idf.txt')))
            self.assertTrue(os.path.isfile(os.path.join(self._tmp_dir, 'BII-S-1.transcriptome.sdrf.txt')))
            self.assertTrue(os.path.isfile(os.path.join(self._tmp_dir, 'BII-S-2.microarray.sdrf.txt')))

    def test_json2magetab_convert_bii_s_3(self):
        with open(os.path.join(self._json_data_dir, 'BII-S-3', 'BII-S-3.json')) as json_fp:
            with self.assertRaises(IOError):
                json2magetab.convert(json_fp, self._tmp_dir)
                self.assertTrue(os.path.isfile(os.path.join(self._tmp_dir, 'BII-S-3.idf.txt')))
