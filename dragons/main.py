"""
This module contains the Dragons command line entry point
"""

import argparse

import gevent

from dragons.engine import process


def build_parser():
    """
    Handle the main command line, ie. selecting a command to run.
    """

    parser = argparse.ArgumentParser(prog='dragons')

    subparsers = parser.add_subparsers(title='commands',
        help='run "dragons {command} -h" for specific help')

    # The local mode 'run' subcommand
    run_parser = subparsers.add_parser('run',
        help='Run dragon locally')

    run_group = run_parser.add_argument_group('run optional arguments')

    run_group.add_argument('--concurrency',
        dest='conc',
        help='Similtaneous workers (def: 1)',
        type=int, default=1)

    run_group.add_argument('--host',
        dest='host',
        help='Target host (def: http://localhost:8000)',
        type=str, default='http://localhost:8000')

    run_group.add_argument('--entry',
        dest='entry',
        help='Dragonfile entry function (def: start)',
        type=str, default='start')

    run_parser.set_defaults(func=_main_run)

    # stubs for future subcommands, AWS integration point
    #subparsers.add_parser('add', help='Spawn new instances in hoard')
    #subparsers.add_parser('list', help='List the instances in hoard')
    #subparsers.add_parser('remove', help='Remove instances from hoard')

    return parser

def load_dragonfile():
    """
    Loads the provided dragonfile
    """

    try:
        return  __import__('dragonfile')
    except ImportError:
        print 'Failed to load dragonfile!'
        raise

def _main_run(args):
    """
    Main command-line execution loop.
    """

    # Prepare the settings for the engine
    settings = {
        'host': args.host,
    }

    dragonfile = load_dragonfile()
    concurrency = args.conc
    workers = [gevent.spawn(process, dragonfile, settings) for _i in range(concurrency)]

    try:
        gevent.joinall(workers)
    except KeyboardInterrupt:
        print 'done'

if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)
