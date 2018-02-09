SET SERVEROUTPUT ON;

CREATE OR REPLACE PROCEDURE insert_new_job
(v_job_id IN VARCHAR2, v_job_title IN VARCHAR2, v_max IN NUMBER, v_min IN NUMBER)
IS
	v_temp_job_id NUMBER(3);

BEGIN
	
	v_temp_job_id :=0;
	
	SELECT COUNT (job_id)
	INTO v_temp_job_id
	FROM jobs
	WHERE job_id=v_job_id;
	
	IF v_temp_job_id = 0 THEN
		INSERT INTO jobs VALUES (v_job_id, v_job_title, v_max, v_min);
		ELSE
		DBMS_OUTPUT.PUT_LINE('El identificador ya existe');
		END IF;

END
/