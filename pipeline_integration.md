# INTEGRATING PIPELINE MAPS INTO A WEBSITE WITH QGIS

Let's say, I have a map with special information, and I want to integrate it into base maps. How can I achieve that? Let's follow the tutorials!

## INSTALLATION

Download [QGIS](https://qgis.org/en/site/forusers/download.html), which is software for creating, editing, visualising, analysing, and publishing geospatial information.

## WORKFLOW

### STEP 1

You should have a vector file of the map. If you do not have a vector file, you should use a converter. The SVG file did not work in my case, so I used the website below to convert it into a DXF file.

```
https://anyconv.com/svg-to-dxf-converter/
```

### STEP 2

You need to place the map in the right area using the Georeferencer in QGIS. On the toolbar, you should:

```
Layer -> Georeferencer
```

Next, click "Open vector" on the toolbar. Finally, use "Add points" to start georeferencing. You can also follow [this](https://www.youtube.com/watch?v=2pi2illeom4&t=96s) video to learn how to georeference.

### STEP 3

Right-click on the vector layer that you've just created, and follow these steps:

```
Export -> Save Feature As
```

Finally, save it in the GeoJSON format. Now, you can use that to display the pipeline on your own website.

## DEMO

![image](https://github.com/huyhoang-mike/Markdown-Compiler/assets/109945762/445b47eb-8274-426f-95de-b6b227a17709)

