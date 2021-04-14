import argparse
import json

from tests_examples.demostore.report.functions import (
    prepare_data_for_report,
    create_feature_table_row,
)
from tests_examples.demostore.report.templates import (
    prepare_report_html_template,
)

parser = argparse.ArgumentParser()
parser.add_argument(
    "--test_report_file", required=True, help="Path to test report file in JSON format."
)
parser.add_argument(
    "--html_output",
    required=True,
    help="Path to the test report output generated in html.",
)

args = parser.parse_args()

test_report = args.test_report_file
html_output = args.html_output


class raport_generator:
    def __init__(self):
        self.features_number = 0
        self.features_passed_number = 0
        self.features_failed_number = 0
        self.features_passed_rate = 0
        self.scenarios_number = 0
        self.scenarios_passed_number = 0
        self.scenarios_failed_number = 0
        self.scenarios_passed_rate = 0

    def _count_features_passed_rate(self):
        self.features_passed_rate = round(
            self.features_passed_number / self.features_number * 100, 2
        )

    def _features_number_count(self, test_data):
        self.features_number = len(test_data)
        for feature in test_data:
            if feature["feature_status"] == "passed":
                self.features_passed_number += 1
            elif feature["feature_status"] == "failed":
                self.features_failed_number += 1
        self._count_features_passed_rate()

    def _count_scenarios_passed_rate(self):
        self.scenarios_passed_rate = round(
            self.scenarios_passed_number / self.scenarios_number * 100, 2
        )

    def _scenarios_number_count(self, test_data):
        for feature in test_data:
            self.scenarios_number += len(feature["scenarios"])
            for scenario in feature["scenarios"]:
                if scenario["status"] == "passed":
                    self.scenarios_passed_number += 1
                elif scenario["status"] == "failed":
                    self.scenarios_failed_number += 1
        self._count_scenarios_passed_rate()

    def get_test_report_data(self, test_report_path):
        with open(test_report_path) as f:
            reports = json.load(f)

        report_data = prepare_data_for_report(reports)
        self._features_number_count(report_data)
        self._scenarios_number_count(report_data)
        features_table = create_feature_table_row(report_data)
        report_html = prepare_report_html_template(
            features_table,
            self.scenarios_passed_rate,
            self.scenarios_passed_number,
            self.scenarios_number,
        )
        return report_html

    def generate_report(self):
        report_html = self.get_test_report_data(test_report)

        with open(html_output, "w") as f:
            f.write(report_html)


if __name__ == "__main__":
    generator = raport_generator()
    generator.generate_report()
