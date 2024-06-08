# SET UP TO RUN NOTEBOOK ON WINDOWS 10
How to run jupyter notebooks or other python scripts on your local machine.

## INSTALLATION
There are two things that you have to install:
- Download [Ubuntu Windows Subsystem Linux](https://ubuntu.com/desktop/wsl), which helps you run Linux on your Windows terminal.
- Download [Anaconda for Linux 64-Bit (x86) Installer](https://www.anaconda.com/download/success), which helps you create the required environment from the environment.yml file.

## WORKFLOW

### STEP 1: Basic setup

After install Ubuntu WSL, you should open the WSL terminal, without the (base).

Change directory (cd) to where you have installed [Anaconda for Linux 64-Bit (x86) Installer](https://www.anaconda.com/download/success). Firstly, the default directory is at "root", so you should be back to one subdirectory by using:
```
cd ..
```
Then change directory to the place where you installed. In my case, I use the command:
```
cd mnt/c/Users/Admin/Downloads
```
### STEP 2: Install Anaconda on WSL
After change directory to the directory where Anaconda was downloaded, use the command below to start installing Anaconda on WSL terminal: 
```
bash Anaconda3-2024.02-1-Linux-x86_64.sh
```
Now after installing Anaconda, you should have (base) in the your terminal.

### STEP 3: Clone repository
The h2g-africa: clone it using **https** method
```
git clone https://gitlab.oth-regensburg.de/EI/Labore/fenes/energiespeicher/h2g-africa.git
```

### STEP 4: Set up conda environment
At first, you need to have the `environment.yml` file in the repository because h2g-africa does not have the environment file. In my case, I used the [file](https://gitlab.oth-regensburg.de/EI/Labore/fenes/energiespeicher/htwo-map/-/blob/develop/environment.yml) from the hydrogen map project. 
<br/><br/>
Next, I change the directory to h2g-africa, then run `conda env create --file environment.yml` to create the environment. Then, you need to activate it by using `conda activate htwo_map`. Finally, run `snakemake -j 1 all
` to install all the required data. 


### STEP 5: Open the notebooks or scripts
After successfully running snakemake, you can use the `Remote Window` on the bottom-left of [VS Code](https://code.visualstudio.com/Download). Then, click `Connect to WSL` and open the folder **h2g-africa**. 
<br/><br/>
Finally, you can debug any scripts or jupyter notebooks on VS Code. If you would like to run Jupyter Notebook, please remember to select the kernel to `htwo_map` which we already set up before using Anaconda. 
