<h1> Automation </h1>

<p> My various automation projects </p>

<h2>Project Descriptions</h2>

<h3><b>ImageJ Automation/ImageJ-multi-channel-image-prep</b></h3>
<p> To run, use "Open Macro" in ImageJ software and select the file in saved location </p>
<ol>
  <li> Asks for directory where images are located </li>
  <li> Saves the file path as "filename" </li>
  <li> Splits different image wavelengths into separate channels and labels each one </li>
  <li> Saves each of the new windows as variables </li>
  <li> Merge all the channels into a single composite image </li>
  <li> Opens colour balance window (manually adjust RGB and click OK to continue) </li>
  <li> Automatically subtracts background (remove second argument to manually adjust) </li>
  <li> Adds a cale bar of set width, height, font, color, background, location (click OK to continue) </li>
  <li> Saves prepped image as a TIFF in variable "filename" </li>
  <li> Automatically opens next file in directory </li>
</ol>

<ul>
  <li> Note: User can adjust colours based on naming scheme in step 4 or by changing the colours found in step 5</li>
</ul>

<h3><b>autoFollow.py</b></h3>
<p> Automatically follows Instagram users based on the follow.jpg image using pyautogui module </p>
<ul>
  <li>Note: follow.jpg is a certain size ->  Best to create own image for own purposes (or match screen size to image -- difficult)</li>
</ul>

<h3><b>backupToZip.py</b></h3>
<p> Copies an entire folder and its contents into a ZIP file whose filename increments using zipfile and os modules </p>
<h3><b>combinePdfs.py</b></h3>
<p> Combines all PDFs in current working directory into a single PDF using PyPDF2 and os modules </p>
<h3><b>countdown.py</b></h3>
<p> A simple countdown script that plays an alarm file once complete.  Uses time and subprocess modules </p>
<h3><b>formFiller.py</b></h3>
<p> Automatically fills in a specific form using pyautogui and time modules </p>
<ul>
  <li> Note: This script fills in a specific form by manually inputting the location of the namefields and submit button </li>
</ul>
<h3><b>lucky.py</b></h3>
<p> Displays top search result links from Google on specified string using requests, sys, webbrowser, bs4 modules </p>
<h3><b>mapIt.py</b></h3>
<p> Launches a browser to google maps with inputted string location using webbrowser and sys modules </p>
<h3><b>mcb.pyw</b></h3>
<p> Saves and loads pieces of text to clipboard (can be used as a password diary) using shelve, pyperclip, sys modules </p>
<h3><b>multidownloadXkcd.py</b></h3>
<p> Downloads XKCD comics into specific folder using multiple threads -- uses requests, os, bs4, threading modules </p>
<h3><b>openAll.py</b></h3>
<p> Launches a browser with separate tabs for each website (used to instantly open a browser with my most commonly daily visited websites -- uses webbrowser module </p>
<h3><b>quickWeather.py</b></h3>
<p> Prints the weather for a location with inputted string location -- uses json, requests, sys modules </p>
<h3><b>randomQuizGenerator.py</b></h3>
<p> Creates quizes with questions and answers in rawndom order, along with the answer key -- uses random module </p>
<h3><b>readCensusExcel.py</b></h3>
<p> Tabulates population and number of census tracts for each county based on 'censuspopdata.xlsx' sheet -- uses openpyxl and pprint modules </p>
<h3><b>removeCsvHeader.py</b></h3>
<p> Removes header from all CSV files in current working directory -- uses csv and os modules </p>
<h3><b>renameDates.py</b></h3>
<p> Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY -- uses shutil, os, re modules </p>
<h3><b>resizeAndAddLogo.py</b></h3>
<p> Resizes all images in current working directory to fit in a 300x300 square, and adds a specified photo (not included) to lower-right corner -- uses os and PIL modules </p>
<h3><b>sendDuesReminders.py</b></h3>
<p> Send emails based on payment status in spreadsheet -- uses openpyxl, smtplb, sys modules </p>
<h3><b>spiralDraw.py</b></h3>
<p> Draws a spiral using pyautogui and time modules </p>
<h3><b>stopwatch.py</b></h3>
<p> Simple stopwatch program that can also track lap times -- uses time module </p>
<h3><b>updateProduce.py</b></h3>
<p> Corrects costs in produce sales spreadsheet -- uses openpyxl module </p>
