Feature: Search functionality

@search
  Scenario: search a valid product
    Given User is navigated to home page
    When user entered valid product in search field
    And user clicked on search button
    Then Valid product should display in search result

@search
  Scenario: search an invalid product
    Given User is navigated to home page
    When user entered invalid product in search field
    And user clicked on search button
    Then Proper message should be displayed in search result
@search
  Scenario: search without entering any product
    Given User is navigated to home page
    When user did not enter any product in search field
    And user clicked on search button
    Then Proper message should be displayed in search result