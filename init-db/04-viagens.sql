-- Definindo as viagens
INSERT INTO Viagem (Nome, Descricao, Clima, Preco, Companhia) VALUES 
('Praia de Copacabana', 'Famosa praia do Rio de Janeiro com paisagens deslumbrantes', 'quente', 'medio', 'amigos'),
('Ski nos Alpes Suíços', 'Esqui nas montanhas nevadas dos Alpes', 'frio', 'alto', 'amigos'),
('Disney World Orlando', 'Parque temático para toda família', 'quente', 'alto', 'familia'),
('Romance em Paris', 'Cidade luz ideal para casais', 'temperado', 'medio', 'casal'),
('Mochilão Europa Econômico', 'Roteiro econômico por capitais europeias', 'temperado', 'economico', 'sozinho'),
('Resort Maldivas', 'Ilhas paradisíacas com águas cristalinas', 'tropical', 'luxo', 'casal'),
('Ecovila Amazônica', 'Imersão na floresta amazônica', 'tropical', 'economico', 'sozinho'),
('Campos do Jordão Inverno', 'Cidade romântica no inverno brasileiro', 'frio', 'medio', 'casal'),
('Cancún All Inclusive', 'Resort tudo incluído no Caribe', 'tropical', 'alto', 'amigos'),
('Tour Histórico Roma', 'Conheça o Coliseu e monumentos históricos', 'temperado', 'medio', 'familia'),
('Fernando de Noronha', 'Paraíso ecológico brasileiro', 'tropical', 'luxo', 'casal'),
('Las Vegas Nights', 'Cassinos e entretenimento 24h', 'quente', 'alto', 'amigos'),
('Machu Picchu Trekking', 'Trilha inca até as ruínas perdidas', 'temperado', 'economico', 'sozinho'),
('Safári África do Sul', 'Observação de animais selvagens', 'quente', 'luxo', 'familia'),
('Patagônia Argentina', 'Aventura nos glaciares', 'frio', 'medio', 'amigos'),
('Bali Spiritual Retreat', 'Yoga e meditação em templos', 'tropical', 'medio', 'sozinho'),
('New York City Tour', 'Compras e cultura na cidade que nunca dorme', 'temperado', 'alto', 'amigos'),
('Gramado Natal Luz', 'Natal mágico na serra gaúcha', 'frio', 'medio', 'familia'),
('Ilhas Gregas', 'Navegação pelas ilhas do mediterrâneo', 'quente', 'alto', 'casal'),
('Jericoacoara Aventura', 'Dunas e lagoas no nordeste brasileiro', 'quente', 'economico', 'amigos');


-- =============================================================================
-- Genero da viagem
-- =============================================================================

INSERT INTO GeneroViagem (ViagemId, GeneroId, Intensidade) VALUES 

-- VIAGEM 1: Praia de Copacabana 
(1, 2, 4), (1, 7, 5), (1, 5, 3), (1, 3, 3),  -- Aventura, Ecoturismo, Cultural, Relaxamento

-- VIAGEM 2: Ski nos Alpes Suíços 
(2, 2, 5), (2, 7, 4), (2, 4, 3), (2, 5, 3),  -- Aventura, Ecoturismo, Histórico, Cultural

-- VIAGEM 3: Disney World Orlando 
(3, 5, 4), (3, 6, 4), (3, 1, 3), (3, 3, 3),  -- Cultural, Gastronômico, Romance, Relaxamento

-- VIAGEM 4: Romance em Paris 
(4, 1, 5), (4, 5, 4), (4, 6, 5), (4, 3, 3),  -- Romance, Cultural, Gastronômico, Relaxamento

-- VIAGEM 5: Mochilão Europa Econômico 
(5, 5, 5), (5, 2, 3), (5, 7, 3), (5, 4, 4),  -- Cultural, Aventura, Ecoturismo, Histórico

-- VIAGEM 6: Resort Maldivas 
(6, 1, 5), (6, 3, 5), (6, 7, 3), (6, 2, 3),  -- Romance, Relaxamento, Ecoturismo, Aventura

-- VIAGEM 7: Ecovila Amazônica 
(7, 7, 5), (7, 3, 4), (7, 2, 3), (7, 4, 3),  -- Ecoturismo, Relaxamento, Aventura, Histórico

-- VIAGEM 8: Campos do Jordão Inverno 
(8, 1, 4), (8, 3, 4), (8, 5, 3), (8, 7, 3),  -- Romance, Relaxamento, Cultural, Ecoturismo

-- VIAGEM 9: Cancún All Inclusive 
(9, 3, 5), (9, 1, 4), (9, 7, 4), (9, 2, 3),  -- Relaxamento, Romance, Ecoturismo, Aventura

-- VIAGEM 10: Tour Histórico Roma 
(10, 4, 5), (10, 5, 5), (10, 6, 4), (10, 1, 3),  -- Histórico, Cultural, Gastronômico, Romance

-- VIAGEM 11: Fernando de Noronha 
(11, 7, 5), (11, 2, 4), (11, 3, 5), (11, 5, 3),  -- Ecoturismo, Aventura, Relaxamento, Cultural

