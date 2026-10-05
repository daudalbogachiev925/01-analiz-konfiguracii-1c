SELECT module_name,
       LENGTH(body) AS chars,
       (LENGTH(body) - LENGTH(REPLACE(body, 'Процедура', ''))) / 9 AS procedures,
       (LENGTH(body) - LENGTH(REPLACE(body, 'Если', ''))) / 4 AS ifs,
       (LENGTH(body) - LENGTH(REPLACE(body, 'Цикл', ''))) / 4 AS loops
FROM modules
ORDER BY procedures DESC;
