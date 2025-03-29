# Spinal Tap Concert Visualizer

## Overview
This repository contains a dynamic Python simulation developed as part of the COMP5005 (Fundamentals of Programming) unit at Curtin University. The project visualizes a rock concert setup for the fictional band **Spinal Tap**, implementing concepts such as object-oriented programming, animation, and data-driven control. 

By using **Matplotlib**, **NumPy**, and **Pillow (PIL)** libraries, the simulation brings to life stage lighting, smoke machines, choreography, props, and audience-facing visuals.

---

## Features
- 🎇 **Dynamic Lighting System**: Five top and five front lights with real-time color and intensity transitions controlled via `lights.csv`.
- 💨 **Smoke Machine Simulation**: Smoke particles are generated and diffused randomly using `stepChange` method for animated realism.
- 🎸 **Customizable Stage Setup**: Includes a band, backdrop, props (e.g., speakers), and layered stage with animated components.
- 🖼️ **Image Overlay**: Imports band, backdrop, and logo images for enriched visual storytelling.
- 🧠 **Modular Design**: Classes for lights, smoke, props, and animations support easy extension and readability.
- 🎞️ **Choreographed Animation**: Uses `FuncAnimation` to simulate frame-by-frame animation of stage visuals.

---

## File Structure
| File | Description |
|------|-------------|
| `spinal-tap.py` | Main script containing all class definitions, plotting logic, and animation loop |
| `lights.csv` | Lighting configuration file with color and intensity values across 100 iterations |
| `REPORT_20972008.pdf` | Detailed report outlining design, implementation, testing, and future work |
| `band.png`, `background.jpg`, `tap-logo.png` | Image assets used in the simulation |

---

## Dependencies
Make sure you have the following Python libraries installed:
```bash
pip install matplotlib numpy pillow
```

---

## How to Run
1. Clone the repository:
```bash
git clone https://github.com/yourusername/spinal-tap-concert-visualizer.git
```

2. Place all required files in the same directory:
   - `spinal-tap.py`
   - `lights.csv`
   - `band.png`, `background.jpg`, `tap-logo.png`

3. Run the simulation:
```bash
python spinal-tap.py
```

This will open a Matplotlib animation window with two subplots:
- Top plot: **Ceiling lights view**
- Bottom plot: **Audience stage view**

---

## Author
**Syed Muhammad Ahmed Zaidi**  
Student ID: 20972008  
Curtin University – COMP5005 (Fundamentals of Programming)

---

## License
This project is licensed under the MIT License.

---

## Acknowledgements
- Practical exercises and tests from COMP5005
- Matplotlib documentation
- Pillow for image processing
- Referenced visuals from public assets (credited in report)

---
