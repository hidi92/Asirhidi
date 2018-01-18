SET SERVEROUTPUT ON; 

DECLARE
	contador NUMBER(3) := 0;

BEGIN
	
	WHILE contador <= 100 LOOP 
		DBMS_OUTPUT.PUT_LINE ('Hola Steven');
		contador := contador +1;
	END LOOP;
	
END;
/
SET SERVEROUTPUT ON;