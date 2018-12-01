
Feature: Authorization in an instagram
#test comment
   Scenario Outline: Check positive data login functionality
     Given I am on authorization page
     Then Login as <username>, <password>
     Then Skip download app
     When The authorization as <username> complete, we check logout function

     Examples: By valid data
     | username  | password |
     | mrfox7315 | *******  |