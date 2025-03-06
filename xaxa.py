import re

def extract_valid_servers(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        server_name = None
        valid_addresses = set()  # Используем set для уникальных адресов
        
        for line in infile:
            # Находим имя сервера
            server_match = re.search(r'=== Output from (.+) ===', line)
            if server_match:
                # Если были предыдущие записи, записываем их в файл
                if valid_addresses:
                    outfile.write(f"{server_name}\n")
                    for address in valid_addresses:
                        outfile.write(f"{address}\n")
                    valid_addresses = set()  # Очищаем set для нового сервера
                server_name = server_match.group(1)
                continue
            
            if server_name:
                # Ищем соответствия для IP-адресов и портов
                match = re.search(r'\s+(\S+):(\d+)\s+(\S+):(\d+)', line)
                if match:
                    local_address, local_port, foreign_address, foreign_port = match.groups()
                    
                    # Проверяем, является ли внешний адрес глобальным
                    if not (foreign_address.startswith("0.0.0.0") or 
                            foreign_address.startswith("localhost") or 
                            foreign_address.startswith("[::]")):
                        # Добавляем внешний адрес в set
                        valid_addresses.add(f"{foreign_address}:{foreign_port}")
        
        # Записываем последний сервер, если были найденные записи
        if valid_addresses:
            outfile.write(f"{server_name}\n")
            for address in valid_addresses:
                outfile.write(f"{address}\n")

# Использование
extract_valid_servers('logs.txt', 'filtered_logs.txt')


cp        0      0 dbscsrvt2.rrb.by:17984  dbscsrvt2.rrb.:ncube-lm ESTABLISHED oracle     1027188798 3703917/ora_lreg_t2 
tcp        0      0 dbscsrvt2.rrb.by:59452  ST-Storage:microsoft-ds ESTABLISHED root       703466654  -                   
tcp        0      0 dbscsrvt2.rrb.by:ssh    10.28.4.190:34878       ESTABLISHED root       1044960063 266752/sshd: root [ 
tcp        0      0 dbscsrvt2.rrb.by:31452  dbscsrvt2.rrb.:ncube-lm ESTABLISHED oracle     497815506  1072386/ora_lreg_t2 
tcp6       0      0 [::]:sunrpc             [::]:*                  LISTEN      root       19914      1/systemd           
tcp6       0      0 [::]:ncube-lm           [::]:*                  LISTEN      oracle     2965       1515/tnslsnr        
tcp6       0      0 [::]:13043              [::]:*                  LISTEN      oracle     497831015  1072402/ora_d000_t2 
tcp6       0      0 [::]:ssh                [::]:*                  LISTEN      root       25155      1214/sshd           
tcp6       0      0 [::]:32283              [::]:*                  LISTEN      oracle     1027184218 3703933/ora_d000_t2 
tcp6       0      0 [::]:fcp-addr-srvr1     [::]:*                  LISTEN      oracle     497828590  1515/tnslsnr        
tcp6       0      0 [::]:zabbix-agent       [::]:*                  LISTEN      zabbix     182928772  3958318/zabbix_agen 
tcp6       0      0 [::]:websm              [::]:*                  LISTEN      root       22869      1/systemd           
tcp6       0      0 dbscsrvt2.rrb.:ncube-lm 10.28.4.125:51692       ESTABLISHED oracle     1044959708 266566/oraclet2bank 
tcp6       0      0 dbscsrvt2.rrb.:ncube-lm 10.28.4.125:37046       ESTABLISHED oracle     1044935991 266081/oraclet2bank 
tcp6       0      0 dbscsrvt2.rrb.:ncube-lm 10.28.4.125:54518       ESTABLISHED oracle     1044959928 266697/oraclet2bank 
tcp6       0      0 dbscsrvt2.rrb.:ncube-lm 10.28.4.125:48420       ESTABLISHED oracle     1044959967 266721/oraclet2bank 
tcp6       0      0 dbscsrvt2.rrb.:ncube-lm 10.28.4.22:32778        ESTABLISHED oracle     1044352825 238847/oraclet2fosd 
