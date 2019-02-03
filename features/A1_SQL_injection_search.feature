Feature: A1 injection: SQL injection GET/POST search

   Scenario Outline: The simplest case to detect error
     Given option <value> in the bug list and press hack
     Then enter data <sql_injection_case> and submit the form
     When the form is submited this <err_msg> must be including into table#table_yellow
        #expected result:
           # injection code not included
           # "<table id=table_yellow>" include <error_message> string

     Examples: By incorrect data
     | value | sql_injection_case                      | err_msg               |
     | 15    | '                                       | No movies were found! |
     | 13    | 'union select 1,@@version,3,4,5,6,7-- - | No movies were found! |

