Feature: Cart summary

    Scenario: Add to cart and verify summary
    When I open automationpractice website
    And I login with username "EMAILADDRESS" and password "PASSWORD"
    And I hover on women menu item and click summer dresses
    And I add a summer dress to cart
    Then verify the item and price