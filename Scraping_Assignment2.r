install.packages("rvest")
library(rvest)
url <- "https://en.wikipedia.org/wiki/Delimiter-separated_values"
csv_wiki <- read_html(url)
csv_tables <- csv_wiki %>% #%>% means “and then”,
  html_nodes(xpath = "//pre") %>% ##looks for all HTML <pre> blocks on the page.
  #(Wikipedia uses <pre> for text that looks like formatted code or tables.)
  html_text()  #extracts the plain text from those <pre> tags.
csv_table <- csv_tables[1]
write.table(csv_table,
            file = "wikipedia_example_r.csv", #file name
            quote = FALSE, #don’t wrap each line in quotation marks
            col.names = FALSE, #don’t add extra column names
            row.names = FALSE) #don’t add row number
read.csv("wikipedia_example_r.csv")
