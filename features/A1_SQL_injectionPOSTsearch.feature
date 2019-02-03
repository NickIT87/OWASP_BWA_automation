Feature: A1 injection: SQL injection POST/search

   Scenario Outline: The simplest case to detect error
     Given option <value> in the bug list and press hack
     Then enter data <sql_injection_case> and submit the form
     When the form is submited this <error_message> must be including into table#table_yellow
        #expected result:
           # injection code not included
           # "<table id=table_yellow>" include <error_message> string

     Examples: By incorrect data
     | value | sql_injection_case | error_message         |
     | 15    | '                  | No movies were found! |