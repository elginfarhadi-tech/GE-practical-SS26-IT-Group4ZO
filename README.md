# Lab Report - V050

## Project Information

- **Practical Course:** General Enginnering Practice 
- **Lab name:** Informatik v50
- **Date:** 27.04.2026
- **Group Members:**  
  - Baris Yaksi
  - Sofia Atti  
  - Qiye Jiang
  - Ze Xen Choong
  - Zohreh Farhadi
- Instructors: Prof. Rasche & J. Schweizer B.Sc.

---

________________________________________
CARLA & YOLOv8 Integration Lab Report - Group 4a (SS26)

-Introduction

This project aimed to connect a simulated self-driving setup with instant image analysis. Through the CARLA platform, a flow of data was built to capture video output from a driver-guided vehicle. That feed then moved into a YOLOv8 model for immediate object detection. Instead of relying on pre-recorded footage, live visuals were tapped directly during operation. With synchronization maintained, the system responded as decisions unfolded in the virtual world. Processing happened frame by frame without delay. While simulation ran continuously, vision tasks kept pace using optimized inference timing. Such integration allowed dynamic responses based on what the camera saw. Not limited to static tests, the method adapted mid-drive. Because inputs changed constantly, outputs reflected real moments in the scenario.
Through real-time tracking - spotting cars, people - we pushed past basic photo analysis while keeping the simulation interface smooth. This step showed how self-driving tech can sense surroundings dynamically, opening paths toward automatic reactions such as sudden stops or crash prevention.
Setup and Tools
A setup based on Windows formed the foundation, where an Anaconda virtual environment handled intricate software requirements. Though dependency management often poses challenges, this approach simplified installation processes across multiple packages. Complexity emerged naturally during configuration, yet isolation through virtualization reduced interference between components. Tools were organized systematically, ensuring that version conflicts remained minimal throughout development tasks.
Carla simulator engine version 0.9.15 or 0.9.16 using carlau e four exe.
anaconda yolo sim environment with python.

-Core Libraries:

Carla, delivered as a .whl file, serves as the main interface for working within the 3D environment - introducing entities into scenes while overseeing sensor operations through its structured functions.
Simulation visuals, driver controls via WASD keys, also interface elements were managed by pygame. The library supported screen updates alongside real-time interaction handling. Rendering tasks ran within its framework, while feedback displays stayed synchronized with user actions. Input processing occurred directly through its event system, maintaining responsiveness throughout. Display layers combined smoothly under its management, ensuring clarity during operation.
Ultralytics supplied YOLOv8 for detecting objects.
Image processing relies on opencv-python, specifically cv2, handling essential color space shifts like RGB to BGR. While other tools exist, this library remains central due to its precision in conversion tasks. Through it, pixel data transforms accurately for downstream analysis. Without such capability, visual inputs would misalign with expected formats. Its role, though narrow, proves foundational in the pipeline.
numpy processed sensor data and managed arrays.
Using pathlib improved flexibility in handling file paths across different operating systems. This adjustment allowed models to load without dependency on specific directory structures. Instead of hardcoding locations, paths adapt during runtime. System independence emerged naturally through object-oriented path management. Flexibility increased while maintaining clarity in navigation logic.
For external models, the lightweight yolov8n.pt (Nano) was chosen because it supports faster processing when used at the same time as the demanding CARLA 3D simulation. Though small in size, this version keeps performance stable under load. Its efficiency helps avoid lag during real-time operation. Since speed matters in dynamic environments, using a streamlined network makes sense. The trade-off between accuracy and response time favors responsiveness here. Thus, integration runs more smoothly without sacrificing essential detection capabilities.

-Exercise Summary

Multi phase integration approach
1. Starting at localhost:2000, the initial link was confirmed. Town01 appeared next, brought in through notebook commands. A Tesla Model 3 came into view afterward, placed by spawn functions. Weather shifted later - adjusted manually - to HardRainNight conditions. Each step followed sequentially, driven by script inputs. Environment tweaks happened one after another, without overlap.
2. Using only basic vision tools, the Pygame display output was separated cleanly from YOLO processing. A three-dimensional pixel grid from Pygame became compatible with OpenCV through format translation. That transformed data then moved into YOLO for analysis. Detection results appeared as outlined regions on still frames along with moving footage. Each stage operated without interference once split apart.
3. In task 3, the Pygame window displays the images of a car and a person, allowing users to drag these images with the mouse, while the code simultaneously captures the screen in real time and uses the YOLO model for target detection and annotation.
The main changes we made for this are as follows:
•    Import and Load: Import numpy, cv2, and the YOLO model, and load the model.
•    Frame Capture and Conversion: Use pygame.surfarray.array3d(surface) to get the three-dimensional pixel array of the Pygame interface. The original array shape is (width, height, color channel).
•    Dimension and Color Adjustment: Use np.transpose(pixels, (1, 0, 2)) to convert the dimensions of the pixels in the Pygame window into an array that OpenCV can process (height, width, color channel). Then, use OpenCV to convert the RGB color space into the BGR format default to OpenCV.
•    Model Inference and Annotation: Pass the processed image frame into the model for processing, and call results[0].plot() to generate the annotated frame containing detection results (such as bounding boxes and labels).
•    Visualization and Interaction: Display the annotated frame in a new window via cv2.imshow, and use cv2.waitKey(1) & 0xFF == ord('q') to implement the logic of exiting the detection window by pressing the 'q' key.

