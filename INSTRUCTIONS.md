# 📋 Instructions

This document provides step-by-step instructions for using the marifl_crawling tool to scrape Bookdown websites and other documentation sites.

## 🚀 Quick Start

### 1. Installation
```bash
# Clone the repository
git clone https://github.com/marifl/marifl_crawling.git
cd marifl_crawling

# Install with uv (recommended)
uv sync
uv run crawl4ai-setup

# Install as global tool
uv tool install .
```

### 2. Basic Usage
```bash
# Crawl a Bookdown site to Markdown
scrwl -u https://r4ds.had.co.nz/index.html -o ./my_book -f md -d 1.0 -c

# Crawl with clean output (removes navigation)
scrwl -u https://bookdown.org/yihui/rmarkdown/index.html -o ./output -f md -c -N
```

## 📚 Step-by-Step Tutorial

### Step 1: Choose Your Target Website
- **Bookdown sites** work best (this tool was designed for them)
- Look for sites with structured chapter navigation
- Examples: R4DS, Bookdown examples, academic books

### Step 2: Set Up Your Command
```bash
scrwl -u [URL] -o [OUTPUT_DIR] -f [FORMAT] [OPTIONS]
```

**Required Parameters:**
- `-u` / `--url`: The starting URL (usually the index page)
- `-o` / `--output`: Where to save files (e.g., `./my_book`)
- `-f` / `--format`: Either `html` or `md`

### Step 3: Choose Your Options

**Recommended for Bookdown:**
```bash
scrwl -u URL -o DIR -f md -d 1.0 -c -N
```

**What each option does:**
- `-d 1.0`: Adds 1 second delay between requests (be respectful!)
- `-c`: Clean output (removes scripts, styles, meta tags)
- `-N`: No navigation (removes sidebar/nav elements)
- `-s`: Skip existing files (useful for resuming)
- `-n`: Dry run (see what would be crawled without downloading)

### Step 4: Advanced Filtering

**Filter specific chapters:**
```bash
# Only chapters containing "introduction" or "data"
scrwl -u URL -o DIR -f md -fil "introduction|data"

# Only numbered chapters 1-5
scrwl -u URL -o DIR -f md -fil "chapter-[1-5]"
```

**Limit number of pages:**
```bash
# Only first 10 pages
scrwl -u URL -o DIR -f md -m 10
```

## 🎯 Common Use Cases

### Academic Books
```bash
# Complete book with clean output
scrwl -u https://example.bookdown.org/book/ -o ./academic_book -f md -d 1.5 -c -N

# Only specific chapters
scrwl -u https://example.bookdown.org/book/ -o ./chapters -f md -fil "introduction|methodology|conclusion"
```

### R Documentation
```bash
# R for Data Science
scrwl -u https://r4ds.had.co.nz/index.html -o ./r4ds -f md -d 1.0 -c -N

# R Markdown Guide
scrwl -u https://bookdown.org/yihui/rmarkdown/index.html -o ./rmarkdown_guide -f md -d 1.0 -c
```

### Large Documentation Sites
```bash
# Resume interrupted crawl
scrwl -u https://large-docs.example.com -o ./docs -f md -s -d 2.0

# Test first (dry run)
scrwl -u https://large-docs.example.com -o ./docs -f md -n
```

## 🔧 Troubleshooting

### Common Issues

**"Browser executable not found"**
```bash
# Run the setup command
uv run crawl4ai-setup
```

**"Rate limited / Too many requests"**
```bash
# Increase delay between requests
scrwl -u URL -o DIR -f md -d 3.0
```

**"Timeout errors"**
```bash
# Increase timeout
scrwl -u URL -o DIR -f md -t 60
```

**"Command not found: scrwl"**
```bash
# Install as global tool
uv tool install .

# OR use with uv run
uv run scrwl -u URL -o DIR -f md
```

### Getting Help
```bash
# Show all options
scrwl --help

# Show version info
scrwl --version
```

## 📂 Understanding Output

After crawling, you'll get:
```
your_output_directory/
├── index.json          # Machine-readable index
├── README.md           # Human-readable overview
├── 00_Introduction.md  # Numbered content files
├── 01_Chapter_One.md
├── 02_Chapter_Two.md
└── ...
```

**Files are automatically:**
- ✅ Numbered in correct order
- ✅ Named based on chapter titles
- ✅ Cross-linked internally
- ✅ Cleaned of navigation/scripts (if `-c` used)

## ⚡ Pro Tips

1. **Always start with a dry run** (`-n`) to see what will be crawled
2. **Use delays** (`-d 1.0`) to be respectful to servers
3. **Clean output** (`-c -N`) for better reading experience
4. **Filter wisely** (`-fil`) to get only what you need
5. **Resume interrupted crawls** with `-s` flag

## 🚨 Important Notes

- **Respect websites**: Use appropriate delays, don't overload servers
- **Check robots.txt**: Make sure crawling is allowed
- **Legal compliance**: Only crawl content you have permission to access
- **Attribution**: Remember to credit original sources

## 📞 Need Help?

- Check the main [README.md](README.md) for detailed documentation
- Look at [troubleshooting section](#-troubleshooting) above
- Open an issue on GitHub for bugs or feature requests
