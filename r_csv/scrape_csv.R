# scrape_csv.R
# Scrape an example CSV from Wikipedia and save + verify it

# Install required packages if missing
if (!requireNamespace("rvest", quietly = TRUE)) install.packages("rvest", repos = "http://cran.us.r-project.org")
if (!requireNamespace("stringr", quietly = TRUE)) install.packages("stringr", repos = "http://cran.us.r-project.org")
if (!requireNamespace("readr", quietly = TRUE)) install.packages("readr", repos = "http://cran.us.r-project.org")

library(rvest)
library(stringr)
library(readr)

url <- "https://en.wikipedia.org/wiki/Delimiter-separated_values"
out_csv <- "wikipedia_example_r.csv"
user_agent_str <- "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"

# Fetch the page with a browser-like user agent to avoid 403 errors
page <- read_html(httr::GET(url, httr::user_agent(user_agent_str)))

# Extract all <pre> blocks and their text
pre_nodes <- html_nodes(page, "pre")
pre_texts <- html_text2(pre_nodes)

# Helper: determine if a block looks like CSV
looks_like_csv <- function(x) {
  has_comma   <- str_detect(x, ",")
  has_newline <- str_detect(x, "\n")
  n_lines     <- str_count(x, "\n")
  has_comma && has_newline && n_lines >= 1
}

# Find the first CSV-like block
candidates <- pre_texts[vapply(pre_texts, looks_like_csv, logical(1))]
if (length(candidates) == 0L) stop("No CSV-like <pre> block found.")
csv_text <- candidates[[1]]

# Remove empty lines
csv_lines <- unlist(str_split(csv_text, "\n"))
csv_lines <- csv_lines[nzchar(trimws(csv_lines))]

# Write to CSV
write_lines(csv_lines, out_csv)
cat("Saved CSV to:", out_csv, "\n")

# Read back and print a preview
df <- read_csv(out_csv, show_col_types = FALSE)
print(df)
