## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We created then a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains +4 thousand images taken from client's crop fields. The images show cherry leaves that are healthy and cherry leaves that contain powdery mildew, which is a fungal disease that affects a wide range of plants. The cherry plantation crop is one of their finest products in the portfolio and the company is concerned about supplying the market with a product of compromised quality.



## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is to manually verify if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If it has powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees located in multiple farms across the country. As a result, this manual process is not scalable due to time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that is capable of detecting instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project to all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


* 1 - The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy and that contains powdery mildew.
* 2 - The client is interested to predict if a cherry leaf is healthy or contains powdery mildew.



## Hypothesis and how to validate?
#### Hypothesis
* With a high accuracy separate leaves with mildew from leaves without mildew infect with an AI.

#### Validation
To validate with high accuracy (over 97%), you need a big and balanced sample set and this set has both. This hypotesis is a binary classification of objects:
* leaf with mildew
* leaf without mildew

There is actually misleading information in this validation of whether the leaf is healthy. It only states *with or whitout* mildew with a high presicion. 
There is also an option that the leaf has mildew but in a very small amount where there is no human visual trace of it. With that stated, this deep learning algoritm 
can differentiate from these two options within the goal range.\
***Validation*** is made from a seperate folder from the test set. This force the algorithm to get the result of pattern recognition rather than memorising.  

The train test and validation ratio is 70%, 20% and 10%. 


## Rationale to map the business requirements to the Data Visualizations and ML tasks

## Business requirements
* The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
* The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

#### visually differentiate
As a stake holder it could be beneficial to automate the visual differences between a cherry leaf with and without mildew. Especially in education of new staff.
The difference is made with grayscale, It seams to be the standard to use grayscale. Important to note is that not every colormap converts linear to grayscale.
The difference is hard to interpret, the dark part part is where images are similar and the brighter to where it differs.      


#### Predicting algorithm
This algorithm analyses nominal categorical variable of leaves with mildew mold or without mildew. This it does in range of the business requirements.
Healthy is on the other hand an ordinal categorical variable and could be a consideration for the steakholders but could be difficult to measure.
If there are other visual diseases, this framework can expand its nominal categories to handle that. 

##### CNN
This algorithm is done with tensorflow keras. It is a self-improving algorithm loosely based on neural synapse, where every synapse (node) has a weight, threshold, bias and memory conected to it. This recognition algorithm brakes down the images to grids and within the grids create smaller grids. The grid size is a 3 x 3 pixel grid set by kernel_size. In the grid the algorith looks for Q-points and picks out one point in every kernal. A functions rescales the grid saving only the Q-points (MaxPooling2D). Then tries to find symmetries in the walk between the points. This "walk" uses ReLu which is a linear activation for the walk between points. ReLU is a commonly used activation function in neural networks. \
If the "walk" or cycle does not give you the targeted symmetry it will not keep it in memory or "lose" the pattern. The nodes can be laid deep or broad, this one is made deep. Today (2022-05-12) there are no certain optimized patterns for this. Therefore I tried *Stirling numbers of the first kind*  with 2 disjoint cycles. With some crunching of the numbers I found the sum could be derived by the kormula (n-a)!sum(_k=1 to ^ k=(n-1)) of (1/k). Example [5/2] = 50 and 50 = ( 4!( 1 + 1/2 + 1/3 + 1/4 )) = 24 + 12 + 8 + 6. This gave me a relatively good result, even if the Dense layer in the Flatten part was really low. There was a big spread in the result in lower numbers and I did not find any connection between Stirling numbers and Flatten Dense numbers. however I kept that number high because the spread of infected leaves can vary and a good result of an uncertain leaf is more important than speed in this case.               


## ML Business Case
Business idea was created by the steakholders. There ide was to study the visual diffirence between healthy and unhealthy leaves \
with the hypothesis that the diffirence could be accurate identify by a computer with over 97% match rate. \
The data understaning was derived and well sorted by the theam of Code Institute. The model of a deep convolving neural networks \
eliminate the null hypothesis and showed good result. The output data was shown by a streamlit dashboard and deployed on heroku \
for employees to ease there repetitive workload. Next up is for the steakholders to derive the deductive cycle. 


## Dashboard Design

#### Sidebar

The sidebar contains of 5 checkboxes: 
* box1: Quick Project Summary
* box2: Leaves Visualizer
* box3: Mildew Detection
* box4: Project Hypothesis
* box5: ML Performance Metrics

The design is streamlits default and the sidebar will colapse going to table size (768px).


##### box1: Quick Project Summary
Package of use: 
* streamlit

The user (employee) will be briefed on how to get started and the quality of the outcome.\
A Info button gives more info about business requiraments, machine learning content and a link to this REAMDME file.



##### box2: Leaves Visualizer
Package of use: 
* streamlit
* matplotlib

There are three checkbox alternatives:
* Difference between average and variability image:
    * matplotlib shows average of 20 leaves image in both categories.
* Differences between average unhealthy and average healthy leaf
    * matplotlib show difference between the two categories
* Image Montage
    * randomly show images from selected category in a 3x3 with matplotlib subplot.\
        The category is chosen from a selectbox and is been executed buttom


##### box3: Mildew Detection
Package of use: 
* streamlit
* PIL
* numpy
* plotly
* pandas

Here evaluation of new unclasificated content will be classified by the built in AI. \
The design is clean with an streamlits file_uploader
The result shown is an info text, the uploaded imgage and an plotly bar followed by an success text and a table, both showing the result.\
Last but not least is an HTML `<a>` Tag to download the result in a csv file. 
 


##### box4: Project Hypothesis
Package of use:
* streamlit 

The project hypothesis is show in a success box. 


##### box5: ML Performance Metrics
Package of use:
* streamlit
* matplotlib
* pandas

matplotlib shows a png fil over seaborn barplot of the train, validation and test sets. Next is two dot-line plots of the model history in png shown by matplotlib. 
Next is three streamlit checkbox, the first two will show you text about the deep layers and last is a \
pandas DataFrame opened up by streamlits dataframe.
 



## Unfixed Bugs


## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly in case all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.


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

* This object oriented website layout is made by GyanShashwat1611 at [Github site](https://github.com/GyanShashwat1611/WalkthroughProject01/). His layout is a deep learning on its own. 
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves)
 
### Content 

- The image from the NoteBook_Template was taken from robertdickau.com [stirling1]("https://www.robertdickau.com/stirling1-5-2.png"/)
- The icon in the page favicon were taken from [Twemoji](https://twemoji.maxcdn.com/2/test/preview.html/)



