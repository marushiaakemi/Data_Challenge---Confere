# Data_Challenge---Confere

Programa responsável por fazer o download de um arquivo em formato EDI (Electronic Data Interchange) e converter para o formato de Json.

Dentro da pasta src consta o arquivo Data_challenge.py, onde assim que executado, faz o download do arquivo em formato csv e faz a conversao para um arquivo Json chamado arquivo_parseado.json.

Para executá-lo, basta python3 Data_challenge.py.

Além do arquivo json, sao criadas também 2 tabelas dentro de um banco sqlite3 in memory para armazenar os dados que foram recuperados do EDI.