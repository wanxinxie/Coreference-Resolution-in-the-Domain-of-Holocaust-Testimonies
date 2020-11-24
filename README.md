# brat_installation
This is a installation tutorial for [brat rapid annotation tool](https://brat.nlplab.org/) on Mac OS.
This tutorial is based on [their official instruction](https://brat.nlplab.org/installation.html).

# Before Installation
## Python
Make sure you have python 2.5+ on your device. If you don't have python, please follow the following steps for python 3 installation.

1. Open "Terminal", first you can install Xcode by running the command:
```
$ xcode-select --install
```

2. Next you can install Homebrew by running the command:
```
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
You can check whether brew has been successfully installed by:
```
$ brew doctor
```
It should return something like 
```
Your system is ready to brew.
```

3. Now you can install python 3 by running the command:
```
brew install python3
```
You can check whether python3 has been successfully installed by:
```
$ python3 --version
```
It should return something like 
```
Python 3.8.5
```

You can switch to python2 by running the command:
```
python
```
It should return something like 
```
Python 2.7.17
```
# Installation
1. Download [brat installation package](http://weaver.nlplab.org/~brat/releases/brat-v1.3_Crunchy_Frog.tar.gz)

2. Unzip the package, then open terminal and go to the unzipped folder. For instance, if you put the folder (whose name is "brat-v1.3_Crunchy_Frog") in Desktop, then you may run:
```
cd Desktop/brat-v1.3_Crunchy_Frog
```

3. Run the install shell script
```
./install.sh -u
```
It should prompt you to answer the following three questions:
Please the user name that you want to use when logging into brat
(Enter your username)
Please enter a brat password (this shows on screen)
(Enter your password)
Please enter the administrator contact email
(Enter your email)

4. Set up working directory
Allow brat server to read and write data to several directories:
```
mkdir -p data work
```

5. Find your apache group
```
./apache-group.sh
```

If it returns for instance "staff", run the following command:
```
sudo chgrp -R staff data work
chmod -R g+rwx data work
```
Basically it follows
```
sudo chgrp -R ${YOUR_APACHE_GROUP} data work
chmod -R g+rwx data work
```

6. Run the standalone.py file
```
sudo -u USER python standalone.py
```
where USER is your username on your device, and it could be found out by this command:
```
whoami
```
It should provide a link to brat, which looks like
```
Serving brat at http://127.0.0.1:8080
```

# Using New Data
1. Create new folders in brat-v1.3_Crunchy_Frog/data/. Put the text you would like to annotate in the new folders in txt format.

2. Open a new terminal. Go to your brat directory.For instance, if you put the folder (whose name is "brat-v1.3_Crunchy_Frog") in Desktop, then you may run:
```
cd Desktop/brat-v1.3_Crunchy_Frog
```

3. Create ann file for txt files by running the command:
```
find data -name '*.txt' | sed -e 's|\.txt|.ann|g' | xargs touch
```

4. Open the brat link in your web browser (Chrome would be the best choice). Move your mouse to the blue chunk on the top, and click "Login". Enter your username and password you just set in your terminal during the installation. 

5. Go to "Colletion" on the top left corner. Go to your new folders and click on the text you want to work on.

6. Start annotating!

More details  could be found in [their official instruction](https://brat.nlplab.org/installation.html).


