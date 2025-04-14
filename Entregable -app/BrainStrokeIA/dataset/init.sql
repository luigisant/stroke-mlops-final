-- Crear la tabla stroke_data
CREATE TABLE IF NOT EXISTS stroke_data (
    id INT,
    gender VARCHAR(10),
    age FLOAT,
    hypertension INT,
    heart_disease INT,
    ever_married VARCHAR(5),
    work_type VARCHAR(20),
    residence_type VARCHAR(10),
    avg_glucose_level FLOAT,
    bmi FLOAT, -- Mantener FLOAT
    smoking_status VARCHAR(20),
    stroke INT
);

-- Cargar datos y manejar valores inválidos
COPY stroke_data (id, gender, age, hypertension, heart_disease, ever_married, work_type, residence_type, avg_glucose_level, bmi, smoking_status, stroke)
FROM '/docker-entrypoint-initdb.d/healthcare-dataset-stroke-data.csv'
DELIMITER ','
CSV HEADER
NULL 'N/A'; -- Interpretar "N/A" como NULL