import re

def parse_log(file_path):
    servers = []
    ip_pairs = []
    
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            
            if ':' in line and ' ' not in line:  # Определяем сервер
                servers.append(line)
            elif ' ' in line:  # Определяем строку с IP
                parts = line.split()
                if len(parts) == 2:
                    ip_pairs.append(tuple(parts))
    
    matches = []
    with open(file_path, 'r') as file:
        known_server = None
        for line in file:
            line = line.strip()
            if not line:
                continue
            
            if line in servers:
                known_server = line
            elif ' ' in line and known_server:
                parts = line.split()
                if len(parts) == 2:
                    # Проверяем на совпадения с ранее найденными парами
                    for ip1, ip2 in ip_pairs:
                        if (parts[0] == ip2 and parts[1] == ip1) or (parts[0] == ip1 and parts[1] == ip2):
                            matches.append((known_server, line))
    
    return matches

# Использование
file_path = 'log.txt'  # Укажите путь к вашему файлу
matches = parse_log(file_path)
for match in matches:
    print(f'Match found: {match[0]} <-> {match[1]}')
