-- Usuarios
INSERT INTO Usuario (Nome, Email, Senha) VALUES 
('Usuario1', 'usuario1@email.com', 'senha123'),
('Usuario2', 'usuario2@email.com', 'senha123'),
('Usuario3', 'usuario3@email.com', 'senha123'),
('Usuario4', 'usuario4@email.com', 'senha123'),
('Usuario5', 'usuario5@email.com', 'senha123'),
('Usuario6', 'usuario6@email.com', 'senha123'),
('Usuario7', 'usuario7@email.com', 'senha123'),
('Usuario8', 'usuario8@email.com', 'senha123'),
('Usuario9', 'usuario9@email.com', 'senha123'),
('Usuario10', 'usuario10@email.com', 'senha123'),
('Usuario11', 'usuario11@email.com', 'senha123'),
('Usuario12', 'usuario12@email.com', 'senha123'),
('Usuario13', 'usuario13@email.com', 'senha123'),
('Usuario14', 'usuario14@email.com', 'senha123'),
('Usuario15', 'usuario15@email.com', 'senha123'),
('Usuario16', 'usuario16@email.com', 'senha123'),
('Usuario17', 'usuario17@email.com', 'senha123'),
('Usuario18', 'usuario18@email.com', 'senha123'),
('Usuario19', 'usuario19@email.com', 'senha123'),
('Usuario20', 'usuario20@email.com', 'senha123'),
('Usuario21', 'usuario21@email.com', 'senha123'),
('Usuario22', 'usuario22@email.com', 'senha123'),
('Usuario23', 'usuario23@email.com', 'senha123'),
('Usuario24', 'usuario24@email.com', 'senha123'),
('Usuario25', 'usuario25@email.com', 'senha123'),
('Usuario26', 'usuario26@email.com', 'senha123'),
('Usuario27', 'usuario27@email.com', 'senha123'),
('Usuario28', 'usuario28@email.com', 'senha123'),
('Usuario29', 'usuario29@email.com', 'senha123'),
('Usuario30', 'usuario30@email.com', 'senha123'),
('Usuario31', 'usuario31@email.com', 'senha123'),
('Usuario32', 'usuario32@email.com', 'senha123'),
('Usuario33', 'usuario33@email.com', 'senha123'),
('Usuario34', 'usuario34@email.com', 'senha123'),
('Usuario35', 'usuario35@email.com', 'senha123'),
('Usuario36', 'usuario36@email.com', 'senha123'),
('Usuario37', 'usuario37@email.com', 'senha123'),
('Usuario38', 'usuario38@email.com', 'senha123'),
('Usuario39', 'usuario39@email.com', 'senha123'),
('Usuario40', 'usuario40@email.com', 'senha123'),
('Usuario41', 'usuario41@email.com', 'senha123'),
('Usuario42', 'usuario42@email.com', 'senha123'),
('Usuario43', 'usuario43@email.com', 'senha123'),
('Usuario44', 'usuario44@email.com', 'senha123'),
('Usuario45', 'usuario45@email.com', 'senha123'),
('Usuario46', 'usuario46@email.com', 'senha123'),
('Usuario47', 'usuario47@email.com', 'senha123'),
('Usuario48', 'usuario48@email.com', 'senha123'),
('Usuario49', 'usuario49@email.com', 'senha123'),
('Usuario50', 'usuario50@email.com', 'senha123');

-- =============================================================================
-- PREFERÊNCIAS DOS USUÁRIOS 
-- =============================================================================

INSERT INTO Preferencias (UsuarioId, Clima, Preco, Companhia) VALUES 
-- Usuários 1-10: Perfil Aventura/Amigos
(1, 'quente', 'medio', 'amigos'),
(2, 'tropical', 'economico', 'amigos'),
(3, 'quente', 'alto', 'amigos'),
(4, 'tropical', 'medio', 'amigos'),
(5, 'quente', 'economico', 'amigos'),

-- Usuários 6-15: Perfil Romance/Casal
(6, 'temperado', 'alto', 'casal'),
(7, 'tropical', 'luxo', 'casal'),
(8, 'frio', 'medio', 'casal'),
(9, 'temperado', 'luxo', 'casal'),
(10, 'frio', 'alto', 'casal'),

