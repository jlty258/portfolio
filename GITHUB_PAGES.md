# GitHub Pages Setup

## Option A: Static HTML (Recommended)

The portfolio includes a static landing page at `docs/index.html`.

### Setup Steps

1. Push the `international/portfolio/` directory to a GitHub repository
   (e.g., `jlty258/portfolio` or use existing profile repo)

2. In repository Settings → Pages:
   - Source: Deploy from a branch
   - Branch: `main` / `docs` folder

3. Site will be available at:
   `https://jlty258.github.io/[repo-name]/`

### Repository Structure for GitHub Pages

```
portfolio/          ← repository root
├── docs/
│   └── index.html  ← GitHub Pages entry point
├── README.md
├── resume/
├── architecture/
├── system-design/
├── articles/
├── interview-stories.md
├── linkedin.md
└── cover-letter.md
```

Note: GitHub Pages serves `docs/index.html` but relative links to `.md` files
will render as raw markdown unless using Jekyll. For full markdown rendering,
use Option B.

---

## Option B: Jekyll (Markdown Rendering)

Create `_config.yml` in repository root:

```yaml
title: Guan Chen — Senior Data Platform Engineer
description: Building distributed data infrastructure
theme: jekyll-theme-minimal
plugins:
  - jekyll-relative-links
relative_links:
  enabled: true
  collections: true
```

Move `README.md` content to `index.md` in repository root. Jekyll will render
all markdown files with the theme.

---

## Option C: Profile README

For GitHub profile page (github.com/jlty258), create a repository named
`jlty258/jlty258` with README.md content from `portfolio/README.md`.

---

## PDF Resume Export

Generate PDF from all resumes using the included Python script (no pandoc required):

```bash
python3 scripts/resume_to_pdf.py
```

Output:
- `resume/Senior_US_Resume.pdf`
- `resume/Staff_US_Resume.pdf`
- `resume/Master_Resume.pdf`

Alternative with pandoc (if installed):

```bash
pandoc portfolio/resume/Senior_US_Resume.md \
  -o portfolio/resume/Senior_US_Resume.pdf \
  --pdf-engine=xelatex \
  -V geometry:margin=1in \
  -V fontsize=11pt
```

---

## Deployment Checklist

- [ ] Create GitHub repository
- [ ] Push portfolio directory
- [ ] Enable GitHub Pages from docs/ folder
- [ ] Verify index.html loads correctly
- [ ] Generate PDF resumes with pandoc
- [ ] Update LinkedIn with content from linkedin.md
- [ ] Customize cover letter per target company
