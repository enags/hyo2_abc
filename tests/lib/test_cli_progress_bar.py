import time
import unittest

from hyo2.abc.lib.progress.cli_progress import CliProgress


class TestABCLibCliProgress(unittest.TestCase):

    def test_run(self):
        progress = CliProgress()

        progress.start(title='Test Bar', text='Doing stuff', min_value=100, max_value=300, init_value=100)

        time.sleep(.1)

        progress.update(value=150, text='Updating')

        time.sleep(.1)

        progress.add(quantum=50, text='Updating')

        time.sleep(.1)

        self.assertFalse(progress.canceled)

        progress.end()


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestABCLibCliProgress))
    return s
