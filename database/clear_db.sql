DO $$ DECLARE
    table_row record;
BEGIN
    FOR table_row IN (SELECT table_name FROM information_schema.tables WHERE table_schema = 'public') LOOP
        EXECUTE 'DROP TABLE IF EXISTS ' || table_row.table_name || ' CASCADE';
    END LOOP;
END $$;
