Feature: verify the home page

    Scenario: check the home page title
        Given we are present on the home page
        Then the page title is "DemoStore – Just another WordPress site"

    Scenario Outline: check the home page tabs
        Given we are present on the home page
        Then the "<tab_label>" tab is present

        Examples:
        | tab_label   |
        | Home        |
        | Cart        |
        | Checkout    |
        | My account  |
        | Sample Page |

      Scenario Outline: check navigation using tabs
        Given we are present on the home page
        When we click on <tab_label> tab
        Then the page title is <page_title>

        Examples:
        | tab_label   | page_title                              |
        | Home        | DemoStore – Just another WordPress site |
        | Cart        | Cart – DemoStore                        |
        | Checkout    | Cart – DemoStore                        |
        | My account  | My account – DemoStore                  |
        | Sample Page | Sample Page – DemoStore                 |



#   git push origin master
#   behave features\tutorial.feature --no-capture
#   C:\Users\bartoszeg\AppData\Local\Programs\Python\Python38
