import subprocess

def test_main():
    result = subprocess.run(("./main_program_under_test",))
    assert result.returncode == 0