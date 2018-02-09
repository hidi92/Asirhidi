SET SERVEROUTPUT ON; 

DECLARE
	v_fist_name employees.first_name%TYPE;

BEGIN
	SELECT	first_name
	INTO v_fist_name
	FROM employees
	WHERE employee_id='100';
	
	IF v_fist_name = 'Steven' THEN 
		DBMS_OUTPUT.PUT_LINE ('Hola Steven');
	ELSIF v_fist_name = 'Pepito' THEN
		DBMS_OUTPUT.PUT_LINE ('Hola Pepito');
	ELSE
		DBMS_OUTPUT.PUT_LINE ('Hola Majete');
	END IF;
END;
/
SET SERVEROUTPUT ON;