SELECT t.title , t.description, u.fullname  FROM tasks t 
JOIN users u ON u.id = t.user_id 
WHERE u.id  = 4;

SELECT t.title , t.description, s."name" as "Status" FROM tasks t 
JOIN status s ON s.id = t.status_id 
WHERE s."name"  ='in progress';

update tasks set
status_id  = 3
from tasks t 
where tasks.id  = 4;

select * from users u 
where u.id  not in (select t.user_id  from tasks t);

insert into tasks (title, description, status_id, user_id)
values ('New title', 'New escription', 1, 1);

select title, description, s."name" as "Status" from tasks t 
inner join status s on s.id  = t.status_id 
where s."name" != 'completed';

delete from tasks t where t.id  = 21;

select * from users u where email like '%example.org';

update users set fullname = 'Borys Johnsonuk' where fullname  = 'Kayla Decker';

select count(t.id), s."name" as "Status" from tasks t 
inner join status s on s.id  = t.status_id  
group by s."name";

select t.title, t.description  from tasks t 
inner join users u ON u.id = t.user_id
where u.email like '%example.org';

select * from tasks t 
where t.description  = '';
--field is not null

select u.fullname, title, description, s."name" as "Status" from tasks t
inner join users u on u.id  = t.user_id 
inner join status s on s.id  = t.status_id 
where s."name" = 'in progress';

select u.fullname , count(t.id) from users u 
left join tasks t on t.user_id  = u.id 
group by u.fullname; 