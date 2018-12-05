Feature: A1 injection: HTML injection - reflected(GET)

   Scenario Outline: negative input field testing
     Given select option <value> in the bug list and press hack
     Then enter data <firstname>, <lastname> and submit the form
     When The ...

     Examples: By incorrect data
     | value | firstname       | lastname |
     | 2     | <h1>HACKED</h1> | <p></p>  |