CREATE OR REPLACE PROCEDURE incrementa_salario
( 
 v_idEmp IN employees.employee_id%TYPE,
 v_porcentaje IN NUMBER
 v_name OUT employees.last_name%TYPE
 )
IS
BEGIN
	UPDATE employees
	SET SALARY=SALARY*v_porcentaje
	WHERE employee_id = v_idEmp;

	SELECT last_name
	INTO v_name
	FROM employees
	WHERE employee_id = v_idEmp;

END;
/