-- Usuários 11-20: Perfil Familiar
(11, 'temperado', 'medio', 'familia'),
(12, 'quente', 'economico', 'familia'),
(13, 'tropical', 'medio', 'familia'),
(14, 'temperado', 'alto', 'familia'),
(15, 'quente', 'medio', 'familia'),

-- Usuários 21-30: Perfil Sozinho/Aventura
(16, 'frio', 'economico', 'sozinho'),
(17, 'temperado', 'economico', 'sozinho'),
(18, 'tropical', 'medio', 'sozinho'),
(19, 'quente', 'economico', 'sozinho'),
(20, 'frio', 'medio', 'sozinho'),

-- Usuários 31-40: Mix diversos
(21, 'quente', 'luxo', 'amigos'),
(22, 'tropical', 'alto', 'casal'),
(23, 'temperado', 'medio', 'familia'),
(24, 'frio', 'economico', 'sozinho'),
(25, 'quente', 'alto', 'amigos'),
(26, 'tropical', 'medio', 'casal'),
(27, 'temperado', 'luxo', 'familia'),
(28, 'frio', 'alto', 'sozinho'),
(29, 'quente', 'economico', 'amigos'),
(30, 'tropical', 'medio', 'casal'),

-- Usuários 41-50: Completando os padrões
(31, 'temperado', 'alto', 'familia'),
(32, 'frio', 'medio', 'sozinho'),
(33, 'quente', 'luxo', 'amigos'),
(34, 'tropical', 'economico', 'casal'),
(35, 'temperado', 'medio', 'familia'),
(36, 'frio', 'alto', 'sozinho'),
(37, 'quente', 'medio', 'amigos'),
(38, 'tropical', 'luxo', 'casal'),
(39, 'temperado', 'economico', 'familia'),
(40, 'frio', 'medio', 'sozinho'),
(41, 'quente', 'alto', 'amigos'),
(42, 'tropical', 'medio', 'casal'),
(43, 'temperado', 'luxo', 'familia'),
(44, 'frio', 'economico', 'sozinho'),
(45, 'quente', 'medio', 'amigos'),
(46, 'tropical', 'alto', 'casal'),
(47, 'temperado', 'medio', 'familia'),
(48, 'frio', 'luxo', 'sozinho'),
(49, 'quente', 'economico', 'amigos'),
(50, 'tropical', 'medio', 'casal');

-- =============================================================================
-- GÊNEROS DOS USUARIOS
-- =============================================================================

INSERT INTO GeneroUsuario (UsuarioId, GeneroId, Preferencia) VALUES 
-- PERFIL AVENTURA (Usuários 1-10)
(1, 2, 5), (1, 7, 4), (1, 5, 3),  -- Aventura, Ecoturismo, Cultural
(2, 2, 5), (2, 7, 4), (2, 4, 3),  -- Aventura, Ecoturismo, Histórico
(3, 2, 4), (3, 7, 5), (3, 6, 3),  -- Aventura, Ecoturismo, Gastronômico
(4, 2, 5), (4, 5, 4), (4, 7, 3),  -- Aventura, Cultural, Ecoturismo
(5, 2, 4), (5, 7, 4), (5, 3, 3),  -- Aventura, Ecoturismo, Relaxamento

-- PERFIL ROMANCE (Usuários 6-15)
(6, 1, 5), (6, 3, 4), (6, 5, 3),  -- Romance, Relaxamento, Cultural
(7, 1, 5), (7, 3, 5), (7, 6, 3),  -- Romance, Relaxamento, Gastronômico
(8, 1, 4), (8, 3, 5), (8, 7, 3),  -- Romance, Relaxamento, Ecoturismo
(9, 1, 5), (9, 6, 4), (9, 5, 3),  -- Romance, Gastronômico, Cultural
(10, 1, 4), (10, 3, 5), (10, 5, 4), -- Romance, Relaxamento, Cultural

-- PERFIL FAMÍLIA (Usuários 11-20)
(11, 5, 5), (11, 3, 4), (11, 1, 3),  -- Cultural, Relaxamento, Romance
(12, 5, 4), (12, 7, 4), (12, 3, 3),  -- Cultural, Ecoturismo, Relaxamento
(13, 5, 5), (13, 6, 4), (13, 1, 3),  -- Cultural, Gastronômico, Romance
(14, 5, 4), (14, 4, 4), (14, 3, 3),  -- Cultural, Histórico, Relaxamento
(15, 5, 5), (15, 7, 3), (15, 6, 3),  -- Cultural, Ecoturismo, Gastronômico

