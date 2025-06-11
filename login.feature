Feature: login scenario
@login @only
  Scenario Outline: Login with valid credentials
    Given user has navigated to Login page
#    When User enters valid email as "amotooriapril2023@gmail.com" and password as "12345"
    When User enters valid email as "<email>" and password as "<password>"
    And User clicks on submit button
    Then User should login
  Examples:
    |email                          |password     |
    |amotoorisampleone@gmail.com    |secondone    |
    |amotoorisampletwo@gmail.com    |secondtwo    |
    |amotoorisamplethree@gmail.com  |secondthree  |

  @login
  Scenario: Login with invalid email and valid password
    Given user has navigated to Login page
    When User enters invalid email and valid password
    And User clicks on submit button
    Then Proper valid message should be displayed
@login
  Scenario: Login with valid email and invalid password
    Given user has navigated to Login page
    When User enters valid email and invalid password
    And User clicks on submit button
    Then Proper valid message should be displayed
@login
  Scenario: Login with invalid email and invalid password
    Given user has navigated to Login page
    When User enters invalid email and invalid password
    And User clicks on submit button
    Then Proper valid message should be displayed
@login
  Scenario: Login with no credentials
    Given user has navigated to Login page
    When User do not enter any credentials
    And User clicks on submit button
    Then Proper valid message should be displayed




