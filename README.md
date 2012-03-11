# Dragons

Psuedo-realistic load generator for web servers. gevent is leveraged for high concurrency and boto (AWS / EC2) to for web scale expansion.

This project is very young and under heavy development. We are striving towards a stable alpha interface.

## Goals

The ultimate goal of this project to enable load testing during the entire continuous development process.
Centralised load processing steps will enable load testing to be performed locally, even before changes are committed.
Additionally, load testing should be automatic and effortless during the build pipeline.
Any dips in performance should trigger alerts to developers.

## Features

*   Load is generated by simple workflows that resemble Finite State Machines.
*   Workflows are stored in a dragonfile, separate from server configuration details. This is a design choice to decouple the logic and configuration.
*   Access to the underlying HTTP client permits rich interactions (ie. cookies).

## Usage

### Development

After cloning the repo and installing dependencies (requirements.txt), do:

1.  "cd path/to/dragons/repo"
2.  "cp examples/example.py dragonfile.py"
3.  tweak the contents of dragonfile.py to your liking
4.  "python dragons/main.py -h" for basic help
5.  "python dragons/main.py run -h" for basic help on running dragon locally

## TODO

*   Add EC2 instance creation / termination
*   Decide how to install Dragons onto a remote EC2 instance
*   Fix setup.py; geventhttpclient is not available in repos yet.
*   Make command more reliable and produce statistical output.

## Contributors

*   [Adam Neumann](https://github.com/noizwaves)

## License

TODO