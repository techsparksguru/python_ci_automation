Feature: This feature performs addition of two numbers
  
  @headless.scenario
  @addition
  Scenario: Add two numbers
    Given I have two integers a and b
    When I add the numbers
    Then I print the addition result