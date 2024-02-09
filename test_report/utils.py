import json
from pathlib import Path
from datetime import datetime


BASEDIR = Path(__file__).parent / "assets"


def parse_datetime(timestamp):
    try:
        parsed_datetime = datetime.fromisoformat(str(timestamp))
    except ValueError:
        try:
            timestamp = float(timestamp)
            parsed_datetime = datetime.fromtimestamp(timestamp)
        except ValueError:
            parsed_datetime = None

    return parsed_datetime.strftime("%Y-%m-%d %H:%M:%S") if parsed_datetime else None


def format_keys(obj):
    obj = {key.replace("_", " ").title(): value for key, value in obj.items()}
    return obj


def pytest_coverage_report():
    filename = "coverage-report.json"
    with open(BASEDIR / filename) as f:
        data = json.load(f)
        report = data["totals"]

        not_covered = round(100 - report["percent_covered"], 2)
        report["percent_not_covered"] = str(not_covered) + "%"

        covered = round(report["percent_covered"], 2)
        report["percent_covered"] = str(covered) + "%"

        grade = (
            "Excelent"
            if covered >= 90
            else "Good"
            if covered >= 80
            else "Satisfactory"
            if covered >= 70
            else "Poor"
        )
        return format_keys(report), grade


def pytest_test_report():
    filename = "pytest-report.json"
    with open(BASEDIR / filename) as f:
        data = json.load(f)
        report = data["summary"]
        created = data["created"]
        created = parse_datetime(created)
        return format_keys(report), created
