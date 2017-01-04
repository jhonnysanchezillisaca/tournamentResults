-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


CREATE TABLE player (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE tournament (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE match (
    id SERIAL PRIMARY KEY,
    winner INTEGER REFERENCES player,
    looser INTEGER REFERENCES player,
    tournament INTEGER REFERENCES tournament
);

CREATE VIEW total_wins as SELECT player.id, player.name, count(match.winner) as total FROM player LEFT JOIN match ON player.id = match.winner GROUP BY player.name, player.id ORDER BY total desc;

CREATE VIEW total_matches as SELECT player.id, player.name, count(match.id) as total FROM player LEFT JOIN match ON player.id = match.winner OR player.id = match.looser GROUP BY player.name, player.id ORDER BY total desc;
