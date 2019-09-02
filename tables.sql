create user dbms_project identified by proc123;
grant all privileges to dbms_project;
connect dbms_project/proc123;

insert into league values(1,'EnglishPremireLeague',1,'2018/2019',NULL,NULL,NULL);
insert into league values(2,'Spanish la liga',1,'2018/2019',NULL,NULL,NULL);
insert into league values(3,'BundeLiga',1,'2018/2019',NULL,NULL,NULL);
create table  league(
    Id number primary key,
    lg_name varchar2(20),
    title number,
    season varchar2(20),
    winner_id number,  --this has to be a foreign key to team table
    start_date date,
    end_date date
);
create table league_team( ------junction table
    tm_id number,
    league_id number,
    constraint fk_lt_1 foreign key (league_id) references league,
    constraint fk_lt_2 foreign key (tm_id) references teams

);
alter table points add point number;
create table points(
    team number,
    lg_id number,
    played number,
    gf number,
    ga number,
    win number,
    loss number,
    draw number,
    point number,
    constraint pk_pts primary key(team,lg_id),
    constraint fk_lt_3 foreign key (lg_id) references league,
    constraint fk_lt_4 foreign key (team) references teams
);
alter table teams add league number;
create table teams(
    team_id number primary key,
    team_name varchar2(20) unique,
    code varchar2(20),--BAR for barcelona
    address varchar2(20),
    home varchar2(20),
    trophies number,
    established date,
    is_national number(1,0),
    squad_id number,--this is foreign key to the squad
    league number
);
create table team_player(--junction table
    team_id number,
    player_id number,
    constraint fk_tp_1 foreign key (player_id) references players,
    constraint fk_tp_2 foreign key (team_id) references teams
);
create table players(
    player_id number primary key,
    name varchar2(20),
    birth_date date,
    titles_ID number,--foreign key to some uncreated player title table
    position varchar(20)
    --will have relation with goals scored lifetime table 
);


create table match(
    match_id number primary key,
    league_id number,
    home_team number,
    away_team number,
    home_goal number,
    away_goal number,
    home_win number,
    match_type varchar2(20),
     constraint fk_mt_1 foreign key(league_id) references league,
     constraint fk_mt_2 foreign key(home_team) references teams,
     constraint fk_mt_3 foreign key(away_team) references teams
    ---should have the data of the squad playing??
);
create table match_squad(
    sqd_id  number primary key,
    player_id number,
    match_id number,
  constraint fk_msqd_1 foreign key(match_id) references match,
  constraint fk_msqd_2 foreign key(player_id) references players
);
create table mat_goals(
    --goal_ID number primary_key,
    --goals scored by a player can be calculated from this table and the players table,
    match_id number,
    scorer_ID number,
    score_minute number,
    owngoal number,
    constraint fk_mtgl_1 foreign key(match_id) references match,
    constraint fk_mtgl_2 foreign key(scorer_id) references players
);
create table mat_events(
    --goal_ID number primary_key,
    --so can cards,injuries or etcetra of a player like the goal count can be calculated from here
    match_id number,
    player_ID number,
    minute number,
    --owngoal boolean,
    event_type varchar2(20),
    create constraint fk_mtev_1 match_id references match,
    create constraint fk_mtev_2 player_id references players
);
create table goals_leag(
    league_id number, 
    player_ID number ,
    goals number,
    constraint pkhabijabi primary key(league_id,player_ID),
    constraint fk_mtgl_11 foreign key(league_id) references match,
    constraint fk_mtgl_21 foreign key(player_id) references players
);




select * from points where lg_id=2 ORDER BY point,gf-ga desc;