-- PERFIL SOLITÁRIO/AVENTURA (Usuários 16-25)
(16, 2, 5), (16, 7, 4), (16, 4, 3),  -- Aventura, Ecoturismo, Histórico
(17, 2, 4), (17, 7, 5), (17, 5, 3),  -- Aventura, Ecoturismo, Cultural
(18, 7, 5), (18, 2, 4), (18, 3, 3),  -- Ecoturismo, Aventura, Relaxamento
(19, 2, 5), (19, 4, 4), (19, 7, 3),  -- Aventura, Histórico, Ecoturismo
(20, 7, 5), (20, 2, 4), (20, 5, 3),  -- Ecoturismo, Aventura, Cultural

-- USUÁRIOS 26-35 (Mix)
(21, 6, 5), (21, 1, 4), (21, 3, 3),  -- Gastronômico, Romance, Relaxamento
(22, 1, 5), (22, 6, 4), (22, 5, 3),  -- Romance, Gastronômico, Cultural
(23, 5, 5), (23, 3, 4), (23, 7, 3),  -- Cultural, Relaxamento, Ecoturismo
(24, 2, 5), (24, 7, 4), (24, 4, 3),  -- Aventura, Ecoturismo, Histórico
(25, 2, 4), (25, 6, 4), (25, 5, 3),  -- Aventura, Gastronômico, Cultural

-- USUÁRIOS 36-45 (Mix)
(26, 1, 5), (26, 5, 4), (26, 3, 3),  -- Romance, Cultural, Relaxamento
(27, 5, 5), (27, 6, 4), (27, 1, 3),  -- Cultural, Gastronômico, Romance
(28, 7, 5), (28, 2, 4), (28, 4, 3),  -- Ecoturismo, Aventura, Histórico
(29, 2, 5), (29, 7, 4), (29, 5, 3),  -- Aventura, Ecoturismo, Cultural
(30, 1, 4), (30, 3, 5), (30, 6, 3),  -- Romance, Relaxamento, Gastronômico

-- USUÁRIOS 46-50 (Completando)
(31, 5, 5), (31, 4, 4), (31, 3, 3),  -- Cultural, Histórico, Relaxamento
(32, 2, 5), (32, 7, 4), (32, 5, 3),  -- Aventura, Ecoturismo, Cultural
(33, 6, 5), (33, 1, 4), (33, 3, 3),  -- Gastronômico, Romance, Relaxamento
(34, 1, 5), (34, 5, 4), (34, 6, 3),  -- Romance, Cultural, Gastronômico
(35, 7, 5), (35, 2, 4), (35, 3, 3),  -- Ecoturismo, Aventura, Relaxamento
(36, 4, 5), (36, 5, 4), (36, 2, 3),  -- Histórico, Cultural, Aventura
(37, 2, 5), (37, 7, 4), (37, 6, 3),  -- Aventura, Ecoturismo, Gastronômico
(38, 1, 5), (38, 3, 4), (38, 6, 3),  -- Romance, Relaxamento, Gastronômico
(39, 5, 5), (39, 7, 4), (39, 3, 3),  -- Cultural, Ecoturismo, Relaxamento
(40, 2, 5), (40, 4, 4), (40, 7, 3),  -- Aventura, Histórico, Ecoturismo
(41, 6, 5), (41, 1, 4), (41, 5, 3),  -- Gastronômico, Romance, Cultural
(42, 1, 5), (42, 3, 4), (42, 5, 3),  -- Romance, Relaxamento, Cultural
(43, 5, 5), (43, 4, 4), (43, 6, 3),  -- Cultural, Histórico, Gastronômico
(44, 7, 5), (44, 2, 4), (44, 3, 3),  -- Ecoturismo, Aventura, Relaxamento
(45, 2, 5), (45, 5, 4), (45, 7, 3),  -- Aventura, Cultural, Ecoturismo
(46, 1, 5), (46, 6, 4), (46, 3, 3),  -- Romance, Gastronômico, Relaxamento
(47, 5, 5), (47, 3, 4), (47, 7, 3),  -- Cultural, Relaxamento, Ecoturismo
(48, 4, 5), (48, 2, 4), (48, 7, 3),  -- Histórico, Aventura, Ecoturismo
(49, 2, 5), (49, 7, 4), (49, 5, 3),  -- Aventura, Ecoturismo, Cultural
(50, 1, 5), (50, 3, 4), (50, 5, 3);  -- Romance, Relaxamento, Cultural

