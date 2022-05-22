## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We created then a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains +4 thousand images taken from the client's crop fields. The images show cherry leaves that are healthy and cherry leaves that contain powdery mildew, which is a fungal disease that affects a wide range of plants. The cherry plantation crop is one of their finest products in the portfolio and the company is concerned about supplying the market with a product of compromised quality.



## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is to manually verify if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If it has powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that is capable of detecting instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project in all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


* 1 - The client is interested to study differentiate a cherry leaf that is healthy from the ones that contain powdery mildew.
* 2 - The client is interested to predict if a cherry leaf is healthy or contains powdery mildew.



## Hypothesis and how to validate?
#### Hypothesis
* With a high accuracy separate leaves with mildew from leaves without mildew infection with help of an ML model.

#### Validation
To validate with high accuracy (over 97%), you need a big and balanced sample set and this set has both. This hypothesis is a binary classification of objects:
* leaf with mildew
* leaf without mildew

There is misleading information in this validation of whether the leaf is healthy. It only states *with* or *without* mildew with high precision. 
There is also an option that the leaf has mildew but in a very small amount where there is no human visual trace of it. With that stated, this deep learning algorithm 
can differentiate between these two options within the goal range.\
***Validation*** is made from a separate folder from the test and training set. This force the algorithm to get the result of pattern recognition rather than memorizing. 

The train test and validation ratio is 70%, 20%, and 10%. 



## Rationale to map the business requirements to the Data Visualizations and ML tasks

## Business requirements
* The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
* The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

#### visually differentiate
As a stakeholder, it could be beneficial to automate the visual differences between a cherry leaf with and without mildew. Especially in the education of new staff.
The difference is made with grayscale, It seems to be the standard to use grayscale. Important to note is that not every colormap converts linear to grayscale.
The difference is hard to interpret, the dark part is where images are similar and the brighter to where it differs.      


#### Predicting algorithm
This algorithm analyses the nominal categorical variable of leaves with mildew mold or without mildew. This it does in the range of the business requirements.
Healthy is on the other hand an ordinal categorical variable and could be a consideration for the stakeholders but could be difficult to measure.
If there are other visual diseases, this framework can expand its nominal categories to handle that.



## ML Business Case
The business idea was created by the stakeholders. Their idea was to study the visual difference between healthy and unhealthy leaves \
with the hypothesis that the difference could be accurately identified by a computer with over 97% match rate. \
The data understanding was derived and well sorted by the team of Code Institute. The model of deep convolving neural networks \
eliminate the null hypothesis and showed good results. The output data was shown by a streamlit dashboard and deployed on Heroku \
for employees to ease their repetitive workload. Next up is for the stakeholders to derive the deductive cycle. 


## Data Understanding
* Images were collected by Code Institute 
* Images are equally balanced with "healthy" and "non-healthy" leaves
* All images is uniformed at: 256,256,256,3

A shape is relative to its geometric viewpoint. To simulate different viewpoints the images pass through an augmentation, simulating different viewpoints by stretching, rotating, and zooming.  
This is done by ImageDataGenerator from Keras TensorFlow.  

*Data understanding* is an important step in crisp-dm and for this target, if a leaf is healthy or not, there is no more indexing required to analyze before modeling. Future questions for the farm could be:
* The differences between leaves of plants on the farms
    - Can the algorithm trained on charry-leafs directly be used on other species of plants
* How does the leaf differ in seasons
    - Is there a time in the season when the algorithm won't work as expected


## Modeling 
Package of use: 
* tensorflow
* keras

The model is a Sequential function from TensorFlow.Keras. The sequence contains two important building blocks
* Feature Learning 
* Classification
and is sometimes called Hidden Layers. The engine of the hidden layers contains: 
* Nodes  
* Edges
where nodes represent mathematical operations and edge multidimensional data arrays also called *tensors*.

## Node 
Nodes differ between nodes in *Feature Learning* and nodes in *Classification*.
In Feature Learning filters search the image for:
- vertical lines 
- horizontal lines
- tilted lines 
- color differences 
- other

They are 24 filters in the first layer and each filter (kernel) focuses on a specific target.
Kernal filter for vertical lines could look like this:

**Red Filter**              

| 1 | 0 | -1 |              
--------------          
| 1 | 0 | -1 |              
--------------                        
| 1 | 0 | -1 |

*and* 

**Green Filter**

| 1 | 0 | -1 | 
-------------- 
| 2 | 0 | -2 |
--------------  
| 1 | 0 | -1 |  

*and*

**Blue Filter**

| 3  | 0 | -3  |
---------------- 
| 10 | 0 | -10 |
----------------
| 3  | 0 | -3  |


* *note that odd size matrix (3x3, 5x5, ..) has a middle point and is a standard to use*
Every filter creates a new multidimensional array. A bias is added and together they are activated by a  ReLu function.
**z = Wa + b**
z = new layer
W = input image 
a = collection of filters
b = bias

