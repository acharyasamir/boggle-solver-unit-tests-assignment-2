import unittest
from boggle_solver import Boggle


class TestSuiteAlgScalabilityCases(unittest.TestCase):
    """Test suite for various grid sizes to check scalability."""

    def test_normal_case_3x3(self):
        grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        dictionary = ["abc", "abdhi", "abi", "ef", "cfi", "dea"]
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]
        expected = ["ABC", "ABDHI", "CFI", "DEA"]
        self.assertEqual(sorted(expected), sorted(solution))

    def test_4x4_grid(self):
        grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],
                ["G", "Z", "Qu", "R"], ["O", "N", "T", "A"]]
        dictionary = ["art", "ego", "gent", "get", "net", "new",
                      "newt", "prat", "pry", "qua", "quart", "quartz",
                      "rat", "tar", "tarp", "ten", "went", "wet",
                      "arty", "not", "quar"]
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]
        expected = ["ART", "EGO", "GENT", "GET", "NET", "NEW", "NEWT",
                    "PRAT", "PRY", "QUA", "QUART", "QUARTZ", "RAT",
                    "TAR", "TARP", "TEN", "WENT", "WET", "QUAR"]
        self.assertEqual(sorted(expected), sorted(solution))

    def test_7x7_grid(self):
        grid = [["H", "A", "R", "B", "O", "R", "S"],
                ["T", "R", "A", "V", "E", "L", "S"],
                ["W", "I", "N", "T", "E", "R", "S"],
                ["S", "N", "O", "W", "F", "A", "L"],
                ["B", "R", "I", "S", "K", "S", "L"],
                ["C", "O", "L", "D", "S", "E", "A"],
                ["B", "E", "A", "C", "H", "S", "S"]]
        dictionary = [
          "harbor", "travels", "winter", "snowfall",
          "brisk", "cold", "beach", "seas"
          ]
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]
        expected = ["HARBOR", "WINTER", "COLD", "BEACH"]
        self.assertEqual(sorted(expected), sorted(solution))

    def test_13x13_grid_no_words_found(self):
        """Test Boggle solver with a """
        grid = [["X", "Y"] * 6 + ["X"]] * 13
        dictionary = ["HELLO", "WORLD", "PYTHON", "UNITTEST",
                      "OPENAI", "CHATGPT", "ALGORITHM", "DATA",
                      "STRUCTURE", "FUNCTION", "VARIABLE", "CLASS"]
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]
        expected = []
        self.assertEqual(sorted(expected), sorted(solution))


class TestSuiteSimpleEdgeCases(unittest.TestCase):
    """Test suite for edge cases including empty and minimal grids."""

    def test_square_grid_1x1(self):
        grid = [["A"]]
        dictionary = ["a", "b", "c"]
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]
        expected = []
        self.assertEqual(sorted(expected), sorted(solution))

    def test_empty_grid(self):
        grid = [[]]
        dictionary = ["hello", "there", "general", "kenobi"]
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]
        expected = []
        self.assertEqual(sorted(expected), sorted(solution))

    def test_empty_dictionary(self):
        grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        dictionary = []
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]
        expected = []
        self.assertEqual(sorted(expected), sorted(solution))


class TestSuiteCompleteCoverage(unittest.TestCase):
    """Test suite for complete test coverage."""

    def test_no_words_from_dictionary(self):
        grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        dictionary = ["xyz", "mno", "pqr"]
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]
        expected = []
        self.assertEqual(sorted(expected), sorted(solution))

    def test_partial_words_from_dictionary(self):
        grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        dictionary = ["abc", "cfi", "xyz", "ghi"]
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]
        expected = ["ABC", "CFI", "GHI"]
        self.assertEqual(sorted(expected), sorted(solution))

    def test_all_words_from_dictionary(self):
        grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        dictionary = ["abc", "cfi", "beh", "def", "ghi", "adg", "aei", "ceg"]
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]
        expected = ["ABC", "CFI", "BEH", "DEF", "GHI", "ADG", "AEI", "CEG"]
        self.assertEqual(sorted(expected), sorted(solution))


class TestSuiteQuAndSt(unittest.TestCase):
    """Test suite for grids containing QU and ST as multi-letter cells."""

    def test_grid_with_multiple_multi_letter_cells(self):
        grid = [["St", "A", "R"], ["Qu", "E", "T"], ["F", "G", "H"]]
        dictionary = ["star", "start", "quest", "quiet", "rat", "hat", "set"]
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]
        expected = ["STAR", "START", "QUEST", "RAT"]
        self.assertEqual(sorted(expected), sorted(solution))

    def test_grid_with_more_complex_words(self):
        grid = [["St", "A", "R"], ["Qu", "E", "T"], ["F", "G", "H"]]
        dictionary = ["stqufgearth", "startequfgh", "star",
                      "start", "quest", "quiet", "rat", "hat", "set"]
        mygame = Boggle(grid, dictionary)
        solution = [x.upper() for x in mygame.getSolution()]
        expected = [
          "STAR", "START", "QUEST", "RAT",
          "STARTEQUFGH", "STQUFGEARTH"
        ]
        self.assertEqual(sorted(expected), sorted(solution))


if __name__ == '__main__':
    unittest.main()