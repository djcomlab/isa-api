import os
import unittest
from isatools import isatab2
from tests import utils


class TestIsaTab2(unittest.TestCase):

    def setUp(self):
        self._tab_data_dir = utils.TAB_DATA_DIR

    def test_isatab2_charac_param_factor(self):
        test_case = 'TEST-ISA-charac-param-factor'
        df = isatab2.read_tfile(os.path.join(self._tab_data_dir, test_case, 'a_test-template1-splitting_transcription_profiling_DNA_microarray.txt'))
        sources, samples, other_material, data, processes, process_sequences = isatab2.ProcessSequenceFactory().create_from_df(df)
        print(sources, samples, other_material, data, processes, process_sequences)
        self.assertEqual(len(sources), 0)  # expecting no sources
        self.assertEqual(len(samples), 2)  # expecting 2 samples
        self.assertEqual(len(other_material), 4)  # expecting 2 extracts, 2 labeled extracts
        self.assertEqual(len(data), 4)  # expecting 3 array data files and 1 derived array data file
        self.assertEqual(len(processes), 11)  # expecting 11 processes
        # self.assertEqual(len(process_sequences), 3)  # expecting 3 process sequences

    def test_isatab2_bii_s_7(self):
        test_case = 'BII-S-7'
        df = isatab2.read_tfile(os.path.join(self._tab_data_dir, test_case, 's_BII-S-7.txt'))
        sources, samples, other_material, data, processes, process_sequences = isatab2.ProcessSequenceFactory().create_from_df(df)
        print(sources, samples, other_material, data, processes, process_sequences)
        self.assertEqual(len(sources), 29)  # expecting 29 sources
        self.assertEqual(len(samples), 29)  # expecting 29 samples
        self.assertEqual(len(other_material), 0)  # expecting no other materials
        self.assertEqual(len(data), 0)  # expecting no raw data files
        self.assertEqual(len(processes), 29)  # expecting 29 processes
        # self.assertEqual(len(process_sequences), 29)  # expecting 29 process sequences
        #  TODO: Fix processes and sequences to combine repeated parts to build graph properly.

    def test_isatab2_bii_s_3_Gx(self):
        test_case = 'BII-S-3'
        df = isatab2.read_tfile(os.path.join(self._tab_data_dir, test_case, 'a_gilbert-assay-Gx.txt'))
        sources, samples, other_material, data, processes, process_sequences = isatab2.ProcessSequenceFactory().create_from_df(df)
        print(sources, samples, other_material, data, processes, process_sequences)
        self.assertEqual(len(sources), 0)  # expecting no sources
        self.assertEqual(len(samples), 4)  # expecting 4 samples
        self.assertEqual(len(other_material), 4)  # expecting 4 extracts
        self.assertEqual(len(data), 6)  # expecting 6 raw data files
        self.assertEqual(len(processes), 18)  # expecting 18 processes
        # self.assertEqual(len(process_sequences), 6)  # expecting 6 process sequences
        #  TODO: Fix processes and sequences to combine repeated parts to build graph properly