-- =============================================================================
-- LAZERES DOS USUÁRIOS
-- =============================================================================

INSERT INTO LazerUsuario (UsuarioId, LazerId, Intensidade) VALUES 
-- PERFIL AVENTURA/RADICAL (Usuários 1-10)
(1, 5, 5), (1, 3, 4), (1, 7, 3),  -- Radical, Fotografia, Natureza
(2, 5, 5), (2, 7, 4), (2, 3, 3),  -- Radical, Natureza, Fotografia
(3, 5, 4), (3, 1, 4), (3, 7, 3),  -- Radical, Praia, Natureza
(4, 5, 5), (4, 3, 4), (4, 1, 3),  -- Radical, Fotografia, Praia
(5, 5, 4), (5, 7, 4), (5, 3, 3),  -- Radical, Natureza, Fotografia

-- PERFIL ROMANCE/RELAXAMENTO (Usuários 6-15)
(6, 2, 5), (6, 3, 4), (6, 1, 3),  -- Piscina, Fotografia, Praia
(7, 2, 5), (7, 1, 4), (7, 3, 3),  -- Piscina, Praia, Fotografia
(8, 3, 5), (8, 2, 4), (8, 7, 3),  -- Fotografia, Piscina, Natureza
(9, 1, 5), (9, 2, 4), (9, 3, 3),  -- Praia, Piscina, Fotografia
(10, 2, 5), (10, 3, 4), (10, 6, 3), -- Piscina, Fotografia, Vida Noturna

-- PERFIL FAMÍLIA (Usuários 11-20)
(11, 4, 5), (11, 3, 4), (11, 1, 3),  -- Compras, Fotografia, Praia
(12, 1, 5), (12, 3, 4), (12, 7, 3),  -- Praia, Fotografia, Natureza
(13, 4, 5), (13, 6, 4), (13, 3, 3),  -- Compras, Vida Noturna, Fotografia
(14, 3, 5), (14, 4, 4), (14, 1, 3),  -- Fotografia, Compras, Praia
(15, 1, 5), (15, 7, 4), (15, 3, 3),  -- Praia, Natureza, Fotografia

-- PERFIL SOLITÁRIO (Usuários 16-25)
(16, 3, 5), (16, 7, 4), (16, 5, 3),  -- Fotografia, Natureza, Radical
(17, 7, 5), (17, 3, 4), (17, 5, 3),  -- Natureza, Fotografia, Radical
(18, 3, 5), (18, 7, 4), (18, 1, 3),  -- Fotografia, Natureza, Praia
(19, 5, 5), (19, 3, 4), (19, 7, 3),  -- Radical, Fotografia, Natureza
(20, 7, 5), (20, 3, 4), (20, 5, 3),  -- Natureza, Fotografia, Radical

