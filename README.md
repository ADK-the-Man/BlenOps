# BlenOps
BlenOps is a containerized application that provides the feasibility of rendering the blend files via the pod and containers. Specifically, this project renders a blend file and adds a mp3 file to it enhancing the output to an mp4 file with the 3D name reveal with Audio. 

We have used the blender image from the linuxserver/blender and programmed the application using the Flask in Python further exporting the videos to the pod mount (for instance).

**Containerized BlenOps application Image as Docker container:**

![image](https://github.com/user-attachments/assets/743dfbee-b2ba-4732-8354-6396523e2d14)


**UI page to take inputs from the user:**

![image](https://github.com/user-attachments/assets/f7a57609-077a-4b72-bb3b-392206ab1ec9)


**Render component**
![image](https://github.com/user-attachments/assets/b3c569c9-f3a9-4696-a5a5-6af64320f271)
![image](https://github.com/user-attachments/assets/2d5dcca1-79af-4d4c-b723-053359daf3a7)


Output Video: ( Upon Complete Render )

[![Watch the video](https://img.youtube.com/vi/a73resnnQqc/0.jpg)](https://www.youtube.com/watch?v=a73resnnQqc)

[![Watch the video](https://img.youtube.com/vi/F3ZrqtyYn0A/0.jpg)](https://www.youtube.com/watch?v=F3ZrqtyYn0A)

The application works in the local environment and the docker image includes the blender image as a base with the multi-stage architecture. But while deploying in the cloud-based environment, consider using GPU-based node pools for better and faster render results.

Consider best practices and only deploy when you are aware of using the secrets and configuring them with a pod while exposing the blender image to the internet.

Note: Any suggestions/collaborations upon optimizing blender containerization and further enhancing the application code are highly anticipated and encouraged.

#3Dmodelling #BlenOps #3dBlender #Blender #Flask #
