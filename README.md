# `Clearcut App`

ClearCut is a simple and intuitive web app built with Streamlit that allows users to upload an image and instantly remove its background using AI.  
It is powered by [`rembg`](https://github.com/danielgatis/rembg), a deep learning-based background removal tool that uses U-2-Net for high-quality results.

---

## Demo

Watch the demo video [here](demo/demo.mp4)

---

## Features

- Upload an image (PNG, JPG, JPEG)  
- Remove background instantly using `rembg`  
- Preview original and background-free images  
- Download the result as `image.png`

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/ahmdeltoky03/clearcut-app.git
cd background_removal_app
```

2. **Create and activate a virtual environment**
```bash
python -m venv env
source env/Scripts/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the App**
```bash
streamlit run app.py
```

---

## Collaboration

Contributions, suggestions, and improvements are welcome.

If you'd like to contribute to this project, please follow these steps:
1. **Fork** the repository  
2. **Create a new branch** for your feature or bugfix  
3. **Commit** your changes with a clear description  
4. **Push** your work to a new branch  
5. **Open a Pull Request** with a description of your changes

---

## License

This project is licensed under the Apache License 2.0.
