def set_table_to_query_at(table="empresas"):

    query_mais_funcionarios = f'''SELECT regiao_brasil, SUM(num_funcionarios) AS total_funcionarios
        FROM {table}
        GROUP BY regiao_brasil
        ORDER BY total_funcionarios DESC
        LIMIT 1'''

    query_empresa_mais_antiga = f'''SELECT nome AS Nome_Empresa, data_fundacao AS Data_Fundacao
    FROM {table}
    ORDER BY data_fundacao ASC
    LIMIT 1;
    '''

    query_regiao_mais_industrial =  f'''SELECT regiao_brasil AS Regiao, COUNT(*) AS Numero_Empresas_Industriais
    FROM {table}
    WHERE setor_atuacao = 'Industrial'
    GROUP BY regiao_brasil
    ORDER BY Numero_Empresas_Industriais DESC
    LIMIT 1;
    '''

    query_numero_empresas_por_setor_decrescente = f'''SELECT setor_atuacao AS Setor, COUNT(*) AS Numero_Empresas
    FROM {table}
    GROUP BY setor_atuacao
    ORDER BY Numero_Empresas DESC;
    '''

    query_total_funcionarios_todas_empresas = f'''SELECT SUM(num_funcionarios) AS Total_Funcionarios
    FROM {table};
    '''
    return query_mais_funcionarios, query_empresa_mais_antiga,  query_regiao_mais_industrial, query_numero_empresas_por_setor_decrescente,  query_total_funcionarios_todas_empresas