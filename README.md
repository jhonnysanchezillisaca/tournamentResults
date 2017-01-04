Tournament Results project
=============

Tournament Results is a project that uses the PostgreSQL database to keep track of players and matches in a game tournament.

The game tournament uses Swiss system for pairing up players in each round: players are not eliminated, and each player is paired with another player with the same number of wins, or as close as possible.

The repository contains the virtual machine configuration to use with Vagrant and the code of the project in the ``/vagrant/tournament/`` directory.

## Files

The project is composed of four files:

- ``tournament.py``: contains the code of the program that controls the logic of the tournament.
- ``tournament.sql``: contains the database schema.
- ``tournament_test.py``: contains unit tests.
- ``data.sql``: contains SQL code to populate the DB.

## Installation and use

To run this project you need to have installed VirtualBox and Vagrant.

Once started the vagrant machine, go to ``/vagrant/tournament/`` directory.

To run the tests simply type the following code:
`` $ python tournament_test.py ``
