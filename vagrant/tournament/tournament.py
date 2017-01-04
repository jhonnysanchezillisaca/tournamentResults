#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    cur = db.cursor()
    cur.execute("DELETE FROM match")

    db.commit()

    cur.close()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    cur = db.cursor()
    cur.execute("DELETE FROM player")

    db.commit()

    cur.close()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT count(*) FROM player;")
    # The cursor returns a tuple, the data we want is in the first element
    num_players = cur.fetchone()[0]
    db.commit()

    cur.close()
    db.close()

    return num_players


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    cur = db.cursor()
    cur.execute("INSERT INTO player (name) VALUES (%s);", (name,))

    db.commit()

    cur.close()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place,
    or a player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT w.id, w.name, w.total as wins, m.total as matches FROM total_wins as w, total_matches as m WHERE w.id = m.id ORDER BY w.total;")  # NOQA

    result = cur.fetchall()

    db.commit()

    cur.close()
    db.close()

    return result


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    cur = db.cursor()
    cur.execute("INSERT INTO match (winner, looser, tournament) VALUES (%s, %s, 1);", (winner, loser))  # NOQA

    db.commit()

    cur.close()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    players_ranking = playerStandings()
    # Separates the player in two list, then zip two adjacent players
    players_even = [[p[0], p[1]] for p in players_ranking if
                    players_ranking.index(p) % 2 == 0]
    players_uneven = [(p[0], p[1]) for p in players_ranking if
                      players_ranking.index(p) % 2 != 0]

    # Create four lists, with the ids and names of the even and uneven lists
    even_list = zip(*players_even)
    uneven_list = zip(*players_uneven)

    # Zip the four lists, (id1, name1, id2, name2)
    result = zip(even_list[0], even_list[1], uneven_list[0], uneven_list[1])

    return result
