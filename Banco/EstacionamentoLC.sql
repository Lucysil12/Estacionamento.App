CREATE DATABASE Estacionamento;
USE Estacionamento;

CREATE TABLE Cliente (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    telefone VARCHAR(20)
);

CREATE TABLE Categoria (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nome_categoria VARCHAR(50) UNIQUE NOT NULL,
    descricao VARCHAR(100)
);

CREATE TABLE Setor (
    id_setor INT AUTO_INCREMENT PRIMARY KEY,
    nome_setor VARCHAR(50) NOT NULL,
    tipo_setor VARCHAR(50)
);

CREATE TABLE Veiculo (
    id_veiculo INT AUTO_INCREMENT PRIMARY KEY,
    placa VARCHAR(7) UNIQUE NOT NULL,
    modelo VARCHAR(50),
    cor VARCHAR(30),
    id_cliente INT NOT NULL,
    id_categoria INT NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente),
    FOREIGN KEY (id_categoria) REFERENCES Categoria(id_categoria)
);

CREATE TABLE Tabela_Preco (
    id_preco INT AUTO_INCREMENT PRIMARY KEY,
    id_categoria INT NOT NULL,
    valor_hora DECIMAL(10,2) NOT NULL,
    valor_adicional DECIMAL(10,2),
    tolerancia_minutos INT,
    FOREIGN KEY (id_categoria) REFERENCES Categoria(id_categoria)
);

CREATE TABLE Vaga (
    id_vaga INT AUTO_INCREMENT PRIMARY KEY,
    numero VARCHAR(10) NOT NULL,
    status_vaga ENUM('Livre','Ocupada','Manutenção') DEFAULT 'Livre',
    id_setor INT NOT NULL,
    FOREIGN KEY (id_setor) REFERENCES Setor(id_setor)
);

CREATE TABLE Ticket (
    id_ticket INT AUTO_INCREMENT PRIMARY KEY,
    data_entrada DATETIME NOT NULL,
    data_saida DATETIME NULL,
    valor_pago DECIMAL(10,2),
    forma_pagamento ENUM('Pix','Cartão','Dinheiro'),
    status_ticket ENUM('Aberto','Pago','Finalizado') DEFAULT 'Aberto',
    id_veiculo INT NOT NULL,
    id_vaga INT NOT NULL,
    FOREIGN KEY (id_veiculo) REFERENCES Veiculo(id_veiculo),
    FOREIGN KEY (id_vaga) REFERENCES Vaga(id_vaga)
);