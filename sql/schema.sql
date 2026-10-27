-- Mythical Creature Refuge — schema (re-runnable)

DROP TABLE IF EXISTS health_records CASCADE;
DROP TABLE IF EXISTS missions CASCADE;
DROP TABLE IF EXISTS destinations CASCADE;
DROP TABLE IF EXISTS employees CASCADE;
DROP TABLE IF EXISTS creatures CASCADE;
DROP TABLE IF EXISTS enclosures CASCADE;

CREATE TABLE enclosures (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    capacity INTEGER NOT NULL CHECK (capacity > 0)
);

CREATE TABLE creatures (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    species TEXT NOT NULL,
    origin TEXT NOT NULL,
    power_level INTEGER NOT NULL CHECK (power_level BETWEEN 0 AND 100),
    element TEXT,
    resurrection_count INTEGER NOT NULL DEFAULT 0 CHECK (resurrection_count >= 0),
    in_refuge BOOLEAN NOT NULL DEFAULT TRUE,
    enclosure_id INTEGER REFERENCES enclosures (id) ON DELETE RESTRICT,
    registered_at TIMESTAMPTZ NOT NULL DEFAULT now(),

    CONSTRAINT ck_creatures_species
        CHECK (species IN ('Dragon', 'Phoenix', 'Unicorn', 'Griffin', 'Basilisk')),
    CONSTRAINT ck_creatures_element_only_dragon
        CHECK (element IS NULL OR species = 'Dragon')
);

CREATE TABLE employees (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    role TEXT NOT NULL,
    certification_level INTEGER CHECK (certification_level BETWEEN 1 AND 5),
    supervisor_id INTEGER REFERENCES employees (id) ON DELETE SET NULL,
    hired_on DATE NOT NULL DEFAULT CURRENT_DATE,

    CONSTRAINT ck_employees_role
        CHECK (role IN ('handler', 'veterinarian')),
    CONSTRAINT ck_employees_handler_has_level
        CHECK (role <> 'handler' OR certification_level IS NOT NULL)
);

CREATE TABLE destinations (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    danger_multiplier NUMERIC(3, 1) NOT NULL DEFAULT 1.0 CHECK (danger_multiplier >= 1.0)
);

CREATE TABLE missions (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    creature_id INTEGER NOT NULL REFERENCES creatures (id)    ON DELETE RESTRICT,
    handler_id INTEGER NOT NULL REFERENCES employees (id)    ON DELETE RESTRICT,
    destination_id INTEGER NOT NULL REFERENCES destinations (id) ON DELETE RESTRICT,
    departure_date DATE NOT NULL,
    duration_days INTEGER NOT NULL CHECK (duration_days > 0),
    base_reward NUMERIC(10, 2) NOT NULL CHECK (base_reward >= 0),
    returned_on DATE,
    notes TEXT NOT NULL DEFAULT '',

    CONSTRAINT ck_missions_return_after_departure
        CHECK (returned_on IS NULL OR returned_on >= departure_date),
    CONSTRAINT uq_missions_creature_departure
        UNIQUE (creature_id, departure_date)
);

CREATE TABLE health_records (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    creature_id INTEGER NOT NULL REFERENCES creatures (id) ON DELETE CASCADE,
    vet_id INTEGER NOT NULL REFERENCES employees (id) ON DELETE RESTRICT,
    examined_on DATE NOT NULL DEFAULT CURRENT_DATE,
    status TEXT NOT NULL,
    diagnosis TEXT NOT NULL,
    treatment TEXT NOT NULL DEFAULT '',

    CONSTRAINT ck_health_records_status
        CHECK (status IN ('healthy', 'under_observation', 'in_treatment', 'quarantine'))
);