Each layer will downsize the image to a compressed image with the important features.
It can help to think of the Feature Learning section as a question section and the classification section is the answer,
hopefully containing the right answer. 

##### Classification
The second part of the Sequential function is the classification, here the multidimensional array flattens to a one-dimensional array, also called a vector. The first vector has the length of the new image size multiplied by the filters. This vector is isomorphically connected to the Dense layer.    
The result is determined by the sigmoid function, its values go from (0,1) and have a symmetric shape. 
Values over .5 will be classified as True, the leaf has mildew, and vice versa.

The final result is saved in the output folder as an h5 file.


## Dashboard Design
The design and color schematics are from streamlit library. Its responsive design and sidebar collapse going to table size at 768px. 

#### Sidebar

The sidebar contains of 5 checkboxes: 
* box1: Quick Project Summary
* box2: Leaves Visualizer
* box3: Mildew Detection
* box4: Project Hypothesis
* box5: ML Performance Metrics


##### box1: Quick Project Summary
Package of use: 
* streamlit

The user (employee) will be briefed on how to get started and the quality of the outcome.\
An Info button gives more info about business requirements, machine learning content, and a link to this README file.



##### box2: Leaves Visualizer
Package of use: 
* streamlit
* matplotlib

There are three checkbox alternatives:
* Difference between average and variability image:
    * matplotlib shows an average of 20 leaves images in both categories.
* Differences between average unhealthy and average healthy leaf
    * matplotlib shows the difference between the two categories
* Image Montage
    * randomly show images from selected category in a 3x3 with matplotlib subplot.\
        The category is chosen from a select box and is been executed buttom


##### box3: Mildew Detection
Package of use: 
* streamlit
* PIL
* numpy
* plotly
* pandas

Here evaluation of new unclasificated content will be classified by the built-in AI. \
The design is clean with a streamlits file_uploader
The result shown is an info text, the uploaded image, and a plotly bar followed by a success text and a table, both showing the result.\
If the uploaded image has a result below 90% certainty, a warning text pops up. 
Last but not least is an HTML `<a>` Tag to download the result in a CSV file. 
 


##### box4: Project Hypothesis
Package of use:
* streamlit 

The project hypothesis is shown in a success box. 


##### box5: ML Performance Metrics
Package of use:
* streamlit
* matplotlib
* pandas

matplotlib shows a png fil over seaborn barplot of the train, validation, and test sets. Next are two dot-line plots of the model history in png shown by matplotlib. 
Next are three streamlit checkboxes, the first two will show you text about the deep layers and the last is a \
pandas DataFrame opened up by streamlits dataframe.
 

## Unfixed Bugs


## Feature Features 
This engine is based on clean data of cherry leaves. During operation, it's unlikely the data will be of the same quality. There might be misunderstandings about using this ML on laves from different species or some images might contain objects not related to leaves. The ML has not been trained to handle that type of data. If the calculated prediction is lower than 90% certainty, a warning text will be added recommending to look over the input data. However, some none leaf objected data will return accuracy above 90% and in an automated farmland, this can lead to fatal outcomes and meme tweets from Elon.   


             


## Deployment
### Heroku

* The App live link is: https://drmaxpower-mildew.herokuapp.com/ 
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select "Heroku Git" and download the Heroku CLI 
3. Download and unpack this Github repository 
https://github.com/DrMaxPower/Mildew-Detection-in-Cherry-Leaves
4. Open the folder in the local code environment
5. Remove static files in .slugignore.
    - ! This command does not work in .slugignore 
        example: *.JPG
                 !inputs/.../validation/*.JPG
        Will not work
6. log in to Heroku from terminal, with 
$ heroku login

7. Heroku git:clone -a username-mildew *safety*
8. cd username-mildew 
9. git add.
10. git commit -am "life is good"
11. git push heroku master



## Main Data Analysis and Machine Learning Libraries
* numpy==1.19.2
    * usede to convert numbers and objects to arrays and operate on them.
* pandas==1.1.2
    * Is used to struckture data. Index data series or a "table" of data in a DataFrames
* matplotlib==3.3.1
    * .pyplot (v. 4.12.0) is used to creat almost all graph plots  
* seaborn==0.11.0
    * seaborn helps "styling and ordering pyplots graphs"
* streamlit==0.85.0
    * Is used to connect frontend and backend fast and easy.  
* tensorflow-cpu==2.6.0
    * Multidimensional array operator building the core of the CNN operations
* keras==2.6.0
    * seting the sequal for the model and hadels operations on the multidimensional arrays


## Credits 

* This object-oriented website layout is made by GyanShashwat1611 at [Github site](https://github.com/GyanShashwat1611/WalkthroughProject01/). His layout is a deep learning on its own. 

* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves)
 
### Content 

- The image from the NoteBook_Template was taken from robertdickau.com [stirling1]("https://www.robertdickau.com/stirling1-5-2.png"/)
- The icon in the page favicon was taken from [Twemoji](https://twemoji.maxcdn.com/2/test/preview.html/)



