from pathlib import Path

import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = PROJECT_ROOT / "config"


def load_config(profile="small"):
    config_path = CONFIG_DIR / f"{profile}.yaml"

    if not config_path.exists():
        raise FileNotFoundError(
            f"Configuration file not found: {config_path}"
        )

    with config_path.open("r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    return config


if __name__ == "__main__":
    config = load_config("small")

    print("Environment:", config["environment"])
    print("Sites:", config["business"]["sites"])
    print("Products:", config["business"]["products"])
    print("Sales rows:", config["data_volumes"]["sales_rows"])
    print("Start date:", config["date_range"]["start_date"])