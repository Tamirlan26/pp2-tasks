
CREATE OR REPLACE PROCEDURE upsert_user(p_name TEXT, p_phone TEXT)
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
        UPDATE phonebook
        SET phone = p_phone
        WHERE name = p_name;
    ELSE
        INSERT INTO phonebook(name, phone)
        VALUES (p_name, p_phone);
    END IF;
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE PROCEDURE insert_many_users(
    names TEXT[],
    phones TEXT[]
)
AS $$
DECLARE
    i INT;
    invalid_data TEXT[] := '{}';
BEGIN
    FOR i IN 1..array_length(names, 1) LOOP

        
        IF phones[i] ~ '^[0-9]+$' AND length(phones[i]) >= 5 THEN

            IF EXISTS (SELECT 1 FROM phonebook WHERE name = names[i]) THEN
                UPDATE phonebook
                SET phone = phones[i]
                WHERE name = names[i];
            ELSE
                INSERT INTO phonebook(name, phone)
                VALUES (names[i], phones[i]);
            END IF;

        ELSE
            invalid_data := array_append(invalid_data, names[i] || ':' || phones[i]);
        END IF;

    END LOOP;

    RAISE NOTICE 'Invalid data: %', invalid_data;
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE PROCEDURE delete_user(p_value TEXT)
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE name = p_value OR phone = p_value;
END;
$$ LANGUAGE plpgsql;