USE Estacionamento;

CREATE VIEW vw_veiculos_clientes AS
SELECT v.id_veiculo, v.placa, v.modelo, v.cor, c.nome AS cliente, c.cpf, cat.nome_categoria FROM Veiculo v
JOIN Cliente c ON v.id_cliente = c.id_cliente
JOIN Categoria cat ON v.id_categoria = cat.id_categoria;


CREATE VIEW vw_vagas_livres AS
SELECT v.id_vaga, v.numero, s.nome_setor, s.tipo_setor FROM Vaga v 
JOIN Setor s ON v.id_setor = s.id_setor
WHERE v.status_vaga = 'Livre';


CREATE VIEW vw_faturamento AS
SELECT DATE(data_saida) AS data_pagamento, COUNT(*) AS total_tickets, SUM(valor_pago) AS total_faturado FROM Ticket
WHERE status_ticket IN ('Pago', 'Finalizado')
GROUP BY DATE(data_saida);



DELIMITER $$
CREATE FUNCTION fn_calcular_valor(p_id_ticket INT) RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
  DECLARE v_categoria INT;
  DECLARE v_minutos INT;
  DECLARE v_horas INT;
  DECLARE v_valor_hora DECIMAL(10,2);
  DECLARE v_valor_adicional DECIMAL(10,2);
  DECLARE v_tolerancia INT;
  DECLARE v_total DECIMAL(10,2) DEFAULT 0.00;
  SELECT ve.id_categoria, TIMESTAMPDIFF(MINUTE, t.data_entrada, t.data_saida)
  INTO v_categoria, v_minutos FROM Ticket t
  JOIN Veiculo ve ON t.id_veiculo = ve.id_veiculo
  WHERE t.id_ticket = p_id_ticket;
  SELECT valor_hora, valor_adicional, tolerancia_minutos
  INTO v_valor_hora, v_valor_adicional, v_tolerancia FROM Tabela_Preco 
  WHERE id_categoria = v_categoria LIMIT 1;
  IF v_minutos <= IFNULL(v_tolerancia, 0) THEN
    SET v_total = 0.00;
  ELSE
    SET v_horas = CEIL(v_minutos / 60.0);
    IF v_horas = 1 THEN
      SET v_total = v_valor_hora;
    ELSE
      IF v_valor_adicional IS NULL THEN
        SET v_total = v_horas * v_valor_hora;
      ELSE
        SET v_total = v_valor_hora + ((v_horas - 1) * v_valor_adicional);
      END IF;
    END IF;
  END IF;
  RETURN v_total;
END $$
DELIMITER ;


DELIMITER $$
CREATE PROCEDURE sp_cadastrar_cliente(p_nome VARCHAR(50), p_cpf VARCHAR(14), p_telefone VARCHAR(20))
BEGIN
  INSERT INTO Cliente (nome, cpf, telefone) VALUES (p_nome, p_cpf, p_telefone);
END $$
DELIMITER ;


DELIMITER $$
CREATE PROCEDURE sp_cadastrar_veiculo(p_placa VARCHAR(7), p_modelo VARCHAR(50), p_cor VARCHAR(30), p_id_cliente INT, p_id_categoria INT)
BEGIN
  INSERT INTO Veiculo (placa, modelo, cor, id_cliente, id_categoria)
  VALUES (UPPER(p_placa), p_modelo, p_cor, p_id_cliente, p_id_categoria);
END $$
DELIMITER ;


DELIMITER $$
CREATE PROCEDURE sp_cadastrar_categoria_preco(p_nome_categoria VARCHAR(50), p_descricao VARCHAR(100), p_valor_hora DECIMAL(10,2), 
p_valor_adicional DECIMAL(10,2), p_tolerancia_minutos INT)
BEGIN
  DECLARE v_id_categoria INT;
  DECLARE EXIT HANDLER FOR SQLEXCEPTION
  BEGIN
    ROLLBACK;
    RESIGNAL;
  END;
  START TRANSACTION;
  INSERT INTO Categoria (nome_categoria, descricao)
  VALUES (p_nome_categoria, p_descricao);
  SET v_id_categoria = LAST_INSERT_ID();
  INSERT INTO Tabela_Preco (id_categoria, valor_hora, valor_adicional, tolerancia_minutos)
  VALUES (v_id_categoria, p_valor_hora, p_valor_adicional, p_tolerancia_minutos);
  COMMIT;
END $$
DELIMITER ;


DELIMITER $$
CREATE PROCEDURE sp_cadastrar_vaga(p_numero VARCHAR(10), p_id_setor INT)
BEGIN
  INSERT INTO Vaga (numero, status_vaga, id_setor)
  VALUES (UPPER(p_numero), 'Livre', p_id_setor);
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE sp_registrar_entrada(p_id_veiculo INT, p_id_vaga INT)
BEGIN
  INSERT INTO Ticket (data_entrada, status_ticket, id_veiculo, id_vaga)
  VALUES (NOW(), 'Aberto', p_id_veiculo, p_id_vaga);
END $$
DELIMITER ;


DELIMITER $$
CREATE PROCEDURE sp_registrar_saida(p_id_ticket INT,p_forma_pagamento VARCHAR(20)
)
BEGIN
DECLARE v_valor DECIMAL(10,2);
DECLARE EXIT HANDLER FOR SQLEXCEPTION
BEGIN
ROLLBACK;
RESIGNAL;
END;
START TRANSACTION;
UPDATE Ticket
SET data_saida = NOW()
WHERE id_ticket = p_id_ticket;
SET v_valor = fn_calcular_valor(p_id_ticket);
UPDATE Ticket
SET valor_pago = v_valor,forma_pagamento = p_forma_pagamento, status_ticket = 'Finalizado'
WHERE id_ticket = p_id_ticket;

COMMIT;

END $$

DELIMITER ;



DELIMITER $$
CREATE TRIGGER trg_verificar_vaga
BEFORE INSERT ON Ticket
FOR EACH ROW
BEGIN
  DECLARE v_status VARCHAR(20);
  SELECT status_vaga INTO v_status 
  FROM Vaga WHERE id_vaga = NEW.id_vaga;  
  IF v_status <> 'Livre' THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Vaga indisponível';
  END IF;
END $$
DELIMITER ;



DELIMITER $$
CREATE TRIGGER trg_ocupar_vaga
AFTER INSERT ON Ticket
FOR EACH ROW
BEGIN
  UPDATE Vaga SET status_vaga = 'Ocupada'
  WHERE id_vaga = NEW.id_vaga;
END $$
DELIMITER ;



DELIMITER $$
CREATE TRIGGER trg_liberar_vaga
AFTER UPDATE ON Ticket
FOR EACH ROW
BEGIN
  IF NEW.status_ticket = 'Finalizado' AND OLD.status_ticket <> 'Finalizado' THEN
    UPDATE Vaga SET status_vaga = 'Livre' WHERE id_vaga = NEW.id_vaga;
  END IF;
END $$
DELIMITER ;