# SET UP TO RUN SNAKEMAKE -C1 BUILD_DOC ON WINDOWS
My task is update documentation for the htwo-map repository, so I must run snakemake -c1 build_doc to compile the documentation on my local machine. Howerver, there are some dependencies and requirements for that. If you want to do so, please follow this tutorials.

## INSTALLATION
There are two things that you have to install:
- Download [Ubuntu Windows Subsystem Linux](https://ubuntu.com/desktop/wsl), which helps you run Linux on your Windows terminal.
- Download [Anaconda for Linux 64-Bit (x86) Installer](https://www.anaconda.com/download/success), which helps you create the required environment from the environment.yml file.

## WORKFLOW

### STEP 1: Basic setup

After install Ubuntu WSL, you should have a terminal like this, but without the (base).
![1](https://github.com/huyhoang-mike/Markdown-Compiler/assets/109945762/4efe4014-a3c3-4493-a94c-54fd487bfc12)


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
![2](https://github.com/huyhoang-mike/Markdown-Compiler/assets/109945762/bb0959ac-6d5d-4c89-af51-3c8f723dd2a8)


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
![3](https://github.com/huyhoang-mike/Markdown-Compiler/assets/109945762/5003ef66-6ffb-4039-9075-84f7790195a1)


### STEP 4: Set up conda environment
At first, change the directory to htwo-map, then run `conda env create --file environment.yml` to create the environment. Then, you need to activate it by using `conda activate htwo_map`. Finally, run `snakemake -c1 build_doc` to export the pdf and html documentation. 
<br/><br/>
**For your information**: You must clone the ptx repository because snakemake requires the ptx-database in the workflow. 

### STEP 5: Get the ZENODO_ACCESS_TOKEN
Some of our data is stored in a closed Zenodo repository, therefore we need to obtain tokens to enable an automized download. 
The tokens are saved as linux environment variables. Ask the maintainers of the Hydrogen Map (e.g. leon1.schumm@oth-regensburg.de, falk.birett@oth-regensburg.de) for the `ZENODO_ACCESS_TOKEN` (called "personal access token" on zenodo) of the account info@wasserstoffatlas.de.
<br/><br/>
Then, find the `.bashrc` file in your local linux system e.g. with \\wsl$\Ubuntu\home\{username}. Open the file and add the following lines with the tokens obtained and noted before, e.g.
export `ZENODO_ACCESS_TOKEN=zXZQp8Rl8qzXZQp8Rl8qzXZQp8Rl8qzXZQp8Rl8q` 
<br/><br/>
I recommend you follow [this instruction](https://gitlab.oth-regensburg.de/EI/Labore/fenes/energiespeicher/htwo-map) to get the ZENODO_ACCESS_TOKEN.

### STEP 6: Open the pdf and html file
After successfully runned snakemake, you can find the pdf and html at `/htwo-map/docs/build/`
![image](https://github.com/huyhoang-mike/Markdown-Compiler/assets/109945762/9bd67042-f631-44fe-b5c5-5c3c0a6483d2)
Finally, you need to copy the pdf and html folder into your local Windows by using these two commands:
```
cp -r html /mnt/c/Users/Admin/Downloads
```
```
cp -r pdf /mnt/c/Users/Admin/Downloads
```
Remember to change directory (cd) to the `/htwo-map/docs/build/`, where it has the two folders.
<br/><br/>
**For your information**: In the context of Windows Subsystem for Linux (WSL), `/mnt` is used to access your Windows file system from within WSL. For example, `/mnt/c/` corresponds to your `C:/` in Windows. This allows for easy file sharing between Windows and WSL.

