# GreenTrack

GreenTrack is a waste segregation and recycling support project that includes:
- A static landing site and sign-in flow (`index.html`, `signin.html`, `index2.html`, `admin.html`)
- A Streamlit-based garbage classification app (`app.py`) that predicts waste categories from an uploaded image
- A small Flask redirect service (`flask_server.py`) for the pickup scheduling page
- A pickup scheduling page with points calculation (`schedule.html`)
- Styling and client-side interaction using CSS and JavaScript files

## Project Structure

- `app.py` - Streamlit app for image upload and garbage classification
- `flask_server.py` - Flask server that redirects `/schedule` to `schedule.html`
- `index.html` - Main home page for the GreenTrack frontend
- `signin.html` - Sign-in / sign-up landing page
- `index2.html` - Post-sign-in navigation page to the ML model and scheduling pages
- `schedule.html` - Pickup schedule form with waste amount and points calculation
- `admin.html` - Admin-style view for scheduled pickups
- `styles.css`, `stylesadmin.css`, `styless.css` - Styles for the frontend pages
- `script.js`, `scripts.js` - Frontend JavaScript for page behavior
- `garbage_classification/` - Dataset folder containing labeled waste images by category
- `green-track/package.json` - placeholder package metadata for the web app subfolder

## Requirements

- Python 3.8+ recommended
- `streamlit`
- `tensorflow`
- `numpy`
- `matplotlib`
- `pillow`
- `flask`

> The Streamlit app expects the model file `model_aug_no_sh.h5` to be available in the same directory as `app.py`.

## Setup

1. Open a terminal in the project root (`f:/projects/GreenTrack/GreenTrack`).
2. Create and activate a Python virtual environment:

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

3. Install Python dependencies:

```bash
pip install streamlit tensorflow numpy matplotlib pillow flask
```

4. Confirm the model file is present. If it is missing, place `model_aug_no_sh.h5` in the project root.

## Running the app

### Start the Streamlit model app

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal.

### Start the Flask schedule redirect server

```bash
python flask_server.py
```

The Flask server listens on port `8000` and redirects `/schedule` to `schedule.html`.

## Using the project

- Open `index.html` in a browser to see the main landing page.
- Use `signin.html` to access the post-login page `index2.html`.
- From `index2.html`, click `ML MODEL` to open the Streamlit classifier or `Pickup Schedule Directly` to open `schedule.html`.
- In the Streamlit app, upload a JPEG image to classify garbage and optionally follow the schedule link for pickups.

## Notes

- `admin.html` is a static admin-style dashboard view.
- The `green-track/package.json` file is minimal and does not include build scripts.
- If you want to serve the static frontend from a local HTTP server, you can use a simple static server or serve the folder from your preferred web server.

## GitHub Push

To push this README to GitHub yourself, run:

```bash
git add README.md
git commit -m "Add project README"
git push
```
