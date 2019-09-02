create user dbms_project identified by proc123;
grant all privileges to dbms_project;
connect dbms_project/proc123;

/////////////////////successfully created ////////
create or replace procedure calculate_point_table_for(tm_name in varchar2,lg_nm in varchar2,pl out number,g_d out number,w out number,l out number,d out number,poin out number)
as
    goal_f number;
    goal_ag number;
    team_idd number;
    league_idd number;
begin 
    select ID into league_idd from league where lg_name=lg_nm;
    select team_id into team_idd from teams where team_name=tm_name;

    SELECT played,gf,ga,win,loss,draw into pl,goal_f,goal_ag,w,l,d
    from points 
    where team=team_idd and lg_id=league_idd;
    poin:=w*3+d;
    g_d:=goal_f-goal_ag;
end;
/ 
//////////////////
CREATE SEQUENCE team_id_seq
START WITH     0
INCREMENT BY   1
MINVALUE 0;



create or replace procedure insert_new_team(tm_name in varchar2,lg_nm in number,sqd_id in number,address in varchar2,home in varchar2,is_national in number)
as
    code varchar2(3);
    dat date;
begin 
    SELECT CURRENT_DATE into dat FROM dual;
    insert into teams values(team_id_seq.nextval,tm_name,code,address,home,0,dat,is_national,sqd_id,lg_nm);
end;
/
begin
     insert_new_team('espaniol',2,null,'mspain','at_esp_home',0);

end;
/




CREATE SEQUENCE league_id_seq
START WITH     4
INCREMENT BY   1
MINVALUE 0;
create or replace procedure insert_new_league(lg_name in varchar2,season in varchar2,strt in date,end_ in date)
as
begin 
    insert into league values(league_id_seq.nextval,lg_name,0,season,null,strt,end_);
end;
/
show error



begin
     insert_new_league('seri b','2018-2019',TO_DATE('05/05/18', 'DD/MM/YY'),TO_DATE('03/05/19', 'DD/MM/YY'));

end;
/

create or replace trigger tea_leag_junc
after insert on teams
FOR EACH ROW
begin
    insert into league_team values(:new.team_id,:new.league);
end;
/
create or replace trigger pnt_insert
after insert on league_team
for each row
begin
    insert into points values(:new.tm_id,:new.league_id,0,0,0,0,0,0,0);
end;
/



CREATE  SEQUENCE player_id_seq
START WITH     0
INCREMENT BY   1
MINVALUE 0;

create or replace procedure insert_player(p_name in varchar2,birth in date,position varchar2,team varchar2)
as
    t_id number;
    p_id number;
begin
    select player_id_seq.nextval into p_id from dual;
    insert into players values(p_id,p_name,birth,0,position);
    select teams.team_id into t_id from teams where teams.team_name=team;
    insert into team_player values(t_id,p_id);
end;
/
show error;

begin
     insert_player('ronaldo',TO_DATE('01/09/87','dd/mm/yy'),'RW','real madrid');

end;
/
CREATE  SEQUENCE match_id_seq
START WITH     0
INCREMENT BY   1
MINVALUE 0;
create or replace procedure create_match(lg varchar2,home1 varchar2,away varchar2,hg number,ag number,wn number,tp varchar2)
as
    id number;
    lg_id number;
    home_id number;
    away_id number;
begin
   dbms_output.put_line('eije nnaw1111,');
    select match_id_seq.nextval into id from dual;

    dbms_output.put_line('eije nnaw1111,2222222222222222222222 '||home1);
    select team_id 
      into home_id
      from teams
     where team_name=home1;
     dbms_output.put_line('eije nnaw,');
     select team_id 
      into away_id
      from teams
     where team_name=away;
    select league.Id 
      into lg_id
      from league
     where lg_name=lg;
    insert into match values(id,lg_id,home_id,away_id,hg,ag,wn,tp);
end;
/westham,manchester city

exec create_match('EPL','manchester united1','manchester city1',1,0,1,'national')

create or replace trigger pnt_crt
after insert on league_team
for each ROW
begin
    dbms_output.put_line('etriggered '||:new.tm_id||' '||:new.league_id);
   insert into points values(:new.tm_id,:new.league_id,0,0,0,0,0,0,0);
end;
/
show error;

create or replace trigger pnt_updt
after insert on match
for each row
begin
    dbms_output.put_line('eije eije eije');
    update points
       set gf=gf+:new.home_goal,
           ga=ga+:new.away_goal
    where team=:new.home_team and lg_id=:new.league_id;
    update points
       set gf=gf+:new.away_goal,
           ga=ga+:new.home_goal
    where team=:new.away_team and lg_id=:new.league_id;
    if :new.home_goal>:new.away_goal then
        update points
        set win=win+1,
         point=point+3
        where team=:new.home_team and lg_id=:new.league_id;
        update points
        set loss=loss+1
        where team=:new.away_team and lg_id=:new.league_id;
        dbms_output.put_line('eije eije eije1');
    elsif :new.home_goal<:new.away_goal then
        update points
        set win=win+1,
         point=point+3
        where team=:new.away_team and lg_id=:new.league_id;
        update points
        set loss=loss+1
        where team=:new.home_team and lg_id=:new.league_id;
        dbms_output.put_line('eije eije eije2 '||:new.home_team||' '||:new.league_id);
    elsif :new.home_goal=:new.away_goal then
        update points
        set draw=draw+1,
         point=point+1
        where (team=:new.away_team and lg_id=:new.league_id) or (team=:new.home_team and lg_id=:new.league_id);
        dbms_output.put_line('eije eije eije3');
    end if;
    dbms_output.put_line(:new.league_id);
end;
/
show error;

create or replace procedure mat_sqd_ins(match_id in number,player_id in number,sqd_id in number )
as
begin 
    insert into match_squad values (sqd_id,player_id,match_id);
end;
/
show error

create or replace procedure mat_goal_insert(match_id number,scorer_id number,minute number,owngoal number)
as
begin
  insert into  mat_goals
  values (match_id,scorer_id,minute,owngoal);
end;
/
show error

create or replace procedure get_goal_player(player_name in varchar2,ret out number)
as
    ID number;
begin 
    select player_id into ID from players where players.name=player_name;
    select count(*)
      into ret
      from mat_goals
     where scorer_id=ID;
end;
/
show error


create or replace trigger pnt_updt
after insert on match
for each row

drop trigger goals_leag;


create or replace trigger goals_leag12
after insert on team_player
for each ROW
declare
    leg_id number;
begin
    null;
    select league_id into leg_id from league_team where tm_id=:new.team_id;
    insert into goals_leag values(leg_id,:new.player_id,0);
end;
/
show error

create or replace trigger goals_leag2
after insert on mat_goals
for each ROW
begin
update goals_leag
   set goals=goals+1
 where  player_ID=:old.scorer_id;

end;
/