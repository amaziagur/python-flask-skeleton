# python-flask-skeleton
a python skeleton based on flask , developed in TDD methodology.

## Usage
### greeter web service
#### installing
run pip install -r requirments.txt
#### running
run service -> python /skeleton_greeter/greeter.py

call in rest client (GET) to - localhost:8080/greet -> you will get general greeting from service

call in rest client (GET) to - localhost:8080/greet/{your_name} -> you will get personal greeting from service

**between 14 to 16 @ noon time, server is sleeping so you will get zzz as a response :)

## Tests
### unit tests using Nose
unit tests focusing on clock behavor and messager

### componenet tests using Behave
focusing on system functionality
