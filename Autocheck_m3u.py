# -------------------------- # 
#         VERSÃO  2.8        #
# -------------------------- # 
        
import os
import requests
import re

def check_online(m3u_file):
    online_list = []
    offline_list = []
    count = 0
    with open(m3u_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("#EXTINF"):
                params = {"name": "", "tvg-id": "", "tvg-logo": "", "group-title": "", "link": ""}
                match = re.search(",(.*)", line)
                params["name"] = match.group(1).strip() if match else ""                 
                match = re.search("tvg-id=\"(.*?)\"", line)
                params["tvg-id"] = match.group(1) if match else ""
                match = re.search("tvg-logo=\"(.*?)\"", line)
                params["tvg-logo"] = match.group(1) if match else ""   
                match = re.search("group-title=\"(.*?)\"", line)
                params["group-title"] = match.group(1) if match else ""
            if line.startswith("http"):
                link = line.strip()
                params["link"] = link
#                CHECAGEM DE PARAMETROS
#                print(f"\033[0;30;41m{params['name']}\033[m")
#                print(f"\033[0;30;42m{params['tvg-id']}\033[m")
#                print(f"\033[0;30;43m{params['tvg-logo']}\033[m")
#                print(f"\033[0;30;44m{params['group-title']}\033[m")
#                print(f"\033[0;30;45m{params['link']}\033[m")
                try:
                    r = requests.head(line.strip())
                    count += 1
                    if r.status_code == 200:
                        print(f"{count} {line.strip()} esta \033[1;49;32monline\033[m.")
                        online_list.append(params)
                    else:
                        offline_list.append(line.strip())
                        print(f"{count}{line.strip()} esta \033[1;49;31moffline\033[m.")
                except:
                    count += 1
                    offline_list.append(line.strip())
                    print(f"{count} {line.strip()} esta \033[1;49;33moffline.\033[m")
    return online_list,offline_list

current_dir = os.path.dirname(os.path.abspath(__file__))
files = os.listdir(os.path.join(current_dir, 'Listas_Novas'))
m3u_files = [file for file in files if file.endswith('.m3u')]

if len(m3u_files) > 0:
    print("\nOs seguintes arquivos M3U foram encontrados na pasta Listas_Novas:\n")
    for index,file in enumerate(m3u_files):
        print(f"{index+1}. {file}")
    file_index = int(input("\nEscolha o numero do arquivo que deseja analisar: "))
    print("\n" * os.get_terminal_size().lines) #limpar linha
    selected_file = m3u_files[file_index-1]
    selected_file = os.path.join(current_dir, 'Listas_Novas', selected_file)
    print(f"\033[0;30;41mVoce selecionou:\033[m\033[1;47;41m {m3u_files[file_index-1]} \033[m")
    online_list,offline_list = check_online(selected_file)
    print(f"\n\033[0;30;41mA analise de {file} esta \033[m\033[1;47;41mcompleta \033[m \n{len(online_list)} arquivos estao online e {len(offline_list)} arquivos estao offline.")
    
    save_path = os.path.join(current_dir, "Arquivos_Salvos", "online_list.txt")
    with open(save_path, "a") as f:
        for item in online_list:
            f.write("{}\n{}\n\n".format(item['name'], item['link']))
    online_count = sum(1 for line in open(save_path))
    
    save_path = os.path.join(current_dir, "Arquivos_Salvos", "offline_list.txt")
    with open(save_path, "a") as f:
        for item in offline_list:
            f.write("%s\n" % item)
    offline_count = sum(1 for line in open(save_path))  
             
    save_path = os.path.join(current_dir, "Arquivos_Salvos", "Hecko_BR_Completa.m3u")
    with open(save_path, "a") as f:
        f.write("#EXTM3U\n")
        for item in online_list:
            f.write("#EXTINF:-1 tvg-id=\"{}\" tvg-logo=\"{}\" group-title=\"{}\",{}\n{}\n".format(item['tvg-id'], item['tvg-logo'], item['group-title'], item['name'], item['link']))

else:
    print("Nenhum arquivo M3U foi encontrado na pasta Listas_Novas")

print(f"\n\n\033[1;30;43m  #  TOTAIS  #  \033[m")
print(f"No total ja foram analisados:\n\033[1;49;32m[{online_count} ONLINE]\033[m \n\033[1;49;31m[{offline_count} OFFLINE]\033[m\n")

# -------------------------- # 
#       F     I     M        #
# -------------------------- # 



