--	Should generate report for one week.
--	Report should contain folowing data:
--		- List of tasks, finished last week
--		- Who've done that tasks?

SELECT task_id, task_name, process_name, executor_name
  FROM timeline 
  NATURAL JOIN tasks 
  NATURAL JOIN processes
  NATURAL JOIN executors
  WHERE new_status_id=2 AND modified BETWEEN SYSDATE - 7 AND SYSDATE;

--		- Unfinished contracts data:
--			- list of tasks
SELECT task_name, process_name, contract_name, executor_name
FROM contracts
  NATURAL JOIN executors
  NATURAL JOIN processes
  NATURAL JOIN tasks 
  NATURAL JOIN 
  (SELECT task_id
    FROM timeline
    GROUP BY task_id HAVING MAX(new_status_id)<2);
    
--		- Unplanned contracts
(SELECT process_id
  FROM processes)
  MINUS
  (SELECT process_id
  FROM tasks);
  
  (SELECT contract_id, contract_name
  FROM contracts)
  MINUS
  (SELECT contract_id, contract_name
  FROM contracts NATURAL JOIN processes
  NATURAL JOIN tasks);


--		- Deadline violators
SELECT executor_name, task_name, completion_time*24*60
  FROM EXECUTORS
    NATURAL JOIN TASKS
    NATURAL JOIN
  (SELECT task_id, MAX(modified) - MIN(modified) AS completion_time
      FROM timeline 
      WHERE new_status_id = 1 OR new_status_id = 2
      GROUP BY task_id HAVING (MAX(modified) > MIN(modified) + INTERVAL '1' DAY));
    
