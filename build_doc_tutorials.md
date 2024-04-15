# SET UP TO RUN SNAKEMAKE -C1 BUILD_DOC ON WINDOWS
My task is update documentation for the htwo-map repository, so I must run snakemake -c1 build_doc to compile the documentation on my local machine. Howerver, there are some dependencies and requirements for that. If you want to do so, please follow this tutorials.

## INSTALLATION
There are two things that you have to install:
- Download [Ubuntu Windows Subsystem Linux](https://ubuntu.com/desktop/wsl), which helps you run Linux on your Windows terminal.
- Download [Anaconda for Linux 64-Bit (x86) Installer](https://www.anaconda.com/download/success), which helps you create the required environment from the environment.yml file.

## WORKFLOW

### STEP 1: Basic setup

After install Ubuntu WSL, you should have a terminal like this, but without the (base).
![image](https://github.com/huyhoang-mike/Markdown-Compiler/assets/109945762/818e2fb2-e16f-4ee4-8a4e-a79e49373ce7)

Change directory (cd) to where you have installed [Anaconda for Linux 64-Bit (x86) Installer](https://www.anaconda.com/download/success). Firstly, the default directory is at "root", so you should be back to one subdirectory by using:
```
cd ..
```
Then change directory to the place where you installed. In my case, I use the command:
```
cd mnt/c/Users/Admin/Downloads
```
### STEP 2: Install Anaconda on WSL
After change directory to the directory where Anaconda was downloaded, use the command below to start installing Anaconda: 
```
bash Anaconda3-2024.02-1-Linux-x86_64.sh
```
Now, you should have (base) in the your terminal like this:
![image](https://github.com/huyhoang-mike/Markdown-Compiler/assets/109945762/1663f154-7fdb-4ea8-8ea8-cb9d92ba5069)

### STEP 3: Clone repository
There are two repositories which you must clone:
- The htwo-map: clone it using **https** method
```
git clone https://gitlab.oth-regensburg.de/EI/Labore/fenes/energiespeicher/htwo-map.git
```
- The ptx-database: clone it using **https** method
```
https://gitlab.oth-regensburg.de/EI/Labore/fenes/energiespeicher/ptx-database.git
```
In my case, I clone the two repositories to the home directory in WSL. Folder structure should be like this:
![image](https://github.com/huyhoang-mike/Markdown-Compiler/assets/109945762/c8ef25cd-0892-49bb-ac12-27e24c8e0940)

### STEP 4: Set up conda environment
At first, change the directory to htwo-map, then run `conda env create --file environment.yml` to create the environment. Then, you need to activate it by using `conda activate htwo_map`. Finally, run `snakemake -c1 build_doc` to export the pdf and html documentation. 
\For your information: You must clone the ptx repository because snakemake requires the ptx-database in the workflow. 


## Video


