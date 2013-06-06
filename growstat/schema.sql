create table if not exists supplies (
    id integer primary key autoincrement,
    name char(100) not null,
    tstamp integer default now
);

insert or ignore into supplies (id, name) values (0, 'Dead');

create table if not exists columns (
    id integer primary key autoincrement,
    name char(100) not null,
    supply integer not null,
    tstamp integer default now
);

insert or ignore into columns (id, name, supply) values (0, 'Dead', 0);

create table if not exists slots (
    id integer primary key autoincrement,
    name char(100) not null,
    col interger not null,
    tstamp integer default now
);

insert or ignore into slots (id, name, col) values (0, 'Dead', 0);

create table if not exists plants (
    id integer primary key autoincrement,
    name char(100) not null,
    lname char(100) not null,
    slot integer not null,
    tstamp integer default now
);

create table if not exists timerconfigs (
    id integer primary key autoincrement,
    name char(100) not null,
    t0000 bool not null,
    t0030 bool not null,
    t0100 bool not null,
    t0130 bool not null,
    t0200 bool not null,
    t0230 bool not null,
    t0300 bool not null,
    t0330 bool not null,
    t0400 bool not null,
    t0430 bool not null,
    t0500 bool not null,
    t0530 bool not null,
    t0600 bool not null,
    t0630 bool not null,
    t0700 bool not null,
    t0730 bool not null,
    t0800 bool not null,
    t0830 bool not null,
    t0900 bool not null,
    t0930 bool not null,
    t1000 bool not null,
    t1030 bool not null,
    t1100 bool not null,
    t1130 bool not null,
    t1200 bool not null,
    t1230 bool not null,
    t1300 bool not null,
    t1330 bool not null,
    t1400 bool not null,
    t1430 bool not null,
    t1500 bool not null,
    t1530 bool not null,
    t1600 bool not null,
    t1630 bool not null,
    t1700 bool not null,
    t1730 bool not null,
    t1800 bool not null,
    t1830 bool not null,
    t1900 bool not null,
    t1930 bool not null,
    t2000 bool not null,
    t2030 bool not null,
    t2100 bool not null,
    t2130 bool not null,
    t2200 bool not null,
    t2230 bool not null,
    t2300 bool not null,
    t2330 bool not null,
    tstamp integer default now
);

create table if not exists ph (
    id integer primary key autoincrement,
    tstamp integer default now,
    supply integer not null,
    ph decimal not null
);

create table if not exists ec (
    id integer primary key autoincrement,
    tstamp integer default now,
    supply integer not null,
    ec decimal not null
);

create table if not exists temp (
    id integer primary key autoincrement,
    tstamp integer default now,
    supply integer not null,
    temp decimal not null
);

create table if not exists harvest (
    id integer primary key autoincrement,
    tstamp integer default now,
    plant integer not null,
    weight decimal not null
);

create table if not exists height (
    id integer primary key autoincrement,
    tstamp integer default now,
    plant integer not null,
    height decimal not null
);

create table if not exists pictures (
    id integer primary key autoincrement,
    tstamp integer default now,
    plant integer not null,
    path char(200) not null
);

create table if not exists logs (
    id integer primary key autoincrement,
    tstamp integer default now,
    plant integer not null,
    log text not null
);

create table if not exists watering (
    id integer primary key autoincrement,
    tstamp integer default now,
    supply integer not null,
    timerconfig integer not null
);

create table if not exists water (
    id integer primary key autoincrement,
    tstamp integer default now,
    supply integer not null,
    volume decimal not null
);

create table if not exists nutrients (
    id integer primary key autoincrement,
    tstamp integer default now,
    supply integer not null,
    name char(200) not null,
    volume decimal not null
);

create table if not exists movements (
    id integer primary key autoincrement,
    tstamp integer default now,
    plant integer not null,
    slot integer not null
);

create table if not exists humidity (
    id integer primary key autoincrement,
    tstamp integer default now,
    humidity decimal not null
);

