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
To validate with high accuracy (over 97%) you need a big and balanced sample set and this set has both. This hypotesis is binary classification of objects:
* leaf with mildew
* leaf without mildew

There is actually a missleading information in this validation that the leaf is healthy. It only state *with or whitout* mildew with a high pression. 
It is also an option that the leaf has mildew but in a verry small amount that there is no human visual trace of it. With that stated this deep learning algorim 
can diffirent these two options within the goal range.\
***Validation*** is made from a seperate folder from the test set. To make an analogy, we dont want to train on laying a puzzel or an iq test and validate our skills 
whit a puzzel or test we alredy done.

The train test and validation ratio is 70%, 20% and 10%. This is an iso standard.  


## Rationale to map the business requirements to the Data Visualizations and ML tasks

## Business requirements
* The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
* The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

#### visually differentiate
As a stake holder there could be beneficial to automate the visually difference of a cherry leaf with and without mildew. Especially in education of new staff.
The difference is made with grayscale, It seams to be the standard to use grayscale. Important to note is that not every colormap converts linear to grayscale.
The difference in hard to interpret, the dark part part is where images are similar and the brighter where it differs.      


#### Predicting algorithm
This algorithm analyse nominal categorical variable of leaves with mildew mold or without mildew. This it does in range of the business requirements.
Healthy is on the other hand an ordinal categorical variable and could be a consideration for the streakholders but could be difficult to measure.
If there are other visual diseases this framework can expand its nominal categories to handel that. 

##### CNN
This algorithm is done with tensorflow keras. It is a self improving algorithm loosely based on neural synapse, where every synapse (node) has a weight, threshold, bias and memory conected to it. This recognition algorithm brakes down the images to grids and within the grids create smaller grids. In the smaller grid the algorith looks for Q-points. This then tries to find symmetries in the walk between the points. This "walk" uses ReLu which is a linear activation for the walk between points. ReLU is the most commonly used activation function in neural networks. \
If the "walk" or cycle does not give you the targeted symmetry it will not keep it in memory or "lose" the pattern. The nodes can be layed deep or borad, this one ins made deep. Today (2022-05-12) there are no certain optimized pattern for this. Therefore I tryed *Stirling numbers of the first kind*  with 2 disjoint cycles. With some crunching of the numbers I found the sum could be derived by the kormula (n-a)!sum(_k=1 to ^ k=(n-1)) of (1/k). Example [5/2] = 50 and 50 = ( 4!( 1 + 1/2 + 1/3 + 1/4 )) = 24 + 12 + 8 + 6. This gave me realive good result, even if the Dense layer in the Flatten part was really low. There was a big spread in the result in lower numbers and I did not found any conection between Stirling numbers and Flatten Dense numbers. however I kept that number high becouse the spread of infected leaves can vary and a good result of an uncertain leaf is more important than speed in this case.               



## ML Business Case
Business idea was created by the steakholders. There ide was to study the visual diffirence between healthy and unhealthy leaves \
with the hypothesis that the diffirence could be accurate identify by a computer with over 97% match rate. \
The data understaning was derived and well sorted by the theam of Code Institute. The model of a deep convolving neural networks \
eliminate the null hypothesis and showed good result. The output data was shown by a streamlit dashboard and deployed on heroku \
for employees to ease there repetitive workload. Next up is for the steakholders to derive the deductive cycle. 


## Dashboard Design
* List all dashboard pages and its content, either block of information or widgets, like: buttons, checkbox, image, or any other item that your dashboard library supports.
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

matplotlib shows a png fil over seaborn barplot of the train validation and test sets. Next is two \
dot-line plots of the model history in png shown by matplotlib. \
Next is three streamlit checkbox, the first two will show you text about the deep layers and last is a \
pandas DataFrame opened up by streamlits dataframe.
 



## Unfixed Bugs
* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

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
* Here you should list the libraries you used in the project and provide example(s) on how you used these libraries.


## Credits 

* In this section you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign up page are from This Open Source site
- The images used for the gallery page were taken from this other open source site



## Acknowledgements (optional)
* In case you would like to thank the people that provided support through this project.
