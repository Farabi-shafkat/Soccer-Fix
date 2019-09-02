CREATE OR REPLACE TYPE typ_array IS VARRAY(500) OF VARCHAR2(4000)

create or replace procedure import Extract_all_league_names(arr IN typ_array)
is 
begin
    select 
    out1:=name1+100;
end;
/
show error;