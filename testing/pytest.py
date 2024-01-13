# ========================
# Basic Structure and Usage
# ========================

# Test functions must start with "test_"
def test_example():
    assert 1 + 1 == 2

# Run pytest in the terminal
#   pytest pytest_cheatsheet.py

# ========================
# Assertions
# ========================

def test_assert_equal():
    assert 2 + 2 == 4, "Assertion failed: 2 + 2 is not equal to 4"

def test_assert_true():
    assert True, "This assertion always passes"

def test_assert_false():
    assert not False, "This assertion always passes"

# ========================
# Fixture
# ========================

import pytest

# Fixture to set up resources for tests
@pytest.fixture
def setup_teardown_example():
    # Setup code
    print("\nSetting up resources")

    # Yield allows the test to run
    yield

    # Teardown code
    print("\nTearing down resources")

# Using the fixture in a test
def test_with_fixture(setup_teardown_example):
    print("\nRunning test that uses the fixture")

# ========================
# Parameterized Testing
# ========================

# Parametrize decorator for multiple inputs
@pytest.mark.parametrize("input_val, expected_output", [(1, 2), (2, 4), (3, 6)])
def test_parametrized_example(input_val, expected_output):
    result = input_val * 2
    assert result == expected_output, f"Assertion failed: {input_val} * 2 is not equal to {expected_output}"

# ========================
# Markers
# ========================

# Mark tests with custom markers
@pytest.mark.slow
def test_slow_example():
    assert 1 + 1 == 2

# Run tests with a specific marker
#   pytest -m slow pytest_cheatsheet.py

# ========================
# Skipping and xfail
# ========================

# Skip a test
@pytest.mark.skip(reason="Test is skipped for a specific reason")
def test_skip_example():
    assert False, "This test should be skipped"

# Xfail a test (expected failure)
@pytest.mark.xfail(reason="This test is expected to fail")
def test_xfail_example():
    assert False, "This test is expected to fail"

# ========================
# Command-Line Options
# ========================

# Run tests in verbose mode
#   pytest -v pytest_cheatsheet.py

# Run tests in a specific file
#   pytest test_file.py

# ========================
# Fixtures with Parameters
# ========================

# Fixtures can accept parameters
@pytest.fixture
def custom_fixture(request):
    param_value = request.param
    print(f"\nSetting up with parameter: {param_value}")
    yield param_value
    print(f"\nTearing down with parameter: {param_value}")

# Use parametrize with fixtures
@pytest.mark.parametrize("custom_fixture", [1, 2, 3], indirect=True)
def test_fixture_with_parameters(custom_fixture):
    print(f"\nRunning test with parameter: {custom_fixture}")

# ========================
# Fixture Scope
# ========================

# Fixtures can have different scopes
@pytest.fixture(scope="module")
def module_fixture():
    print("\nSetting up module-level resources")
    yield
    print("\nTearing down module-level resources")

# ========================
# Hooks
# ========================

# pytest supports various hooks for customization
def pytest_runtest_protocol(item, nextitem):
    print("\nCustom hook - Before running a test")

# ========================
# Skipping based on condition
# ========================

# Skip tests based on a condition
@pytest.mark.skipif(condition=True, reason="Condition is True, so skipping")
def test_skip_conditionally():
    assert False, "This test should be skipped based on a condition"

# ========================
# Coverage
# ========================

# Install coverage package
#   pip install pytest-cov

# Run tests with coverage report
#   pytest --cov=your_module_name pytest_cheatsheet.py

# ========================
# Plugins
# ========================

# Install plugins
#   pip install pytest-html

# Generate HTML report
#   pytest --html=report.html pytest_cheatsheet.py
