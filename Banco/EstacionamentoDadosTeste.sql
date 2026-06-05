INSERT INTO Categoria (nome_categoria, descricao)
VALUES
('Carro', 'Veículos de passeio'),
('Moto', 'Motocicletas'),
('Caminhonete', 'Veículos de grande porte');

INSERT INTO Setor (nome_setor, tipo_setor)
VALUES
('A', 'Coberto'),
('B', 'Descoberto'),
('C', 'Vip');

INSERT INTO Tabela_Preco
(id_categoria, valor_hora, valor_adicional, tolerancia_minutos)
VALUES
(1, 10.00, 5.00, 15),
(2, 5.00, 2.50, 15),
(3, 15.00, 7.50, 15);

INSERT INTO Cliente (nome, cpf, telefone)
VALUES
('Luciana Silva', '11111111111', '81999990001'),
('Carlos Henrique', '22222222222', '81999990002'),
('Ageu Simões', '33333333333', '81999990003'),
('João Victor', '44444444444', '81999990004'),
('José Matheus', '55555555555', '81999990005');

INSERT INTO Veiculo
(placa, modelo, cor, id_cliente, id_categoria)
VALUES
('ABC1234', 'Onix', 'Prata', 1, 1),
('DEF5678', 'HB20', 'Branco', 2, 1),
('GHI9012', 'CG160', 'Preta', 3, 2),
('JKL3456', 'Hilux', 'Cinza', 4, 3),
('MNO7890', 'Corolla', 'Preto', 5, 1);

INSERT INTO Vaga
(numero, status_vaga, id_setor)
VALUES
('A01', 'Livre', 1), ('A02', 'Livre', 1),('A03', 'Livre', 1),
('B01', 'Livre', 2), ('B02', 'Livre', 2),('B03', 'Livre', 2),
('C01', 'Livre', 3),('C02', 'Livre', 3);

INSERT INTO Ticket (data_entrada, data_saida, valor_pago, forma_pagamento,
status_ticket, id_veiculo, id_vaga)
VALUES(DATE_SUB(NOW(), INTERVAL 3 HOUR),DATE_SUB(NOW(), INTERVAL 1 HOUR),
20.00,'Pix','Finalizado',1,1
);

INSERT INTO Ticket(data_entrada, data_saida, valor_pago, forma_pagamento,
status_ticket, id_veiculo, id_vaga)
VALUES(DATE_SUB(NOW(), INTERVAL 5 HOUR),DATE_SUB(NOW(), INTERVAL 2 HOUR),
30.00,'Cartão','Finalizado',2,2
);

INSERT INTO Ticket
(data_entrada, status_ticket, id_veiculo, id_vaga)
VALUES(DATE_SUB(NOW(), INTERVAL 30 MINUTE),
'Aberto',3,3
);

