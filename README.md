CURRENTLY UNDER WORK
a lot of this project is vibe coded (i am using this as an opportunity to learn new things)

# 🌅 CircadianRGB

Automatically changes your OpenRGB lighting throughout the day with smooth transitions.

---

## Features

- 🌸 Time-based theme switching
- 🌅 Smooth color interpolation
- 💡 Brightness interpolation
- 🎨 YAML configurable themes
- ⚡ OpenRGB SDK support
- 🐧 Built for Linux

---

## Demo

Current themes:

Day (Sakura)

- GPU/RAM/Cabinet → Warm Sakura Pink
- Fans/AIO → Soft Light Pink
- Brightness → 92%

Night (Crimson)

- GPU/RAM/Cabinet → Deep Crimson Red
- Fans/AIO → Dark Wine Red
- Brightness → 30%

Transition duration:
- 120 seconds
- 30 FPS interpolation

---

## Folder Structure

```
CircadianRGB/
│
├── rgb/
│   ├── controller.py
│   ├── renderer.py
│   ├── animator.py
│   ├── theme.py
│   ├── state.py
│   └── colors.py
│
├── themes/
│   ├── sakura.yaml
│   └── crimson.yaml
│
├── daemon.py
├── config.yaml
└── README.md
```

---

## Installation

```bash
git clone https://github.com/CO1DBYT3/CircadianRGB.git
cd CircadianRGB

pip install -r requirements.txt
```

---

## Roadmap

- [x] Theme loader
- [x] Color interpolation
- [x] Brightness interpolation
- [x] Renderer
- [ ] Automatic sunrise/sunset
- [ ] KDE Night Light integration
- [ ] GUI
- [ ] Windows support
- [ ] Packaging

---

## Built With

- Python
- OpenRGB SDK
- PyYAML

---

## License

MIT
