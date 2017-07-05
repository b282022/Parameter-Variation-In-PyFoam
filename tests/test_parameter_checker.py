from src import parameter_checker
import unittest


class TestParameterChecker(unittest.TestCase):
    def setUp(self):
        self.nested_dictionary_list = [];
        dictionary_fvSolution = {
            'solvers': {'p': {'relTol': 0.05, 'preconditioner': 'DIC', 'tolerance': 4e-05, 'solver': 'PCG'},
                        'U': {'relTol': 0, 'smoother': 'symGaussSeidel', 'tolerance': 1e-05, 'solver': 'smoothSolver'},
                        'pFinal': {'relTol': 0, '$p': ''}
                        },
            'PISO': {'pRefValue': 0, 'nCorrectors': 2, 'nNonOrthogonalCorrectors': 0, 'pRefCell': 0}
        }
        dictionary_fvSchemes = {
            'ddtSchemes': {'default': 'Euler'},
            'gradSchemes': {'default': ['Gauss', 'linear'], 'grad(p)': ['Gauss', 'linear']},
            'divSchemes': {'default': 'none', 'div(phi,U)': ['Gauss', 'linear']},
            'laplacianSchemes': {'default': ['Gauss', 'linear', 'orthogonal']},
            'interpolationSchemes': {'default': 'linear'},
            'snGradSchemes': {'default': 'orthogonal'}
        }
        dictionary_controlDict = {
            'application': 'icoFoam', 'startFrom': 'startTime', 'startTime': 0, 'stopAt': 'endTime', 'endTime': 6.5,
            'deltaT': 0.005, 'writeControl': 'timeStep', 'writeInterval': 200, 'purgeWrite': 0, 'writeFormat': 'ascii',
            'writePrecision': 6, 'writeCompression': 'no', 'timeFormat': 'general', 'timePrecision': 6,
            'runTimeModifiable': 'yes'
        }
        self.nested_dictionary_list.append(dictionary_fvSolution)
        self.nested_dictionary_list.append(dictionary_controlDict)
        self.nested_dictionary_list.append(dictionary_fvSchemes)

    def test_modified_search_for_parameter(self):
        self.assertEqual(parameter_checker.modified_search_for_parameter(self.nested_dictionary_list[0],
                                                                         'solvers/p/relTol'.split('/'), 0), True)

        self.assertEqual(parameter_checker.modified_search_for_parameter(self.nested_dictionary_list[0],
                                                                         'solvers/p/preconditioner'.split('/'), 0),
                         True)

        self.assertEqual(parameter_checker.modified_search_for_parameter(self.nested_dictionary_list[0],
                                                                         'solvers/p/tolerance'.split('/'), 0), True)

        self.assertEqual(parameter_checker.modified_search_for_parameter(self.nested_dictionary_list[0],
                                                                         'solvers/p/solver'.split('/'), 0), True)

        self.assertEqual(parameter_checker.modified_search_for_parameter(self.nested_dictionary_list[0],
                                                                         'solvers/p'.split('/'), 0), False)

        self.assertEqual(parameter_checker.modified_search_for_parameter(self.nested_dictionary_list[0],
                                                                         'solvers/p/smoother'.split('/'), 0), False)

        self.assertEqual(parameter_checker.modified_search_for_parameter(self.nested_dictionary_list[0],
                                                                         'PISO/p/smoother'.split('/'), 0), False)

    def test_update_parameter_value(self):
        # Make an update dictionary
        update_dictionary = parameter_checker.ChainDict()
        update_dictionary.set_key_chain('solvers/p/relTol'.split('/'), 0)

        parameter_checker.update_parameter_value(self.nested_dictionary_list[0],
                                                 update_dictionary)

        self.assertEqual(self.nested_dictionary_list[0]['solvers']['p']['relTol'] == 0, True)

        update_dictionary = parameter_checker.ChainDict()
        update_dictionary.set_key_chain('solvers/p/tolerance'.split('/'), 1e-5)
        parameter_checker.update_parameter_value(self.nested_dictionary_list[0],
                                                 update_dictionary)

        self.assertEqual(self.nested_dictionary_list[0]['solvers']['p']['tolerance'] == 1e-5, True)

        update_dictionary = parameter_checker.ChainDict()
        update_dictionary.set_key_chain('solvers/p/preconditioner'.split('/'), 'CID')
        parameter_checker.update_parameter_value(self.nested_dictionary_list[0],
                                                 update_dictionary)

        self.assertEqual(self.nested_dictionary_list[0]['solvers']['p']['preconditioner'] == 'CID', True)

    def tearDown(self):
        del self.nested_dictionary_list


if __name__ == '__main__':
    unittest.main()
