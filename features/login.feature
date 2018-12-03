
Feature: Authorization in an bWAPP
#test comment
   Scenario Outline: Check positive data login functionality
     Given Login to bWAPP as a bee user
     #Then Login as <username>, <password>
     #When The authorization as <username> complete, we check logout function

     Examples: By valid data
     | username  | password |
     | bee       | bug      |