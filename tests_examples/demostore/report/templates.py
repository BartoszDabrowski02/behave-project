def prepare_scenario_table_template(feature_scenarios):
    scenarios_table = ""
    for scenario in feature_scenarios:
        scenarios_table += f"""
        <tr>
            <td>{scenario["name"]}</td>
            <td>{scenario["status"]}</td>
        </tr>
        """
    return scenarios_table


def prepare_feature_table_template(feature_name, feature_status, feature_scenarios):
    return f"""
    <tr>
        <th>{feature_name}</th>
        <th>{feature_status}</th>
    </tr>
    {prepare_scenario_table_template(feature_scenarios)}
    """


green = "#157a20"
red = "#a11717"

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
        #first-row {
          width: 50%;    
          background-color: #f1f1c1;
        }
        #first-row tr:nth-child(even) {
          background-color: #eee;
        }
        #first-row tr:nth-child(odd) {
          background-color: #fff;
        }
        #first-row th {
          color: white;
          background-color: black;
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
        <table id="first-row">
            {feature_rows}
        </table>
    </body>
    </html>
    """
