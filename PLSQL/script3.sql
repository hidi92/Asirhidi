SET SERVEROUTPUT ON; 

DECLARE
	contador NUMBER(3) := 0;

BEGIN
	
	LOOP 
		DBMS_OUTPUT.PUT_LINE ('Hola Steven');
		IF contador = 100 THEN
			EXIT;
		END IF;
		contador := contador +1;

	END LOOP;
	
END;
/
SET SERVEROUTPUT ON;