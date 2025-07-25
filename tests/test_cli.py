import pytest


# a
@pytest.fixture
def get_main_arguments():
    return type('A', (), {'command_line_script_args': None, 'main_function_kwargs': {}})


@pytest.mark.runner_setup()
def test_cli(
    get_main_arguments,
    isolated_cli_runner,
):
    from quma.cli import main

    main_arguments = get_main_arguments()
    result = isolated_cli_runner.invoke(
        main,
        args=main_arguments.command_line_script_args,
        input=None,
        env=None,
        catch_exceptions=False,
        **main_arguments.main_function_kwargs,
    )
    assert result.exit_code == 0
    assert result.stdout == ''
