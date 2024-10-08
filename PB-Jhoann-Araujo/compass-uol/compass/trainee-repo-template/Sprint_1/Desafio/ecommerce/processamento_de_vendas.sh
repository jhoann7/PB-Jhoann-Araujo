cd compass-uol/compass/trainee-repo-template/Sprint_1/Desafio/ecommerce/
mkdir vendas
cp dados_de_vendas.csv vendas
mkdir vendas/backup
cp vendas/dados_de_vendas.csv vendas/backup/dados-20240918.csv
mv vendas/backup/dados-20240918.csv vendas/backup/backup-dados-20240918.csv
date +"%Y/%m/%d %H:%M" > vendas/backup/relatorio$(date +"%d-%m-%Y").txt
grep -oE '[0-9]{2}/[0-9]{2}/[0-9]{4}' vendas/backup/backup-dados-20240918.csv | sort | head -n 1 >> vendas/backup/relatorio$(date +"%d-%m-%Y").txt
grep -oE '[0-9]{2}/[0-9]{2}/[0-9]{4}' vendas/backup/backup-dados-20240918.csv | sort -r | head -n 1 >> vendas/backup/relatorio$(date +"%d-%m-%Y").txt
awk -F, '{sum += 1} END {print sum}' vendas/backup/backup-dados-20240918.csv >> vendas/backup/relatorio$(date +"%d-%m-%Y").txt
tail -n +2 vendas/backup/backup-dados-20240918.csv | head -n 10 >> vendas/backup/relatorio$(date +"%d-%m-%Y").txt
zip vendas/backup/backup-dados-20240918.zip vendas/backup/backup-dados-20240918.csv
rm vendas/backup/backup-dados-20240918.csv
rm vendas/dados_de_vendas.csv