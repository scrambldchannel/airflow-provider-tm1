# airflow-provider-tm1

An experimental airflow provider package for TM1 that leverages TM1py.

## Status

It's experimental at this stage but the hook test passes as a PoC with Airflow 2.4.2 and TM1py 1.10.1 and a tm1 server to test against.

## Notes

+ Auth part could be improved
+ + Look at adding a custom connection type?
+ I get loads of deprecation warnings with my local setup
+ I need to get my head around how to set up a breeze test env with the provider installed
+ There's a vague outline of a mock of the Tm1py RestService
+ + I'm mixing and matching pytest-mock and unittest mock which isn't ideal
