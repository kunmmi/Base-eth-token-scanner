# GitHub Setup Guide

## Prerequisites

1. **Install Git** (if not already installed):
   - Download from: https://git-scm.com/download/win
   - Or use: `winget install Git.Git` (if you have Windows Package Manager)

2. **Create a GitHub Account** (if you don't have one):
   - Go to: https://github.com
   - Sign up for a free account

## Steps to Push to GitHub

### 1. Initialize Git Repository

```bash
# Navigate to your project directory
cd C:\Users\kunmi!\Desktop\bot\BearTech

# Initialize git repository
git init

# Add all files (except those in .gitignore)
git add .

# Create initial commit
git commit -m "Initial commit: BearTech Token Analysis Bot"
```

### 2. Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `BearTech` (or any name you prefer)
3. Description: "Telegram bot for cryptocurrency token analysis"
4. Choose **Private** (recommended since it contains bot code)
5. **DO NOT** initialize with README, .gitignore, or license (we already have these)
6. Click "Create repository"

### 3. Connect and Push

```bash
# Add remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/BearTech.git

# Rename default branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

### 4. Set Up Authentication

If you get authentication errors, you'll need to:
- Use a Personal Access Token instead of password
- Or set up SSH keys
- Or use GitHub Desktop (easier option below)

---

## Option 2: Use GitHub Desktop (Easier)

### 1. Install GitHub Desktop
- Download from: https://desktop.github.com/

### 2. Sign in to GitHub
- Open GitHub Desktop
- Sign in with your GitHub account

### 3. Publish Repository
- Click "File" → "Add Local Repository"
- Browse to: `C:\Users\kunmi!\Desktop\bot\BearTech`
- Click "Publish repository"
- Choose name and description
- Make it **Private** (recommended)
- Click "Publish Repository"

---

## Important Security Notes

✅ **Already Done:**
- `.gitignore` file created to exclude sensitive files
- Hardcoded API keys removed from `src/config.py`
- `.env` file is ignored (won't be committed)

⚠️ **Before Pushing:**
- Make sure your `.env` file is NOT committed (it's in .gitignore)
- Never commit actual API keys or tokens
- Consider making the repository **Private** if it contains any sensitive code

---

## After Pushing

Once your code is on GitHub, you can:
- Share the repository with collaborators
- Set up CI/CD pipelines
- Deploy to cloud platforms (Render, Heroku, etc.)
- Track issues and manage the project

---

## Quick Commands Reference

```bash
# Check status
git status

# Add files
git add .

# Commit changes
git commit -m "Your commit message"

# Push to GitHub
git push

# Pull latest changes
git pull

# View commit history
git log
```

