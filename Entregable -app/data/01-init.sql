-- Crear la tabla para los datos de stroke
CREATE TABLE IF NOT EXISTS stroke_data (
    id INT (50),
    gender VARCHAR(10),
    age INT (3),
    hypertension INT (1),
    heart_disease INT (1),
    ever_married VARCHAR(5),
    work_type VARCHAR(20),
    Residence_type VARCHAR(10),
    avg_glucose_level NUMERIC ,
    bmi NUMERIC,
    smoking_status VARCHAR(20),
    stroke INT (1) -- variable a predict
    --stroke_predict INTEGER DEFAULT NULL - no almaceno el predict
);

-- Copiar datos del CSV a la tabla
COPY stroke_data(id, gender, age, hypertension, heart_disease, ever_married, work_type, Residence_type, avg_glucose_level, bmi, smoking_status, stroke)
FROM './data/healthcaredatasetstrokedata.csv' 
DELIMITER ',' 
CSV HEADER;