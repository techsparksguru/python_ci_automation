Feature: This feature performs addition of two numbers in - loop
  
  @headless.scenario
  Scenario Outline: Add two numbers
    Given I have two integers <integerA> and <integerB>
    When I add the two numbers
    Then The resultant is <result>
    
    Examples:
      | integerA | integerB  | result |
      | 5        | 3         | 8      |
      | 10       | 6         | 16     |
      | 15       | 9         | 24     |
      | 20       | 12        | 32     |
      | 25       | 15        | 40     |
