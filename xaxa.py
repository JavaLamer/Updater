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
