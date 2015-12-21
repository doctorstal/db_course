@"clean_up.sql"
-- companies
CREATE TABLE companies(
  company_id NUMBER CONSTRAINT company_id_pk PRIMARY KEY,
  company_name VARCHAR(30) UNIQUE
    CONSTRAINT company_name_not_null NOT NULL
);

COMMENT ON TABLE companies IS 'This table contains company names';
COMMENT ON COLUMN companies.company_name IS 'Name of the company';

CREATE SEQUENCE company_id_sequence
  START WITH 1
  INCREMENT BY 1 MAXVALUE 150000 CYCLE;
  
CREATE OR REPLACE TRIGGER companies_trg
   BEFORE INSERT ON companies 
  FOR EACH ROW 
  BEGIN
    :NEW.company_id := company_id_sequence.nextval;
  END;
/

-- contracts
CREATE TABLE contracts(
  contract_id NUMBER PRIMARY KEY,
  company_id NUMBER,
  contract_name VARCHAR(30),
  text CHAR(2000),
  CONSTRAINT c_company_id_fk FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE SET NULL
);

COMMENT ON COLUMN contracts.contract_name IS 'Short name of contract';
COMMENT ON COLUMN contracts.text IS 'Full description';

CREATE SEQUENCE contract_id_sequence
  START WITH 1
  INCREMENT BY 1 MAXVALUE 1000000 NOCYCLE;
  
CREATE OR REPLACE TRIGGER contracts_trg
   BEFORE INSERT ON contracts 
  FOR EACH ROW 
  BEGIN
    :NEW.contract_id := contract_id_sequence.nextval;
  END;
/

-- Business processes
CREATE TABLE processes(
  process_id NUMBER PRIMARY KEY,
  contract_id NUMBER,
  process_name VARCHAR(30),
  CONSTRAINT p_contract_id_fk FOREIGN KEY (contract_id) REFERENCES contracts ON DELETE SET NULL
);

CREATE SEQUENCE process_id_sequence
  START WITH 1
  INCREMENT BY 1 MAXVALUE 1000000 NOCYCLE;
  
CREATE OR REPLACE TRIGGER process_trg
   BEFORE INSERT ON processes 
  FOR EACH ROW 
  BEGIN
    :NEW.process_id := process_id_sequence.nextval;
  END;
/

-- executors
CREATE TABLE executors(
  executor_id NUMBER PRIMARY KEY,
  executor_name VARCHAR(30) UNIQUE
);

CREATE SEQUENCE executor_id_sequence
  START WITH 1
  INCREMENT BY 1 MAXVALUE 1000000 NOCYCLE;
  
CREATE OR REPLACE TRIGGER executors_trg
   BEFORE INSERT ON executors 
  FOR EACH ROW 
  BEGIN
    :NEW.executor_id := executor_id_sequence.nextval;
  END;
/

-- tasks
CREATE TABLE tasks(
  task_id NUMBER PRIMARY KEY,
  process_id NUMBER,
  executor_id NUMBER,
  task_name VARCHAR(30),
  CONSTRAINT t_process_id_fk FOREIGN KEY (process_id) REFERENCES processes ON DELETE SET NULL,
  CONSTRAINT t_executor_id_fk FOREIGN KEY (executor_id) REFERENCES executors ON DELETE SET NULL
);

CREATE SEQUENCE task_id_sequence
  START WITH 1
  INCREMENT BY 1 MAXVALUE 1000000 NOCYCLE;
  
CREATE OR REPLACE TRIGGER tasks_trg
   BEFORE INSERT ON tasks 
  FOR EACH ROW 
  BEGIN
    :NEW.task_id := task_id_sequence.nextval;
  END;
/



CREATE TABLE statuses
(
  status_id NUMBER PRIMARY KEY,
  status_name VARCHAR(50)
);

INSERT INTO statuses VALUES ('0', 'New');
INSERT INTO statuses VALUES ('1', 'Working');
INSERT INTO statuses VALUES ('2', 'Done');

CREATE OR REPLACE TRIGGER statuses_lock
  BEFORE INSERT OR DELETE ON statuses
  BEGIN
     RAISE_APPLICATION_ERROR (-20500,
             'Statuses is locked due to business logic of the product.');
  END;
/


CREATE TABLE timeline(
  code NUMBER PRIMARY KEY,
  task_id NUMBER,
  modified DATE DEFAULT SYSDATE,
  new_status_id NUMBER,
  CONSTRAINT tl_new_s_id_fk FOREIGN KEY (new_status_id) REFERENCES statuses(status_id),
  CONSTRAINT tl_task_id_fk FOREIGN KEY (task_id) REFERENCES tasks(task_id) 
);



CREATE SEQUENCE timeline_code_sequence
  START WITH 1
  INCREMENT BY 1 MAXVALUE 1000000 NOCYCLE;

CREATE OR REPLACE TRIGGER timeline_trg
   BEFORE INSERT ON timeline 
  FOR EACH ROW 
  BEGIN
    :NEW.code := timeline_code_sequence.nextval;
  END;
/

CREATE TABLE tasks_order(
  task_id NUMBER UNIQUE,
  prev_id NUMBER UNIQUE,
  CONSTRAINT to_task_id_fk FOREIGN KEY (task_id) REFERENCES tasks(task_id),
  CONSTRAINT to_next_id_fk FOREIGN KEY (prev_id) REFERENCES tasks(task_id)
);

@"views.sql"
@"procedures.sql"
-- Uncomment to fill empty data
--@"insert.sql"
