# Brat Coreference Project
This is an overview of a coreference project starting from training data preparation to using the trained model for coreference.

# Step1: Annotation with Brat
# 1. Installation
This is a installation tutorial for [brat rapid annotation tool](https://brat.nlplab.org/) on Mac OS.
This tutorial is based on [their official instruction](https://brat.nlplab.org/installation.html).

## Python
Make sure you have python 2 on your device. If you don't have python, please follow the following steps for python 2 installation.

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
brew install python@2
```
You can check whether python3 has been successfully installed by:
```
python --version
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
Python 2.7.9
```
## Brat
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

# 2. Using New Data
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

5. Go to "Colletion" on the top left corner. Go to your new folders and click on the text you want to work on. Start annotating!

6. If you would like to edit the entity, relation, and color of each entity, before annotating you need to do the following:

Find "annotation.conf" and "visual.conf" files. They're both in the /data folder of your brat installation (depending on how your corpora are set up they may be in the same folder as your .txt and .ann files.) Edit these two files as following:

For annotation.conf, if you see this in brat when you select a word: 

![](https://raw.githubusercontent.com/wanxinxie/brat_installation/main/Entity%20type.png)

and see this in brat when you link two words:

![](https://raw.githubusercontent.com/wanxinxie/brat_installation/main/relation.png)

your "annotation.conf" file probably contains the following:

```
[entities]

Person
Organization
Geo-political entity

[relations]

Family
Alias
```

If you would like to add a new entity type, just add the type name on a new line under "[entities]".

Relations are a bit more complicated as they can take a variety of restrictions (e.g., the relation can only exist between entities of particular types).
I believe you can just add another type in the same way as with entity types, but if you want to restrict by type, you can do something like:
```
Family  Arg1:<Person>, Arg2:<Person>
```
or even
```
Family  Arg1:<Person>, Arg2:<Person>, <REL-TYPE>:symmetric-transitive
```
(notice that there should be a tab between Family and the rest of it, not a space)

The "visual.conf" file will then control the corresponding visualization of each entity type. You'll want to add a new line under the [drawing] section to specify a color for the highlighting, like this:
```
Family  bgColor:#EDC1F0
```
(specify your color in [hex notation](https://www.google.com/search?q=color+picker))

(notice that there should be a tab between Family and the rest of it, not a space)



More details  could be found in [their official instruction](https://brat.nlplab.org/installation.html).


