SET SERVEROUTPUT ON;   --Permite mostrar daton por pantalla
DECLARE
	v_sal NUMBER(8,2);
	pi CONSTANT NUMBER (10,9) := 3.1415927;	--Crear una constante llamada pi con el valor de pi
	v_name employees.first_name%TYPE;	--Crear una variable que sea del mismo tipo que el campo first_name de la tabla employees
BEGIN
	v_name := 'Pepito Fernandez';
	SELECT SALARY*1.10 
	INTO v_sal
	FROM employees
	WHERE employee_id=100;
	
	DBMS_OUTPUT.PUT_LINE('El resultado es: ' || v_sal || ' para ' || v_name);	--para manejar la salida de datos en oracle(como print en otros lenguajes)
	
END;
		--/ Es para decir que es el final del comando
/
