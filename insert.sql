
BEGIN
  add_executor('Stadnyk');
  add_executor('Koval');
  add_executor('Pupkin');
  
  -- PLAYTECH
  add_company('Playtech');
  add_contract(company_id_sequence.currval, 'Do something');
  add_process(contract_id_sequence.currval, 'Create tasks for people');
  add_task(process_id_sequence.currval, 'Create first task', get_executor_id('Stadnyk'));
  add_task(process_id_sequence.currval, 'Create second task', get_executor_id('Koval'));
  
  add_process(contract_id_sequence.currval, 'Actually do tasks');
  add_task(process_id_sequence.currval, 'Do first task', get_executor_id('Pupkin'));
  add_task(process_id_sequence.currval, 'Do second task', get_executor_id('Pupkin'));
  
  add_contract(company_id_sequence.currval, 'Do something more');
  add_process(contract_id_sequence.currval, 'Tell we wont do');
  add_task(process_id_sequence.currval, 'Send some mails', get_executor_id('Koval'));
  add_task(process_id_sequence.currval, 'Read replies', get_executor_id('Stadnyk'));
  add_task(process_id_sequence.currval, 'Make a call', get_executor_id('Stadnyk'));
  
  -- PAUSETECH
  add_company('Pausetech');
  
  add_contract(company_id_sequence.currval, 'Have a rest');
  add_contract(company_id_sequence.currval, 'Watch a movie');
  add_contract(company_id_sequence.currval, 'Have a nap');
  
  add_company('IT Monsters');
  
  add_contract(company_id_sequence.currval, 'ERP System For Monsters');
  add_contract(company_id_sequence.currval, 'Support ERP');
  
  add_company('New and young');
  
END;
/

