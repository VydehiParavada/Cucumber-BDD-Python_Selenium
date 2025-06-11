Feature: Register functionality
  @register @thisone
  Scenario: Register with mandatory fields
    Given User navigates to register page
    When User enter below details to all mandatory fields
      | first_name | last_name | telephone | password |
      | Vyd        | Par       | 848972842 | 23456    |
    And User click on privacy statement
    And User clicks on Continue button
    Then Account should be created
  @register
  Scenario: Register with all fields
    Given User navigates to register page
    When User enter details to all fields
    And User click on privacy statement
    And User clicks on Continue button
    Then Account should be created
  @register
  Scenario: Register with duplicate email address
    Given User navigates to register page
    When User enter details to all fields except email address
    And User enter existing email address
    And User click on privacy statement
    And User clicks on Continue button
    Then Proper warning message is displayed
  @register
  Scenario: Register without providing any details
    Given User navigates to register page
    When User does not enter any details
    And User clicks on Continue button
    Then Proper warning message is displayed for all fields