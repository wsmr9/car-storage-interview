USE car;

INSERT INTO public.car (brand, model, year, price, created_at)
VALUES 
    ('Toyota', 'Corolla', 2020, 20000, NOW()),
    ('Honda', 'Civic', 2021, 22000, NOW()),
    ('Ford', 'Mustang', 2022, 26000, NOW()),
    ('Chevrolet', 'Camaro', 2021, 25000, NOW()),
    ('Nissan', 'Sentra', 2019, 18000, NOW());
