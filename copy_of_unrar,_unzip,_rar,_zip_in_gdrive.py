# -*- coding: utf-8 -*-
"""Copy of Unrar, Unzip, Rar, Zip in Gdrive - TopTricks.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xinRwhXtlL-9Y0KbPrTmTxNdcN-Hvq4m

#**Unrar, Unzip, Rar, Zip in Gdrive - TopTricks.tech**

---
---

# **STEP 1 - First Mount your Google Drive**


---

<img src="https://i.ibb.co/yPqB75v/output-onlinepngtools.png" alt="output-onlinepngtools" border="0">
"""

from google.colab import drive
drive.mount('/content/drive')

"""# **<font size="10"><center>UNRAR/UNZIP Your Files</center>**</font>

---



---

# **STEP 2 - Run the below Cell to Unrar a .rar file**


---
<img src="https://i.ibb.co/tK5Jhxs/output-onlinepngtools.png" alt="output-onlinepngtools" border="0">

*   First path in below cell - Your Google Drive file location which you want to Unrar
*   Second path in below cell - Path where you want to extract the rar file in Google Drive
"""

!unrar x "/content/drive/My Drive/Desktop.rar" "/content/drive/My Drive/"

"""---



---



---

# **STEP 2 - Run the below cell to Unzip a .zip file**


---
<img src="https://i.ibb.co/Dg66pDB/156361082210525933.png" alt="156361082210525933" border="0">

*   First path in below cell - Your Google Drive file location which you want to Unzip
*   Second path in below cell - Path where you want to extract the zip file in Google Drive
"""

!unzip "/content/drive/My Drive/desktop1.zip" -d "/content/drive/My Drive/"

"""---



---



---

# **<font size="10"><center>RAR/ZIP Your Files</center>**</font>

---



---

# **STEP 3 - Run the below Cells to compress your files into .Rar**


---


<img src="https://i.ibb.co/tK5Jhxs/output-onlinepngtools.png" alt="output-onlinepngtools" border="0">
"""

# <= Click this cell to rar the folder

!apt-get install rar

"""*   First path in below cell - Your Rar File output Name (do not put .rar at the end. It will take it automatically)
*   Second path in below cell - Google Drive file location of the files/folder which you want to Rar


"""

!rar a "Folder Link"

"""# **STEP 3 - Run the below cell to .zip some files**


---
<img src="https://i.ibb.co/Dg66pDB/156361082210525933.png" alt="156361082210525933" border="0">

*   First path in below cell - Your Zip output filename
*   Second path in below cell - Google Drive file location of the files which you want to Zip
"""

!zip -r "/content/drive/My Drive/Getting started.zip" "/content/drive/My Drive/Getting started.pdf"

"""
## **Important note - After doing all the steps, please note that depending on your file size of the Zip and Rar files, it may take a while to show up in your Google Drive. Please be patient. Eventually, it will show up in your drive.**
###**For larger files - it may take some time to show up in your Google Drive. Do not rerun the code if it doesn't show up fast. Just keep refreshing your Google Drive page to see if it shows up**
###**For small files - it will show up quicker in your Google Drive. Just wait until it shows up. Just keep refreshing your page to see if it shows up**"""