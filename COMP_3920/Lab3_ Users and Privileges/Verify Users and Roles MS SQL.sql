use classicmodels;

-- Logins and Associated Users in this Database
select sp.name as login,
       sp.type_desc as login_type,
       case when sp.is_disabled = 1 then 'Disabled'
            else 'Enabled' end as status,
	   sp.create_date, dp.create_date,
	   dp.sid,
	   dp.name AS 'User in DB',
	   dp.type_desc
from sys.server_principals sp
left join sys.sql_logins sl
          on sp.principal_id = sl.principal_id
left join sys.database_principals dp
on sp.sid = dp.sid
where sp.type not in ('G', 'R', 'C', 'U')
and sp.is_disabled = 0
order by sp.name;

-- Roles and their Privileges (GRANTS and tables), Users
	select dp.NAME AS principal_name,
       dp.type_desc AS principal_type_desc,
       o.NAME AS object_name,
       p.permission_name,
       p.state_desc AS permission_state_desc,
	   p.class_desc
	  from   sys.database_permissions p
left   OUTER JOIN sys.all_objects o
on     p.major_id = o.OBJECT_ID
left  JOIN sys.database_principals dp
on     p.grantee_principal_id = dp.principal_id
where dp.NAME != 'public'
order by principal_name


-- Who is in each Roles (which users)
SELECT DP1.name AS DatabaseRoleName,   
   STRING_AGG(DP2.name,', ') AS DatabaseUserName   
 FROM sys.database_role_members AS DRM  
 RIGHT OUTER JOIN sys.database_principals AS DP1  
   ON DRM.role_principal_id = DP1.principal_id  
 LEFT OUTER JOIN sys.database_principals AS DP2  
   ON DRM.member_principal_id = DP2.principal_id  
WHERE DP1.type = 'R'
GROUP BY DP1.name
ORDER BY DP1.name; 

