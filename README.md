# App-notification
# App Notification (Firebase Project)

This project is a simple cloud-based web app that allows users to upload images and view them. It demonstrates how to integrate multiple cloud services using Firebase.

---

## 🚀 What the Project Does

- Uploads images from the user.
- Stores images securely in the cloud.
- Displays the uploaded images on the web.
- (Optional) Sends notifications or emails when actions happen.

---

## ☁️ Cloud Services Used (4+)

| Service Type       | Firebase Service         | Purpose                                |
|--------------------|--------------------------|----------------------------------------|
| Storage            | Firebase Storage         | Stores uploaded image files            |
| Database           | Firestore (NoSQL DB)     | Saves image metadata (URLs, etc.)      |
| Compute            | Cloud Functions          | (Optional) Sends email or auto-tasks   |
| Hosting            | Firebase Hosting         | Hosts the frontend website             |

---

## 🔗 How They Connect

1. The frontend (HTML + JS) is hosted via **Firebase Hosting**.
2. When an image is uploaded:
   - It is stored in **Firebase Storage**.
   - The download URL is saved in **Firestore**.
3. The app fetches the saved URLs from **Firestore** to display images.
4. (Optional) A **Cloud Function** can be used to send an email when a new image is uploaded.

---

## 🛠️ How to Run the Project

### Requirements:
- Node.js
- Firebase CLI
- Git
- GitHub account

### Setup Steps:

```bash
# Clone the repo
git clone https://github.com/swar071005/App-notification.git

# Go into the project folder
cd App-notification

# Install Firebase CLI if not already
npm install -g firebase-tools

# Login to Firebase
firebase login

# Initialize Firebase (if not yet)
firebase init

# Deploy the site
firebase deploy
