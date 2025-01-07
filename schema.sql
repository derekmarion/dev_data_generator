BEGIN;
-- https://www.postgresql.org/docs/9.1/intarray.html
-- this is used for the && operator (array overlap)
CREATE EXTENSION intarray;


CREATE TABLE betting_group (
    id INTEGER PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    name TEXT UNIQUE NOT NULL,
    admission_code TEXT UNIQUE NOT NULL,
    user_ids INTEGER[] DEFAULT '{}'
);
CREATE INDEX betting_group_user_id ON betting_group USING GIN(user_ids);

CREATE TABLE league (
    id INTEGER PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE team (
    id INTEGER PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    name TEXT UNIQUE NOT NULL,
    league_id INTEGER REFERENCES league(id) NOT NULL,
    UNIQUE (name, league_id)
);
CREATE INDEX team_league_id ON team USING btree(league_id);

CREATE TABLE game (
    id INTEGER PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    league_id INTEGER REFERENCES league(id) NOT NULL,
    team_1 INTEGER REFERENCES team(id) NOT NULL,
    team_2 INTEGER REFERENCES team(id) NOT NULL,
    CHECK (team_1 <> team_2)
);
CREATE INDEX game_league_id ON game USING btree(league_id);
CREATE INDEX game_team_1 ON game USING btree(team_1);
CREATE INDEX game_team_2 ON game USING btree(team_2);

COMMIT;
