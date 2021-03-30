Feature: verify the home page

    Scenario: check the home page title
        Given we are present on the home page
        Then the page title is "DemoStore – Just another WordPress site"

    Scenario Outline: check the home page tabs
        Given we are present on the home page
        Then the "<tab>" tab is present

        Examples:
        | tab         |
        | Home        |
        | Cart        |
        | Checkout    |
        | My account  |
        | Sample Page |