-- USUÁRIOS 26-50 (Distribuição balanceada)
(21, 6, 5), (21, 4, 4), (21, 2, 3),  -- Vida Noturna, Compras, Piscina
(22, 2, 5), (22, 6, 4), (22, 4, 3),  -- Piscina, Vida Noturna, Compras
(23, 4, 5), (23, 3, 4), (23, 1, 3),  -- Compras, Fotografia, Praia
(24, 5, 5), (24, 7, 4), (24, 3, 3),  -- Radical, Natureza, Fotografia
(25, 1, 5), (25, 5, 4), (25, 3, 3),  -- Praia, Radical, Fotografia
(26, 2, 5), (26, 1, 4), (26, 6, 3),  -- Piscina, Praia, Vida Noturna
(27, 4, 5), (27, 6, 4), (27, 3, 3),  -- Compras, Vida Noturna, Fotografia
(28, 7, 5), (28, 3, 4), (28, 5, 3),  -- Natureza, Fotografia, Radical
(29, 5, 5), (29, 1, 4), (29, 7, 3),  -- Radical, Praia, Natureza
(30, 6, 5), (30, 2, 4), (30, 4, 3),  -- Vida Noturna, Piscina, Compras
(31, 3, 5), (31, 4, 4), (31, 7, 3),  -- Fotografia, Compras, Natureza
(32, 5, 5), (32, 7, 4), (32, 3, 3),  -- Radical, Natureza, Fotografia
(33, 6, 5), (33, 4, 4), (33, 2, 3),  -- Vida Noturna, Compras, Piscina
(34, 1, 5), (34, 2, 4), (34, 3, 3),  -- Praia, Piscina, Fotografia
(35, 7, 5), (35, 3, 4), (35, 5, 3),  -- Natureza, Fotografia, Radical
(36, 4, 5), (36, 3, 4), (36, 6, 3),  -- Compras, Fotografia, Vida Noturna
(37, 5, 5), (37, 1, 4), (37, 7, 3),  -- Radical, Praia, Natureza
(38, 2, 5), (38, 6, 4), (38, 1, 3),  -- Piscina, Vida Noturna, Praia
(39, 3, 5), (39, 7, 4), (39, 4, 3),  -- Fotografia, Natureza, Compras
(40, 7, 5), (40, 5, 4), (40, 3, 3),  -- Natureza, Radical, Fotografia
(41, 6, 5), (41, 4, 4), (41, 2, 3),  -- Vida Noturna, Compras, Piscina
(42, 1, 5), (42, 2, 4), (42, 3, 3),  -- Praia, Piscina, Fotografia
(43, 4, 5), (43, 3, 4), (43, 6, 3),  -- Compras, Fotografia, Vida Noturna
(44, 7, 5), (44, 3, 4), (44, 5, 3),  -- Natureza, Fotografia, Radical
(45, 5, 5), (45, 1, 4), (45, 3, 3),  -- Radical, Praia, Fotografia
(46, 2, 5), (46, 6, 4), (46, 1, 3),  -- Piscina, Vida Noturna, Praia
(47, 3, 5), (47, 7, 4), (47, 1, 3),  -- Fotografia, Natureza, Praia
(48, 4, 5), (48, 3, 4), (48, 7, 3),  -- Compras, Fotografia, Natureza
(49, 5, 5), (49, 7, 4), (49, 1, 3),  -- Radical, Natureza, Praia
(50, 2, 5), (50, 1, 4), (50, 6, 3);  -- Piscina, Praia, Vida Noturna

-- =============================================================================
-- AVALIAÇÕES DAS VIAGENS 
-- =============================================================================

INSERT INTO ViagemAvaliacao (UsuarioId, ViagemId, Avaliacao)
WITH avaliacoes_realistas AS (
    SELECT 
        u.Id as UsuarioId,
        v.Id as ViagemId,
        CASE 
            -- Usuários de AVENTURA dão notas altas para viagens de AVENTURA
            WHEN EXISTS (
                SELECT 1 FROM GeneroUsuario gu 
                WHERE gu.UsuarioId = u.Id AND gu.GeneroId = 2 AND gu.Preferencia >= 4
            ) AND EXISTS (
                SELECT 1 FROM GeneroViagem gv 
                WHERE gv.ViagemId = v.Id AND gv.GeneroId = 2 AND gv.Intensidade >= 4
            ) THEN 4.0 + (RAND() * 1.0)  -- 4.0-5.0
            
            -- Usuários de ROMANCE dão notas altas para viagens ROMÂNTICAS
            WHEN EXISTS (
                SELECT 1 FROM GeneroUsuario gu 
                WHERE gu.UsuarioId = u.Id AND gu.GeneroId = 1 AND gu.Preferencia >= 4
            ) AND EXISTS (
                SELECT 1 FROM GeneroViagem gv 
                WHERE gv.ViagemId = v.Id AND gv.GeneroId = 1 AND gv.Intensidade >= 4
            ) THEN 4.2 + (RAND() * 0.8)  -- 4.2-5.0
            
            -- Compatibilidade com clima
            WHEN p.Clima = v.Clima THEN 3.5 + (RAND() * 1.0)  -- 3.5-4.5
            
            -- Avaliação neutra para incompatibilidades
            ELSE 2.5 + (RAND() * 1.0)  -- 2.5-3.5
        END as Avaliacao,
        RAND() as random_value
        
    FROM Usuario u
    CROSS JOIN Viagem v
    JOIN Preferencias p ON u.Id = p.UsuarioId
)
SELECT UsuarioId, ViagemId, ROUND(Avaliacao, 1)
FROM avaliacoes_realistas
WHERE random_value < 0.5  
ORDER BY random_value
LIMIT 500;