-- VIAGEM 12: Las Vegas Nights 
(12, 6, 5), (12, 4, 4), (12, 2, 3), (12, 5, 3),  -- Gastronômico, Histórico, Aventura, Cultural

-- VIAGEM 13: Machu Picchu Trekking 
(13, 2, 5), (13, 4, 4), (13, 7, 4), (13, 5, 3),  -- Aventura, Histórico, Ecoturismo, Cultural

-- VIAGEM 14: Safári África do Sul 
(14, 2, 5), (14, 7, 5), (14, 4, 3), (14, 5, 3),  -- Aventura, Ecoturismo, Histórico, Cultural

-- VIAGEM 15: Patagônia Argentina 
(15, 2, 5), (15, 7, 4), (15, 4, 3), (15, 5, 3),  -- Aventura, Ecoturismo, Histórico, Cultural

-- VIAGEM 16: Bali Spiritual Retreat 
(16, 3, 5), (16, 5, 4), (16, 7, 3), (16, 4, 3),  -- Relaxamento, Cultural, Ecoturismo, Histórico

-- VIAGEM 17: New York City Tour 
(17, 4, 5), (17, 6, 4), (17, 5, 3), (17, 2, 3),  -- Histórico, Gastronômico, Cultural, Aventura

-- VIAGEM 18: Gramado Natal Luz 
(18, 1, 4), (18, 5, 4), (18, 3, 3), (18, 7, 3),  -- Romance, Cultural, Relaxamento, Ecoturismo

-- VIAGEM 19: Ilhas Gregas 
(19, 1, 5), (19, 5, 4), (19, 7, 3), (19, 3, 3),  -- Romance, Cultural, Ecoturismo, Relaxamento

-- VIAGEM 20: Jericoacoara Aventura 
(20, 2, 4), (20, 7, 4), (20, 3, 4), (20, 5, 3);  -- Aventura, Ecoturismo, Relaxamento, Cultural

-- =============================================================================
-- Lazer da viagem
-- =============================================================================

INSERT INTO LazerViagem (ViagemId, LazerId, Qualidade) VALUES 

-- VIAGEM 1: Praia de Copacabana 
(1, 1, 5), (1, 5, 4),  -- Praia, Radical

-- VIAGEM 2: Ski nos Alpes Suíços 
(2, 5, 5), (2, 7, 4),  -- Radical, Natureza

-- VIAGEM 3: Disney World Orlando 
(3, 4, 4), (3, 2, 3), (3, 3, 5),  -- Compras, Piscina, Fotografia

-- VIAGEM 4: Romance em Paris 
(4, 4, 4), (4, 6, 5), (4, 3, 4),  -- Compras, Vida Noturna, Fotografia

-- VIAGEM 5: Mochilão Europa Econômico 
(5, 3, 4), (5, 4, 3),  -- Fotografia, Compras

-- VIAGEM 6: Resort Maldivas 
(6, 1, 5), (6, 2, 5),  -- Praia, Piscina

-- VIAGEM 7: Ecovila Amazônica 
(7, 7, 5), (7, 5, 4),  -- Natureza, Radical

-- VIAGEM 8: Campos do Jordão Inverno 
(8, 7, 4), (8, 4, 3), (8, 3, 3),  -- Natureza, Compras, Fotografia

-- VIAGEM 9: Cancún All Inclusive 
(9, 1, 5), (9, 2, 5), (9, 5, 3),  -- Praia, Piscina, Radical

-- VIAGEM 10: Tour Histórico Roma 
(10, 3, 4), (10, 4, 3),  -- Fotografia, Compras

-- VIAGEM 11: Fernando de Noronha 
(11, 1, 5), (11, 3, 4), (11, 5, 3),  -- Praia, Fotografia, Radical

-- VIAGEM 12: Las Vegas Nights 
(12, 4, 5), (12, 2, 3), (12, 6, 5),  -- Compras, Piscina, Vida Noturna

-- VIAGEM 13: Machu Picchu Trekking 
(13, 7, 5), (13, 5, 3), (13, 3, 4),  -- Natureza, Radical, Fotografia

-- VIAGEM 14: Safári África do Sul 
(14, 7, 4), (14, 5, 3),  -- Natureza, Radical

-- VIAGEM 15: Patagônia Argentina 
(15, 7, 4), (15, 5, 3), (15, 3, 3),  -- Natureza, Radical, Fotografia

-- VIAGEM 16: Bali Spiritual Retreat 
(16, 2, 4), (16, 3, 3), (16, 7, 3),  -- Piscina, Fotografia, Natureza

-- VIAGEM 17: New York City Tour 
(17, 4, 5), (17, 6, 5),  -- Compras, Vida Noturna

-- VIAGEM 18: Gramado Natal Luz 
(18, 4, 4), (18, 3, 3),  -- Compras, Fotografia

-- VIAGEM 19: Ilhas Gregas 
(19, 1, 4), (19, 3, 4), (19, 2, 3),  -- Praia, Fotografia, Piscina

-- VIAGEM 20: Jericoacoara Aventura 
(20, 1, 4), (20, 3, 4), (20, 5, 4);  -- Praia, Fotografia, Radical
