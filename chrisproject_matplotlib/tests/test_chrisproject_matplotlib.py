
from unittest import TestCase
from unittest import mock
from chrisproject_matplotlib.chrisproject_matplotlib import ChrisprojectMatplotlib


class ChrisprojectMatplotlibTests(TestCase):
    """
    Test ChrisprojectMatplotlib.
    """
    def setUp(self):
        self.app = ChrisprojectMatplotlib()

    def test_run(self):
        """
        Test the run code.
        """
        args = []
        if self.app.TYPE == 'ds':
            args.append('inputdir') # you may want to change this inputdir mock
        args.append('outputdir')  # you may want to change this outputdir mock

        # you may want to add more of your custom defined optional arguments to test
        # your app with
        # eg.
        # args.append('--custom-int')
        # args.append(10)

        options = self.app.parse_args(args)
        self.app.run(options)

        # write your own assertions
        self.assertEqual(options.outputdir, 'outputdir')
