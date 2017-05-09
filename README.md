# ZeitSonde

ZeitSonde is a small time tracking system. It is still under development.


## Dependencies

ZeitSonde requires [Python (>=3.5.x)](https://www.python.org/), [Node.js
(>=6.x)](https://nodejs.org/), [Yarn](https://yarnpkg.com) and [some libraries
and build tools](http://crossbar.io/docs/Installation-on-Linux/#prepare). You
also need a running MongoDB server instance.


## Setup WAMP router and server application

To setup and run Crossbar.io as WAMP router and our server application open a
new terminal and run:

    $ python --version  # Should return Python 3.5 or higher
    $ python -m venv .virtualenv
    $ source .virtualenv/.bin/activate
    $ pip install --upgrade pip setuptools
    $ pip install --requirement requirements.txt
    $ yarn
    $ node_modules/.bin/gulp
    $ crossbar start


## Setup client application

To setup and run our client application open a new terminal and run:

    $ echo TODO


## Open Browser

Now you can open your webbrowser at http://localhost:8080/.
