def pytest_configure(config):
    config.addinivalue_line(
        "markers", "tcid29: description for your custom mark"
    )

