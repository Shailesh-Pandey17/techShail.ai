git init 
Create a file named .gitignore in root:
git add .
git commit -m "Initial project setup"

git remote add origin https://github.com/Shailesh-Pandey17/techShail.ai.git

git branch -M main
git push -u origin main

<!-- if rejected -->
git pull origin main --allow-unrelated-histories
git push origin main


# infuture commit 
git add .
git commit -m "your message"
git push

# create 
mkdir nginx
# step1:
#mkdir backend
#cd backend
#python -m venv venv
#venv\Scripts\activate

# step2:
node -v
npm -v

#mkdir frontend
#cd frontend
npx create-next-app@latest .

#npm init -y #package.json  optional
# Run Application
npm start  #Production mode
npm run dev  #Development mode

# dir - backend\app - main.py
uvicorn app.main:app --reload
http://127.0.0.1:8000/health

