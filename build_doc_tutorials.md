# SET UP TO RUN SNAKEMAKE -C1 BUILD_DOC ON WINDOWS
My task is to update the documentation for htwo-map, so I must run snakemake -c1 build_doc to compile the documentation on my local machine. Howerver, there are some dependencies and requirements for that. If you want to do so, please follow this tutorials.

## INSTALLATION
There are two things that you have to install:
- Download [Ubuntu Windows Subsystem Linux](https://ubuntu.com/desktop/wsl), which helps you run Linux on your Windows terminal.
- Download [Anaconda for Linux 64-Bit (x86) Installer](https://www.anaconda.com/download/success), which helps you create the required environment from the environment.yml file.
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
