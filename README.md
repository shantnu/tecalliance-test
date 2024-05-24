# tecalliance test

- [tecalliance test](#tecalliance-test)
  - [TecAlliance Excercise](#tecalliance-excercise)
  - [To run the tests](#to-run-the-tests)
  - [Comments and Answers](#comments-and-answers)

## TecAlliance Excercise

In this repo, I try to implement the tests given in the TecAlliance document.

The document doesnt specify which server to use, so I wrote a dummy server in Python Flask, so I had something to test against.

The server is in _server.py_

The acutal tests are in _test\_server.py_



## To run the tests

Create and activate virtual env:

```
python3 -m venv .venv
source .venv/bin/activate
```

Install python libraries:

```
pip install -r requirements.txt
```

Run the tests:

Open 2 terminals. In first start the web server:

```
python server.py
```

In 2nd, run the tests:

```
pytest
```


## Comments and Answers

In the original doc, it says:

> a REST endpoint with 150 methods

Not sure what this meant.


> Please explain your approach to achieve 100% test coverage


Again, not sure about this. As a tester, I cannot gurantee 100% code coverage-- this is for the person writing the server. I can check for **100% specification coverage** -- that is, all the specifications are tested, manually or automated.

Server Coverage: For the test server, I did try to use the Python coverage tool, but I couldnt get it working in my setup.

**If I Had more time**

* I would try to understand the specifications better, as it's not 100% clear what I'm testing. To write more tests, I need to understand what the server does.

* I would try to get code coverage for my dummy web server working-- I added the library but it wasn't working as expected.

