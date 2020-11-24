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
Your system is ready to brew.
```

3. Now you can install python 3 by running the command:
```
brew install python3
```
You can check whether python3 has been successfully installed by:
```
$ python3 --version
Python 3.8.5
```
You can switch to python2 by running the command:
```
$ python
Python 2.7.17
```

# Installation
1. Download [brat installation package](http://weaver.nlplab.org/~brat/releases/brat-v1.3_Crunchy_Frog.tar.gz)

2. Unzip the package, then open terminal and go to the unzipped folder. For instance, if you put the folder (whose name is "brat-v1.3_Crunchy_Frog") in Desktop, then you may run:
```
$ cd Desktop/brat-v1.3_Crunchy_Frog
```

3. Run the install shell script
```
$ ./install.sh -u
```
It should prompt you to answer the following three questions:
Please the user name that you want to use when logging into brat
(Enter your username)
Please enter a brat password (this shows on screen)
(Enter your password)
Please enter the administrator contact email
(Enter your email)

4. Run the standalone.py file
```
$ python standalone.py
```
It should provide a link to brat, which looks like
```
Serving brat at http://127.0.0.1:8001
```

5. Open the brat link in your web browser (Chrome would be the best choice). Move your mouse to the blue chunk on the top, and click "Login". Enter your username and password you just set in your terminal during the installation. Then you're ready to go.

More details about putting new data in brat data folder could be found in [their official instruction](https://brat.nlplab.org/installation.html).


