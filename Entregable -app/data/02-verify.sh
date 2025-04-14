#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    -- Verificar que la tabla se creó correctamente
    SELECT 'Verificando tabla stroke_data:' as message;
    SELECT COUNT(*) as total_records FROM stroke_data;
    
    -- Mostrar estructura de la tabla con el nuevo campo stroke_predict
    SELECT column_name, data_type 
    FROM information_schema.columns 
    WHERE table_name = 'stroke_data' 
    ORDER BY ordinal_position;
EOSQL