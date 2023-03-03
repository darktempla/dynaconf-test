from unittest import TestCase

from dynaconf_test.main import main
from dynaconf_test.config import settings


class TestMain(TestCase):
    def test_main(self):
        settings.setenv('test')
        main()
