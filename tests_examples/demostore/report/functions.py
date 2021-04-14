from tests_examples.demostore.report.templates import prepare_feature_table_template


def prepare_data_for_report(report_data):
    formated_data = []
    for feature in report_data:
        feature_scenarios = []
        for scenario in feature["elements"]:
            scenario_data = {
                "name": scenario["name"],
                "status": scenario["status"],
            }
            feature_scenarios.append(scenario_data)

        feature_data = {
            "feature_name": feature["name"],
            "feature_status": feature["status"],
            "scenarios": feature_scenarios,
        }
        formated_data.append(feature_data)
    return formated_data


def create_feature_table_row(formated_data):
    feature_table_rows = ""
    for feature in formated_data:
        feature_table_rows += prepare_feature_table_template(
            feature["feature_name"], feature["feature_status"], feature["scenarios"]
        )
    return feature_table_rows