Our logic now lives inside the main manual_control.py file. Rather than using several separate popup windows, we built a unique setup - a "Sandwich Rendering Pipeline." This approach streamlines how visuals are processed. One piece feeds into the next, layer by layer. It runs smoother because steps happen in sequence. Not everything loads at once anymore. Changes flow naturally through each stage. Efficiency improved without adding complexity. The system handles tasks more quietly now. Less clutter appears during execution. What used to interrupt is now embedded. Each part knows when to activate. Synchronization happens behind the scenes
From behind the vehicle, the view changed - now showing our car alongside surrounding traffic (_transform_index = 0). The scene opened up when we adjusted the camera outward. Now motion unfolds across space: driver and context seen together. Position shift made movement patterns clearer. Observation improved once external framing took effect. What was hidden before now came into sight. Perspective moved backward - to watch actions unfold at a distance.
Before drawing the HUD, we pulled the raw Pygame display array directly.
Flipping the axes along with the color channels came first. After that, YOLO processed the frame through inference. Then followed conversion of the labeled output into a format compatible with Pygame surfaces.
Back on the display went the AI-labeled image, followed by an overlay of CARLA’s original interface showing speed and frame rate. Critical driving data stayed visible, unblocked by detection outlines.
Challenges and Learnings
Midway through combining systems, some delays popped up - each fixed as it appeared
One tricky moment involved a recurring ModuleNotFoundError stating 'carla' was missing - even though we were inside what should have been the right environment. It turned out that on Windows, PowerShell tends to stick with the base Python version, ignoring the active conda setup. To sidestep this behavior, execution shifted toward directly calling the specific interpreter linked to our working environment. Instead of relying on shell assumptions, running the full file address - C:\Users\BarisY\anaconda3\envs\yolo-sim\python.exe manual_control.py - ensured accurate linkage.
Despite hardcoded paths causing mobility problems, using yolov8n.pt directly made execution fragile across systems. To fix this, reliance shifted toward dynamic resolution by applying pathlib methods - specifically Path(__file__).resolve() - as suggested in documentation. Now, the model folder is located relative to where the script runs, enabling consistent operation regardless of machine setup.
Image handling varies between Pygame and OpenCV - one orders dimensions by width first, the other by height; one uses RGB, the opposite prefers BGR. When unprocessed visuals from Pygame entered YOLO, detection warped unpredictably. To fix, we realigned arrays using numpy.swapaxes(0, 1), while conversion via cv2.cvtColor(view, cv2.COLOR_RGB2BGR) matched color encoding ahead of analysis.
Pushing to GitHub failed when remote updates caused a conflict. Caught inside Vim after a git pull started an automatic merge prompt. The team stopped the hanging operation using git merge --abort. A smoother path emerged by applying the --no-edit option. This allowed the merge and upload to finish without manual input.

-Conclusion

This project connected common Python artificial intelligence libraries to a detailed three-dimensional simulation environment. Through precise control of the rendering cycle, real-time third-person object monitoring was made possible while keeping the CARLA interface responsive and efficient.
Later upgrades include performance checks. Instead of the Nano version, using YOLOv8 Small (yolov8s.pt) helps track how much speed is lost when accuracy improves. Each test will show frame rate changes alongside detection quality.
Starting with object location data, researchers aim to calculate spacing from the self-driving car to surrounding items by pulling boundary frame positions. This measurement process forms a base layer when designing systems that trigger sudden stops automatically. Getting these spatial figures right matters early on in development work focused on safety-driven responses.

-Appendix

Place yolov8n.pt inside the /model/ folder when running manual_control.py. That file needs to sit one level below the script. Its position matters for correct access later on. The path relies on this setup working properly. Running from another location may cause errors. Adjust placement only if directory links change. Location determines whether loading succeeds.
A picture of your simulator in action could go right here - just drag it into the GitHub readme window if you feel like including one.

-References

Ultralytics Docs YOLOv8 Python Use
CARLA Simulator Python API Documentation
GE Practical SS26 IT Module Exercise 4 Guidelines Lab PDF
