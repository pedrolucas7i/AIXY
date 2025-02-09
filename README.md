
---

# **AIXY - Intelligent Autonomous Robot with TTS, STT, and Computer Vision**

**AIXY** is an intelligent autonomous robot designed to interact with the environment efficiently, using **Text-to-Speech (TTS)** and **Speech-to-Text (STT)**, as well as computer vision for object recognition and navigation. It combines modern **artificial intelligence** (AI), **autonomous navigation**, and **sensors** to operate independently.

---

## **Features**

- **Full Autonomy**: Capable of performing tasks independently using sensors and AI to perceive and respond to the environment.
- **Natural Interaction**: With **TTS** and **STT** integration, AIXY can speak and understand voice commands.
- **Computer Vision**: Equipped with a USB camera to detect and recognize objects in the environment.
- **Scalability and Flexibility**: The robot's architecture is designed to be easily adaptable to various scenarios and functions.

---

## **Technologies Used**

- **Programming Languages**: Python
- **Hardware Platform**: Raspberry Pi
- **AI Service**: Ollama (using models like Llama3.1:8b and Llava-LLama3)
- **Sensors**: Ultrasonic sensors for distance detection, USB camera for computer vision
- **TTS (Text-to-Speech)**: Uses tools like Google Text-to-Speech or other TTS APIs.
- **STT (Speech-to-Text)**: Integrated with APIs like Google Speech-to-Text or Whisper.
- **Navigation System**: SLAM (Simultaneous Localization and Mapping), Odometry

---

## **Features**

### **1. Autonomous Navigation**
- AIXY can navigate unknown environments and adjust its path as needed, using ultrasonic sensors and cameras to avoid obstacles and optimize routes.

### **2. Image Processing**
- With the USB camera, AIXY is capable of recognizing objects and performing tasks based on computer vision, such recognizing specific objects.

### **3. Voice Communication**
- **TTS**: AIXY can respond to commands or provide information aloud, creating a more interactive experience.
- **STT**: AIXY can understand voice commands from the user and respond appropriately, such as "turn left" or "find one cube"

### **4. Machine Learning**
- AIXY can adapt its behavior based on past interactions and experiences, using supervised or unsupervised learning.

---

## **Installation Instructions**

### **Prerequisites**
- **Raspberry Pi** (version 3 or higher)
- **Python 3.x**
- **Ollama** with models **Llama3.1:8b** and **Llava-LLama3**
- **Google Text-to-Speech** (or other TTS solution)
- **Whisper** for STT

### **Installation Steps**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/YourUsername/AIXY.git
   cd AIXY
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Ollama Server Setup:**
   - Install and configure the Ollama server on a remote machine or server.
   - Ensure the Raspberry Pi can communicate with the server over the network.

4. **Connect hardware devices**:
   - **USB Camera**: Connect the camera to the Raspberry Pi.
   - **Ultrasonic Sensors**: Connect the ultrasonic sensors to the Raspberry Pi.

5. **Configure TTS and STT**:
   - Install Google Text-to-Speech or another TTS solution.
   - Set up Google Speech-to-Text or Whisper for voice recognition.

6. **Run the system:**

   ```bash
   python main.py
   ```


---

## **System Architecture**

### **Folder Structure**

- **/src**: Main source code for AIXY.
- **/docs**: Project documentation.
- **/config**: Configuration files for sensors and modules.
- **/scripts**: Helper scripts for testing and maintenance.

---

## **Contribution**

If you'd like to contribute to the **AIXY** project, feel free to open issues or submit pull requests! Some ways you can contribute include:

- **Report Bugs**: If you encounter issues, please open an issue.
- **Improvements and New Features**: Propose new features or improvements.
- **Documentation**: Help improve the project documentation.

### **Steps to Contribute**

1. Fork this repository.
2. Create a branch for your modification (`git checkout -b my-modification`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push your code to your forked repository (`git push origin my-modification`).
5. Open a pull request explaining your changes.

---

## **License**

This project is licensed under the Proprietary License - see the [LICENSE](./LICENSE) file for more details.

---

## **Contact**

For more information or inquiries, you can contact me via email:  
**pedrolucas dot core7i @gmail.com**

---

### **Example Interaction with AIXY**

- **User** (STT): "AIXY, what's the temperature in the room?"
- **AIXY** (TTS): "The temperature in the room is 22 degrees Celsius."
  
- **User** (STT): "AIXY, stop moving."
- **AIXY** (TTS): "Command received. AIXY stopping movement."

---