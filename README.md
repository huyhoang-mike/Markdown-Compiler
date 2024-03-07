# INTEGRATION PIPELINE MAPS INTO A WEBSITE WITH QGIS
Let's say, I have a maps with the special information, and I want to integrate it into a base maps. How can I achieve that? Let's follow the tutotials!
## INSTALLATION
Download [QGIS](https://qgis.org/en/site/forusers/download.html) which is the software for creating, editing, visualising, analysing and publishing geospatial information. 
## WORKFLOW
### STEP 1
You should have a vector file of the maps. If you do not have a vector file, you should use a converter. The svg file did not work in my case, so I used the website below to convert it into dxf one.
```
https://anyconv.com/svg-to-dxf-converter/
```
### STEP 2
You need to place the maps in a right area using the Georeferencer in QGIS. On the tools bar, you should:
```
Layer -> Georeferencer
```
Next, click "Open vector" on the tools bar. Finally, use "Add points" to start georeferencing. You can also follow [this](https://www.youtube.com/watch?v=2pi2illeom4&t=96s) video to know how to georeference.

### STEP 3
Right click on the vector layer that you've just created, and follow these steps:
```
Export -> Save Feature As
```
Finally, save it in the geojson format. Now, you can use that to display the pipeline on your own website.

## DEMO

