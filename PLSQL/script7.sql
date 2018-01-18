SET SERVEROUTPUT ON; 

DECLARE

	CURSOR c1 IS	--c1 es el nombre que le vamos a dar al cursor
		SELECT employee_id, commission_pct
		FROM employees;

	v_employee_id employees.employee_id%TYPE;
	v_commission_pct employees.commission_pct%TYPE;


BEGIN
	
	OPEN c1;

		LOOP
			FETCH c1 INTO v_employee_id, v_commission_pct;
			EXIT WHEN c1%NOTFOUND;

			DBMS_OUTPUT.PUT_LINE (v_employee_id || '-----' || v_commission_pct);
		END LOOP;

	CLOSE c1;


END;
/
SET SERVEROUTPUT ON;