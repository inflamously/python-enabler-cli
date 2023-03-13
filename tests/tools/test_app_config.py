from python_enabler.tools.app_config import AppConfig


def test_appconfig_init() -> None:
    config = AppConfig()
    assert config["app"]
    assert config["app"]["version"] == "1.0"
    assert config["app.version"] == "1.0"