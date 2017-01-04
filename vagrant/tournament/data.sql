INSERT INTO player (name) VALUES('Bob');
INSERT INTO player (name) VALUES('Alice');
INSERT INTO player (name) VALUES('Mike');
INSERT INTO player (name) VALUES('John');
INSERT INTO player (name) VALUES('Susan');
INSERT INTO player (name) VALUES('Rene');

INSERT INTO tournament VALUES (
    DEFAULT
);

INSERT INTO match (winner, looser, tournament) VALUES
    (2, 1, 1), (3, 1, 1), (3, 2, 1)
;
