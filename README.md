# Person-Reidentification
Person Reidentification
Requirements- opencv(cv2), tensorflow , flask, numpy
In this project there are two options –
1)Reid between video(reference) and image(query)
2)Reid between 2 videos(reference and query)
Base Approach-
The video is split into frames using open cv and then opencv dnn module and caffemodel are used to detect human in the frame. Image is cropped and then fed to resnet-50 human feature embedding extractor to get a feature vector.
Approach for 1-
First we generate feature vector of Query image.
Video is processed using base approach. While processing each frame’s vector is compared with query image vector.
Approach for 2-
First we process reference video using base approach.
Then Query Video is processed using base approach. While processing each frame’s vector is compared with all image vectors from the reference video.
Note- 
•	Make a “Output_Videos” and “Identity_Gallery” folder in the project folder.
•	Output videos are saved in Output_Videos folder
•	All images generated are stored in Identity_Gallery.(Please clear this folder before running the project otherwise it may throw error)
To Run the Project- 
•	Download model from this link- https://drive.google.com/file/d/11dklDGtuleZBBQE00EJLACdGkPeZY32K/view?usp=sharing   and put it in the “main” folder
•	Run app.py 
•	Go to the server and then put the path to the reference video and path to the query video/image.


