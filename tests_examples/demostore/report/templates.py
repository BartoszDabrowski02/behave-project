def prepare_scenario_table_template(feature_scenarios):
    scenarios_table = ""
    for scenario in feature_scenarios:
        scenarios_table += f"""
        <tr class="scenario-row {scenario["status"]}">
            <td>{scenario["name"]}</td>
            <td class="{scenario["status"]}">{scenario["status"]}</td>
        </tr>
        """
    return scenarios_table


def prepare_feature_table_template(feature_name, feature_status, feature_scenarios):
    return f"""
    <tr class="feature-row {feature_status}">
        <th>{feature_name}</th>
        <th>{feature_status}</th>
    </tr>
    {prepare_scenario_table_template(feature_scenarios)}
    """


style = """
    <style>
        table, th, td {
          border: 1px solid black;
          border-collapse: collapse;
        }
        th, td {
          padding: 15px;
          text-align: left;
        }
        .first-row {
          width: 50%;    
          background-color: #f1f1c1;
        }
        td.passed {
          color: #157a20;
          font-weight: bold;
        }
        td.failed {
          color: #a11717;
          font-weight: bold;
        }
        tr.scenario-row:nth-child(even) {
          background-color: #DBDBDA;
        }
        tr.scenario-row:nth-child(odd) {
          background-color: #FFFFFF;
        }
        tr.scenario-row.failed {
          background-color: #C9B3B3;
        }
        tr.passed.feature-row {
          color: white;
          background-color: #157a20; 
        }
        tr.failed.feature-row {
          color: white;
          background-color: #a11717; 
        }
    </style>
    """


def prepare_report_html_template(
    feature_rows, features_passed_rate, scenarios_passed, scenarios_number
):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Behave Test Report</title>
        {style}
    </head>
    <body>
        <h1> Scenario Pass Rate {features_passed_rate}% ({scenarios_passed}/{scenarios_number})</h1>
        <table id="results">
            {feature_rows}
        </table>
    </body>
    </html>
    """
