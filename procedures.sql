CREATE OR REPLACE PROCEDURE add_executor(p_name IN VARCHAR) IS
  BEGIN
    INSERT INTO executors(executor_name)
      VALUES (p_name);
  END;
/
CREATE OR REPLACE FUNCTION get_executor_id(p_name IN VARCHAR)
  RETURN NUMBER
  IS
    v_res NUMBER;
  BEGIN
    SELECT executor_id INTO v_res FROM executors WHERE executor_name=p_name;
    RETURN v_res;
  END;
/

CREATE OR REPLACE PROCEDURE add_company(p_name IN VARCHAR) IS
  BEGIN
    INSERT INTO companies(company_name)
      VALUES (p_name);
  END;
/

CREATE OR REPLACE PROCEDURE add_contract(p_company_id IN NUMBER, p_contract_name IN VARCHAR) IS
  BEGIN
    INSERT INTO contracts(company_id, contract_name)
      VALUES (p_company_id, p_contract_name);
  END;
  /
CREATE OR REPLACE PROCEDURE add_contract_by_c_name(p_company_name IN VARCHAR, p_contract_name IN VARCHAR) IS
  BEGIN
    
    INSERT INTO contracts(company_id, contract_name)
      VALUES (
        (SELECT company_id FROM companies WHERE company_name=p_company_name)
        , p_contract_name);
  END;
  /
  
CREATE OR REPLACE PROCEDURE add_process(p_contract_id IN NUMBER, p_process_name IN VARCHAR) IS
  BEGIN
    INSERT INTO processes(contract_id, process_name)
      VALUES (p_contract_id, p_process_name);
  END;
  /
  
CREATE OR REPLACE FUNCTION get_prev_task_id(p_task_id IN NUMBER, p_process_id IN NUMBER)
  RETURN NUMBER IS
    v_res NUMBER;
  BEGIN
    SELECT task_id INTO v_res
      FROM tasks NATURAL JOIN tasks_order
      WHERE tasks.process_id=p_process_id AND task_id NOT IN (SELECT NVL(prev_id, -1) FROM tasks_order);
    RETURN v_res;
  EXCEPTION
      WHEN NO_DATA_FOUND THEN
        RETURN NULL;
  END;
  /
CREATE OR REPLACE PROCEDURE add_task(p_process_id IN NUMBER, p_task_name IN VARCHAR, p_executor_id IN NUMBER) IS
    v_prev_id NUMBER;
  BEGIN
    
    INSERT INTO tasks(process_id, task_name, executor_id)
      VALUES(p_process_id, p_task_name, p_executor_id);
      
    INSERT INTO timeline(task_id, NEW_STATUS_ID) VALUES (task_id_sequence.currval, 0);
        
    INSERT INTO tasks_order(task_id, prev_id)
      VALUES(task_id_sequence.currval, get_prev_task_id(task_id_sequence.currval, p_process_id));
  END;
  /

CREATE OR REPLACE PROCEDURE update_contract_text(p_contract_id IN NUMBER, p_text IN CHAR) IS
  BEGIN
    UPDATE contracts SET
      text=p_text 
      WHERE contract_id=p_contract_id;
  END;
  /
  
CREATE OR REPLACE PROCEDURE change_executor(p_e_id IN NUMBER, p_task_id IN NUMBER) IS
  BEGIN
    UPDATE tasks SET
      executor_id=p_e_id 
      WHERE task_id=p_task_id;
  END;
  /

CREATE OR REPLACE PROCEDURE proceed_task_status(p_task_id IN NUMBER) IS
    v_curr_status NUMBER;
  BEGIN
    SELECT new_status_id INTO v_curr_status
      FROM timeline
      WHERE task_id=p_task_id AND ROWNUM<1
      ORDER BY modified;
      
    INSERT INTO timeline(task_id, new_status_id)
      VALUES(p_task_id, v_curr_status+1);
      
    IF v_curr_status IN (SELECT status_is FROM statuses WHERE ROWNUM<1 ORDER BY status_id DESC)
      THEN
        DBMS_OUT.PUT('WOW');
    END IF;
  END;
  /
  
  
  CREATE OR REPLACE PROCEDURE proceed_task_status(p_task_id IN NUMBER) IS
    v_curr_status NUMBER;
    v_has_more_cnt NUMBER;
  BEGIN
    DBMS_OUTPUT.PUT_LINE('TRYING TO PROCEED '||p_task_id);
    SELECT  max(new_status_id) INTO v_curr_status
      FROM timeline
      WHERE task_id=p_task_id;
      
    DBMS_OUTPUT.PUT_LINE('TRYING TO PROCEED '||v_curr_status);
    
    INSERT INTO timeline(task_id, new_status_id)
      VALUES(p_task_id, v_curr_status+1);
      
    DBMS_OUTPUT.PUT_LINE('PROCEEDED '||p_task_id);
    SELECT COUNT(*) 
      INTO v_has_more_cnt
      FROM statuses
      WHERE status_id=v_curr_status+2;
    
    IF  v_has_more_cnt=0 THEN 
        DECLARE v_next_id NUMBER;
      BEGIN
        -- select next task, if exists
        DBMS_OUTPUT.PUT_LINE('WOW');
        SELECT task_id INTO v_next_id FROM tasks_order WHERE prev_id=p_task_id;
        proceed_task_status(v_next_id);
--        SELECT 
        EXCEPTION WHEN NO_DATA_FOUND THEN DBMS_OUTPUT.PUT_LINE('No next task, exiting');
      END;
    END IF;
  END;
  /