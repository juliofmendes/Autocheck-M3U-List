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
* [ ] - Create a ...

---
## Changelog
* [x] - Create a ...
---
---
#### Disclaimer
- 
