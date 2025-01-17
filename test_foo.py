from unittest.mock import Mock, create_autospec

from foo import Foo, Bar


class TestFoo:
    def test_should_delegate_to_bar_when_run_is_called(self):
        mocked_bar = create_autospec(spec=Bar)
        foo = Foo(mocked_bar)
        foo.run()
        mocked_bar.some_method_renamed.assert_called_once_with(7)
