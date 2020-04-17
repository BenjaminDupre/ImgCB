# Images: CheckBoard Mask

### What does it do?
The file 'checkmask.py' holds a function that reveals a picture piece by piece, on a particular order, till all 9 pieces are shown. It takes as input: a picture and a digit between 1-9 which stands for the number of piece to show. By varying the number of revealed peaces you can see more or less of the picture. This idea holds as a reference a particular moment of  80's TV television show 'Catch a Phrase'. 

To have an idea of how the show was you can look at the [link](https://www.youtube.com/watch?v=lFhedb2g9jg) :tv:

### Usage
1. You need to download all files from Github by clicking in 'pull or dowload' and download zip file into your define working directory.
2. Unzip the file in the same folder. 
3. Open the terminal
4. Place yourself on yor working directory by entering in the comand line ``` cd ~/ImgCB-master``` where ~ represents you path to the folder.
5. To check if you have all libraries run on terminal ```pip install -r requirements.txt```.
6. Open python by entering ```python```
7. To dynamically execute the python code we enter ```exec(open('checkmask.py').read())```
### Examples:
In the zip file there are two example pictures to ran the function with (greenthumb.jpg and blackmail.jpg). 
Both images where are from Wire Magazine article on Gabriel Zimmers photos. You can watch the article on this [link](https://www.wired.com/story/idioms-photographs/)

* First example: ```python checkmask('greenthumb.jpg',4)```
* Second example: ```python checkmask('blackmail.jpg',7)```
