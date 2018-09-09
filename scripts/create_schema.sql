CREATE DATABASE reuters OWNER postgres;

\c reuters;

CREATE TABLE feeds (
  id SERIAL PRIMARY KEY,
  status TEXT,
  updated TEXT,
  encoding TEXT
);


CREATE TABLE entries (
  id SERIAL PRIMARY KEY,
  entry_id TEXT,
  feedburner_origlink TEXT,
  published TEXT,
  title TEXT,
  summary TEXT,
  link TEXT
);

