-- Ensure you are in the correct database
-- You can change "car" to your database name if it's different
-- Comment or remove the line below if you are already in the right database
-- \c car

-- Create the 'car' table if it does not exist
CREATE TABLE IF NOT EXISTS public.car (
    id SERIAL PRIMARY KEY,  -- Auto-incremental ID, primary key
    brand VARCHAR(255) NOT NULL,  -- Brand of the car
    model VARCHAR(255) NOT NULL,  -- Model of the car
    year INT NOT NULL,  -- Year of the car model
    price DECIMAL NOT NULL,  -- Price of the car
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW()  -- Timestamp of record creation, defaults to current time
);

-- Insert data into the 'car' table
INSERT INTO public.car (brand, model, year, price, created_at)
VALUES 
    ('Toyota', 'Corolla', 2020, 20000, NOW()),
    ('Honda', 'Civic', 2021, 22000, NOW()),
    ('Ford', 'Mustang', 2022, 26000, NOW()),
    ('Chevrolet', 'Camaro', 2021, 25000, NOW()),
    ('Nissan', 'Sentra', 2019, 18000, NOW());

-- Verify that the data has been inserted correctly
SELECT * FROM public.car;
