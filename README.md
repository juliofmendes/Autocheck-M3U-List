# Autocheck-M3U-List

This code is checking if the links in an M3U file are online or offline by sending a HEAD request to each link using the requests module. The M3U file is read and parsed to extract the link, name, tvg-id, tvg-logo, and group-title. Then, the script checks the status code of the response from the server and prints the result.

If the status code is 200, the link is considered online and the link is added to an online_list. If the status code is not 200, the link is considered offline and it is added to an offline_list.

The script first uses the os module to get the current working directory and list all the files in the subfolder 'Listas_Novas'

It then filters the list of files to only include files with the '.m3u' file extension and prompts the user to select which file they want to check.

Once the file is selected, it opens the file and parses the links, if the link is online it adds to one list, if it's offline it adds to another list.

It also prints the status of the links, if it's online or offline.

Overall, this script can be useful for checking the availability of links in an M3U file, which can be useful for IPTV streaming, for example.

<details>
  <summary>Screenshots</summary>
  
<img src="https://github.com/juliofmendes/Instagram-post-generator-IGPG/blob/main/example_line_7.jpg" width="500" height="500">
<img src="https://github.com/juliofmendes/Instagram-post-generator-IGPG/blob/main/example_line_7.jpg" width="500" height="500">
<img src="https://github.com/juliofmendes/Instagram-post-generator-IGPG/blob/main/example_line_7.jpg" width="500" height="500">
  
</details>



<details>
  <summary>Spoiler warning</summary>
  
  Spoiler text. Note that it's important to have a space after the summary tag. You should be able to write any markdown you want inside the `<details>` tag... just make sure you close `<details>` afterward.
  
  ```javascript
  console.log("I'm a code block!");
  ```
  
</details>
## How to Instal

Download the code:
```
git clone git@github.com:juliofmendes/Instagram-post-generator-IGPG.git
```
To instal PIL (Python Imaging Library):
```
pip install pillow
```
## How to use
```
python IGPG.py
```

## Features
- 


## ToDo
* [ ] - Criar looping para retirar os similares

## Changelog

#### V2.8
Fix error com captura do nome sem virgula.

V2.7 - melhorada a captura para as tags na m3u e salvamento, agora sem erro. Resolvido o problema de salvamento dos arquivos offline na lista. Retirado a repetição do ultimo item.

V2.5 - Restruturado para armazenar as tags da lista m3u e organizado a forma de salvamento. Agora gera a lista M3U com os links online.

V2.1 - Tradução para PT-BR. 

V2.0 - Adicionado recursos para salvar arquivos na pasta "Arquivos_Salvos" e leitura de listas na pasta  "Listas_Novas”. Ajustes na contagem de linhas será feita no arquivo correto salvo na pasta "Arquivos_Salvos" e evitará o erro.

V1.8 - Adicionado correção da quantidade total já salva.

V1.7 - Adicionado cores e inicio da interface visual.

V1.5 - Este código adiciona a capacidade de selecionar qual arquivo M3U deseja-se analisar, ao listar todos os arquivos M3U encontrados na pasta atual e pedir ao usuário para escolher um. Ele também fornece uma mensagem quando o processo estiver concluído, incluindo a quantidade de arquivos online e offline. Além disso, ele adiciona uma contagem em tempo real dos arquivos analisados e quantidade de arquivos salvo nos arquivos de texto.

V1.0 - Básico e inicial.

#### Disclaimer
- 
