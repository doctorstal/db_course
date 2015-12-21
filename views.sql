CREATE OR REPLACE VIEW executor_list AS 
  SELECT executor_id, executor_name, COUNT(DISTINCT task_id) AS "Tasks"
  FROM executors NATURAL LEFT JOIN tasks
  GROUP BY executor_id, executor_name;
  

CREATE OR REPLACE VIEW contracts_list AS 
  SELECT contracts.contract_id,
    companies.company_id,
    company_name AS "Company",
    NVL(contract_name, 'No contracts yet') AS "Contract"    
  FROM companies 
    LEFT JOIN contracts ON contracts.COMPANY_ID = companies.COMPANY_ID
    ORDER BY companies.COMPANY_ID;
    
CREATE OR REPLACE VIEW processes_list AS
  SELECT processes.contract_id as contract_id, process_id,
    company_name||'/'||contract_name AS "Company/Contract",
    process_name AS "Process"
  FROM processes
  LEFT JOIN contracts ON contracts.contract_id = processes.contract_id
  JOIN companies ON companies.company_id = contracts.company_id
  
  ORDER BY process_name;

CREATE OR REPLACE VIEW processes_list_min_status AS
  SELECT contract_id, process_id,
      company_name||'/'||contract_name AS "Company/Contract",
      process_name AS "Process",
      status_id AS "Min task status"
      FROM
       (SELECT processes.process_id, MIN(status_id) as status_id
        FROM  
            (SELECT task_id, MAX(new_status_id) AS status_id
                FROM timeline 
                GROUP BY task_id) 
                  NATURAL JOIN tasks 
                  RIGHT JOIN PROCESSES ON tasks.process_id = processes.process_id 
                  GROUP BY processes.process_id)
          NATURAL JOIN processes
          NATURAL JOIN contracts
          NATURAL JOIN companies
  ;
        
        

CREATE OR REPLACE VIEW tasks_list AS
  SELECT task_name AS "Task name", task_id, executor_name, process_name AS "Process name", status_name AS "Status", status_id, process_id, prev_id, executor_id
    FROM statuses 
    NATURAL JOIN (SELECT task_id,
          MAX(new_status_id) AS status_id
          FROM timeline
          GROUP BY task_id)
    NATURAL JOIN tasks
    NATURAL JOIN processes
    NATURAL JOIN executors
    NATURAL JOIN tasks_order
  ;
  
  

  