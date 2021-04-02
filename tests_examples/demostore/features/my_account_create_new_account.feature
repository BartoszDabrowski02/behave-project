Feature: My account page - create a new account

    Scenario Outline: very weak password
        Given we are present on the my account page
        When we fill the password for a new account field with <password> value
        Then the statement that your password is very weak appears

        Examples:
        | password    |
        | AAAAAA      |
        | Qwerty      |
        | password123 |
