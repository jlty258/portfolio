# Deploy Portfolio to GitHub — jlty258

Account: https://github.com/jlty258

Target repository: **jlty258/portfolio** (does not exist yet — create first)

Pages URL after deploy: **https://jlty258.github.io/portfolio/**

---

## Step 1: Create Repository on GitHub

1. Open https://github.com/new
2. Owner: **jlty258**
3. Repository name: **portfolio**
4. Public
5. Do **not** initialize with README
6. Click **Create repository**

---

## Step 2: Initialize and Push

```bash
cd /Users/jerome/weixin/international/portfolio

git init
git add .
git commit -m "$(cat <<'EOF'
Add engineering portfolio for Senior Data Platform Engineer role.

Includes resumes, architecture docs, system design deep-dives,
articles, interview stories, and GitHub Pages landing page.
EOF
)"

git branch -M main
git remote add origin https://github.com/jlty258/portfolio.git
git push -u origin main
```

Replace `jlty258/portfolio` with your actual repository name.

---

## Step 3: Enable GitHub Pages

1. Repository → Settings → Pages
2. Source: **Deploy from a branch**
3. Branch: **main** → **/docs** folder
4. Save

Site URL: `https://jlty258.github.io/portfolio/`

---

## Step 4: Profile README (jlty258/jlty258)

1. Create repository: https://github.com/new → name **jlty258** (same as username)
2. Copy content from `../profile-readme/README.md`
3. Push to `jlty258/jlty258`

This README appears on https://github.com/jlty258

---

## Step 5: Regenerate PDF Resumes

```bash
python3 scripts/resume_to_pdf.py
```

Generates:
- `resume/Senior_US_Resume.pdf`
- `resume/Staff_US_Resume.pdf`
- `resume/Master_Resume.pdf`

No pandoc required.

---

## Step 6: LinkedIn

Copy content from `linkedin.md` into LinkedIn profile sections.

---

## File Structure

```
portfolio/
├── docs/index.html          ← GitHub Pages entry
├── resume/*.md + *.pdf
├── architecture/
├── system-design/
├── articles/
├── interview-stories.md
├── linkedin.md
├── cover-letter.md
└── scripts/resume_to_pdf.py
```
