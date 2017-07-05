from src import latex_append
import unittest


class TestLatexAppend(unittest.TestCase):
    """
    Tester class for latex_append.py
    """

    def setUp(self):
        self.correct_generated_answer_latex = open('answer_latex.tex', 'w')
        self.incorrect_generated_answer_latex = open('incorrect_answer_latex.tex', 'w')

        latex_append.write_header(self.correct_generated_answer_latex, 'answer_latex.tex')
        latex_append.write_header(self.incorrect_generated_answer_latex, 'incorrect_answer_latex.tex')

        self.correct_generated_answer_latex.close()
        self.incorrect_generated_answer_latex.close()

    def test_correct_file_generated(self):
        """
        Testing method for latex_append.py methods
        Generate two dummy latex files using helper functions of latex_append.py
        Manually already made correct_answer_latex.tex for checking both files against it
        :return: Nothing
        """
        self.correct_generated_answer_latex = open('answer_latex.tex', 'a')
        self.incorrect_generated_answer_latex = open('incorrect_answer_latex.tex', 'a')

        latex_append.append_plot(self.correct_generated_answer_latex, 'AtParameterValue1e-05')
        self.correct_generated_answer_latex = open('answer_latex.tex', 'a')
        latex_append.append_plot(self.correct_generated_answer_latex, 'AtParameterValue2e-05')
        self.correct_generated_answer_latex = open('answer_latex.tex', 'a')
        latex_append.append_plot(self.correct_generated_answer_latex, 'AtParameterValue3e-05')
        self.correct_generated_answer_latex = open('answer_latex.tex', 'a')
        latex_append.append_plot(self.correct_generated_answer_latex, 'AtParameterValue4e-05')
        self.correct_generated_answer_latex = open('answer_latex.tex', 'a')
        latex_append.append_plot(self.correct_generated_answer_latex, 'AtParameterValue5e-05')
        self.correct_generated_answer_latex = open('answer_latex.tex', 'a')
        latex_append.append_plot(self.correct_generated_answer_latex, 'AtParameterValue6e-05')
        self.correct_generated_answer_latex = open('answer_latex.tex', 'a')
        latex_append.append_plot(self.correct_generated_answer_latex, 'AtParameterValue7e-05')
        self.correct_generated_answer_latex = open('answer_latex.tex', 'a')
        latex_append.append_plot(self.correct_generated_answer_latex, 'AtParameterValue8e-05')
        self.correct_generated_answer_latex = open('answer_latex.tex', 'a')
        latex_append.append_plot(self.correct_generated_answer_latex, 'AtParameterValue9e-05')
        self.correct_generated_answer_latex = open('answer_latex.tex', 'a')
        latex_append.append_plot(self.correct_generated_answer_latex, 'AtParameterValue0.0001')
        self.correct_generated_answer_latex = open('answer_latex.tex', 'a')

        latex_append.write_footer(self.correct_generated_answer_latex)

        latex_append.append_plot(self.incorrect_generated_answer_latex, 'AtParameterValue1e-5')
        self.incorrect_generated_answer_latex = open('incorrect_answer_latex.tex', 'a')
        latex_append.append_plot(self.incorrect_generated_answer_latex, 'AtParameterValue2e-5')
        self.incorrect_generated_answer_latex = open('incorrect_answer_latex.tex', 'a')
        latex_append.append_plot(self.incorrect_generated_answer_latex, 'AtParameterValue3e-5')
        self.incorrect_generated_answer_latex = open('incorrect_answer_latex.tex', 'a')
        latex_append.append_plot(self.incorrect_generated_answer_latex, 'AtParameterValue4e-5')
        self.incorrect_generated_answer_latex = open('incorrect_answer_latex.tex', 'a')
        latex_append.append_plot(self.incorrect_generated_answer_latex, 'AtParameterValue5e-5')
        self.incorrect_generated_answer_latex = open('incorrect_answer_latex.tex', 'a')
        latex_append.append_plot(self.incorrect_generated_answer_latex, 'AtParameterValue6e-5')
        self.incorrect_generated_answer_latex = open('incorrect_answer_latex.tex', 'a')
        latex_append.append_plot(self.incorrect_generated_answer_latex, 'AtParameterValue7e-5')
        self.incorrect_generated_answer_latex = open('incorrect_answer_latex.tex', 'a')
        latex_append.append_plot(self.incorrect_generated_answer_latex, 'AtParameterValue8e-5')
        self.incorrect_generated_answer_latex = open('incorrect_answer_latex.tex', 'a')
        latex_append.append_plot(self.incorrect_generated_answer_latex, 'AtParameterValue9e-5')
        self.incorrect_generated_answer_latex = open('incorrect_answer_latex.tex', 'a')
        latex_append.append_plot(self.incorrect_generated_answer_latex, 'AtParameterValue1e-4')
        self.incorrect_generated_answer_latex = open('incorrect_answer_latex.tex', 'a')

        latex_append.write_footer(self.incorrect_generated_answer_latex)
        self.incorrect_generated_answer_latex.close()

        self.correct_generated_answer_latex = open('answer_latex.tex', 'r')
        self.incorrect_generated_answer_latex = open('incorrect_answer_latex.tex', 'r')
        answer_latex = open('tests/correct_answer_latex.tex', 'r')

        self.assertEqual(self.correct_generated_answer_latex.readlines(), answer_latex.readlines())
        answer_latex = open('tests/correct_answer_latex.tex', 'r')
        self.assertNotEqual(self.incorrect_generated_answer_latex.readlines(), answer_latex.readlines())

        self.correct_generated_answer_latex.close()
        self.incorrect_generated_answer_latex.close()
        answer_latex.close()

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
