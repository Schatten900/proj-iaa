-- Tabela principal de Viagens
CREATE TABLE IF NOT EXISTS Viagem (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Descricao TEXT,
    Clima ENUM('quente', 'frio', 'temperado', 'tropical') NOT NULL,
    Preco ENUM('economico', 'medio', 'alto', 'luxo') NOT NULL,
    Companhia ENUM('sozinho', 'casal', 'familia', 'amigos') NOT NULL,
    Popularidade FLOAT DEFAULT 0,
);

-- Tabela de Preferências dos Usuários (1:1 com Usuario)
CREATE TABLE IF NOT EXISTS Preferencias (
    UsuarioId INT UNIQUE NOT NULL,
    Clima ENUM('quente', 'frio', 'temperado', 'tropical') NOT NULL DEFAULT 'temperado',
    Preco ENUM('economico', 'medio', 'alto', 'luxo') NOT NULL DEFAULT 'medio',
    Companhia ENUM('sozinho', 'casal', 'familia', 'amigos') NOT NULL DEFAULT 'casal',
    FOREIGN KEY (UsuarioId) REFERENCES Usuario(Id) ON DELETE CASCADE
);

-- Tabela de Gêneros (categorias de viagem)
CREATE TABLE IF NOT EXISTS Genero (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(50) UNIQUE NOT NULL,
    Descricao TEXT,
);

-- Tabela de relação Usuário-Gênero (N:M)
CREATE TABLE IF NOT EXISTS GeneroUsuario (
    UsuarioId INT NOT NULL,
    GeneroId INT NOT NULL,
    Preferencia INT CHECK (Preferencia BETWEEN 1 AND 5) DEFAULT 3,
    FOREIGN KEY (UsuarioId) REFERENCES Usuario(Id) ON DELETE CASCADE,
    FOREIGN KEY (GeneroId) REFERENCES Genero(Id) ON DELETE CASCADE,
);

-- Tabela de relação Viagem-Gênero (N:M)
CREATE TABLE IF NOT EXISTS GeneroViagem (
    ViagemId INT NOT NULL,
    GeneroId INT NOT NULL,
    Intensidade INT CHECK (Intensidade BETWEEN 1 AND 5) DEFAULT 3,
    FOREIGN KEY (ViagemId) REFERENCES Viagem(Id) ON DELETE CASCADE,
    FOREIGN KEY (GeneroId) REFERENCES Genero(Id) ON DELETE CASCADE,
);

-- Tabela de Características de Lazer
CREATE TABLE IF NOT EXISTS Lazer (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(50) UNIQUE NOT NULL,
    Descricao TEXT,
);

-- Tabela de relação Usuário-Lazer (N:M)
CREATE TABLE IF NOT EXISTS LazerUsuario (
    UsuarioId INT NOT NULL,
    LazerId INT NOT NULL,
    Intensidade INT CHECK (Importancia BETWEEN 1 AND 5) DEFAULT 3,
    FOREIGN KEY (UsuarioId) REFERENCES Usuario(Id) ON DELETE CASCADE,
    FOREIGN KEY (LazerId) REFERENCES Lazer(Id) ON DELETE CASCADE,
);

-- Tabela de relação Viagem-Lazer (N:M)
CREATE TABLE IF NOT EXISTS LazerViagem (
    ViagemId INT NOT NULL,
    LazerId INT NOT NULL,
    Qualidade INT CHECK (Qualidade BETWEEN 1 AND 5) DEFAULT 3,
    FOREIGN KEY (ViagemId) REFERENCES Viagem(Id) ON DELETE CASCADE,
    FOREIGN KEY (LazerId) REFERENCES Lazer(Id) ON DELETE CASCADE,
);