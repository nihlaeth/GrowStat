create table if not exists supplies (
    id integer primary key autoincrement,
    name char(100) not null,
    tstamp integer default (DATETIME('now'))
);

insert or ignore into supplies (id, name) values (0, 'Dead');

create table if not exists columns (
    id integer primary key autoincrement,
    name char(100) not null,
    supply integer not null,
    tstamp integer default (DATETIME('now'))
);

insert or ignore into columns (id, name, supply) values (0, 'Dead', 0);

create table if not exists slots (
    id integer primary key autoincrement,
    name char(100) not null,
    col interger not null,
    tstamp integer default (DATETIME('now'))
);

insert or ignore into slots (id, name, col) values (0, 'Dead', 0);

create table if not exists plants (
    id integer primary key autoincrement,
    name char(100) not null,
    lname char(100) not null,
    slot integer not null,
    tstamp integer default (DATETIME('now'))
);

create table if not exists timerconfigs (
    id integer primary key autoincrement,
    name char(100) not null,
    t0000 bool not null default true,
    t0030 bool not null default true,
    t0100 bool not null default true,
    t0130 bool not null default true,
    t0200 bool not null default true,
    t0230 bool not null default true,
    t0300 bool not null default true,
    t0330 bool not null default true,
    t0400 bool not null default true,
    t0430 bool not null default true,
    t0500 bool not null default true,
    t0530 bool not null default true,
    t0600 bool not null default true,
    t0630 bool not null default true,
    t0700 bool not null default true,
    t0730 bool not null default true,
    t0800 bool not null default true,
    t0830 bool not null default true,
    t0900 bool not null default true,
    t0930 bool not null default true,
    t1000 bool not null default true,
    t1030 bool not null default true,
    t1100 bool not null default true,
    t1130 bool not null default true,
    t1200 bool not null default true,
    t1230 bool not null default true,
    t1300 bool not null default true,
    t1330 bool not null default true,
    t1400 bool not null default true,
    t1430 bool not null default true,
    t1500 bool not null default true,
    t1530 bool not null default true,
    t1600 bool not null default true,
    t1630 bool not null default true,
    t1700 bool not null default true,
    t1730 bool not null default true,
    t1800 bool not null default true,
    t1830 bool not null default true,
    t1900 bool not null default true,
    t1930 bool not null default true,
    t2000 bool not null default true,
    t2030 bool not null default true,
    t2100 bool not null default true,
    t2130 bool not null default true,
    t2200 bool not null default true,
    t2230 bool not null default true,
    t2300 bool not null default true,
    t2330 bool not null default true,
    tstamp integer default (DATETIME('now'))
);

create table if not exists ph (
    id integer primary key autoincrement,
    tstamp integer default (DATETIME('now')),
    supply integer not null,
    ph decimal not null
);

create table if not exists ec (
    id integer primary key autoincrement,
    tstamp integer default (DATETIME('now')),
    supply integer not null,
    ec decimal not null
);

create table if not exists temp (
    id integer primary key autoincrement,
    tstamp integer default (DATETIME('now')),
    supply integer not null,
    temp decimal not null
);

create table if not exists harvest (
    id integer primary key autoincrement,
    tstamp integer default (DATETIME('now')),
    plant integer not null,
    weight decimal not null
);

create table if not exists height (
    id integer primary key autoincrement,
    tstamp integer default (DATETIME('now')),
    plant integer not null,
    height decimal not null
);

create table if not exists pictures (
    id integer primary key autoincrement,
    tstamp integer default (DATETIME('now')),
    plant integer not null,
    path char(200) not null
);

create table if not exists logs (
    id integer primary key autoincrement,
    tstamp integer default (DATETIME('now')),
    plant integer not null,
    log text not null
);

create table if not exists watering (
    id integer primary key autoincrement,
    tstamp integer default (DATETIME('now')),
    supply integer not null,
    timerconfig integer not null
);

create table if not exists water (
    id integer primary key autoincrement,
    tstamp integer default (DATETIME('now')),
    supply integer not null,
    volume decimal not null
);

create table if not exists nutrients (
    id integer primary key autoincrement,
    tstamp integer default (DATETIME('now')),
    supply integer not null,
    name char(200) not null,
    amount decimal not null,
    unit char(200) not null
);

create table if not exists movements (
    id integer primary key autoincrement,
    tstamp integer default (DATETIME('now')),
    plant integer not null,
    slot integer not null
);

create table if not exists humidity (
    id integer primary key autoincrement,
    tstamp integer default (DATETIME('now')),
    humidity decimal not null
);

