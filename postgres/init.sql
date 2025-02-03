CREATE EXTENSION postgis;

CREATE TABLE ais_positions (
    id SERIAL PRIMARY KEY,
    mmsi BIGINT,
    lat DOUBLE PRECISION,
    lon DOUBLE PRECISION,
    speed DOUBLE PRECISION,
    course INT,
    heading INT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    geom GEOMETRY(Point, 4326)
);
