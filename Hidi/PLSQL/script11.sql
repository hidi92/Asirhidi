-- Creamos una variable global llamada g_phone_number
-- SQL>  VARIABLE g_phone_number VARCHAR2(50);
--
-- Asignamos valor a la variable global, a través de un bloque PL/SQL
--
-- SQL> BEGIN
-- SQL>		:g_phone_number := '924676787';
-- SQL> END;
-- SQL> /
--
--
-- Ejecutamos el procedimiento pasando la variable IN OUT que modificará su valor
-- De entrada por un nuevo valor de salida que aignará.
-- 
-- SQL> EXECUTE format_phone(:g_phone_number);
-- 
-- Para ver el valor modificado:
-- 
-- SQL> print :g_phone_number;
-- y mostrará como resultado:

-- G_PHONE_NUMBER
--------------------------------------------------------------------------------
-- (+34)924-676-787


CREATE OR REPLACE PROCEDURE format_phone
(v_phone_number IN OUT VARCHAR2)
IS
BEGIN
	
	v_phone_number := '(+34)' ||
	SUBSTR(v_phone_number,1,3) || '-' ||
	SUBSTR(v_phone_number,4,3) || '-' ||
	SUBSTR(v_phone_number,7);
	
END;
/