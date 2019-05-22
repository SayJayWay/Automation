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
