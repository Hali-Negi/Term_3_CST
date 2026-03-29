# Q1: Load the dataset and examine its structure

# Load required libraries
library(tidyverse)


# Examine the structure
glimpse(survey)

# Total number of responses in the original dataset
total_responses = nrow(survey)
cat("Total responses in dataset:", total_responses, "\n")

survey_selected = survey %>%
  select(Age, WorkExp, DevType, AIThreat, ConvertedCompYearly) %>%
  mutate(
    WorkExp = as.numeric(WorkExp),
    ConvertedCompYearly = as.numeric(ConvertedCompYearly)
  )
survey_selected %>%
  pull(Age) %>%
  unique()


survey_selected %>%
  pull(DevType) %>%
  unique()


# Check how many rows have complete data (no NAs in any of our 5 columns)
survey_clean = survey_selected %>% drop_na()

# Count rows after removing NAs
clean_responses <- nrow(survey_clean)
cat("Responses after removing NAs:", clean_responses, "\n")

# Calculate how many rows were removed
rows_removed = total_responses - clean_responses
percent_removed = (rows_removed / total_responses) * 100

cat("Rows removed:", rows_removed, "\n")
cat("Percentage of data removed:", round(percent_removed, 2), "%\n")



# Q2: Age categories exploration

# Create a frequency table for Age
age_freq = survey_clean %>%
  count(Age) %>%
  arrange(desc(n)) %>%
  mutate(Percentage = round((n / sum(n)) * 100, 2))

# Display the frequency table
print(age_freq)

# Find the most common age group
most_common_age = age_freq %>%
  slice(1) %>%
  pull(Age)

cat("\nMost common age group:", most_common_age, "\n")

# Create a bar chart of age distribution
ggplot(survey_clean, aes(x = Age)) +
  geom_bar(fill = "steelblue") +
  labs(
    title = "Distribution of Developers by Age Group",
    x = "Age Group",
    y = "Number of Respondents"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

# Alternative: horizontal bar chart (easier to read long labels)
ggplot(survey_clean, aes(x = reorder(Age, Age, function(x) -length(x)))) +
  geom_bar(fill = "steelblue") +
  coord_flip() +
  labs(
    title = "Distribution of Developers by Age Group",
    x = "Age Group",
    y = "Number of Respondents"
  ) +
  theme_minimal()


# Q3: Exploring Developer Types

# The DevType column has semicolon-separated values like:
# "Developer, full-stack;Developer, back-end;Cloud infrastructure engineer"

# Step 1: Split the DevType column and separate into individual types
dev_types_separated = survey_clean %>%
  # separate_rows splits semicolon-separated values into separate rows
  separate_rows(DevType, sep = ";") %>%
  # Trim any extra whitespace
  mutate(DevType = str_trim(DevType))

# Step 2: Count how many unique developer types exist
unique_dev_types = dev_types_separated %>%
  distinct(DevType) %>%
  nrow()

cat("Number of unique developer types:", unique_dev_types, "\n\n")

# Step 3: Find the top 5 most common developer types
top_5_dev_types = dev_types_separated %>%
  count(DevType, sort = TRUE) %>%
  head(5)

print("Top 5 most common developer types:")
print(n= 5, top_5_dev_types)

# Step 4: Visualize the top 10 developer types
dev_types_separated %>%
  count(DevType, sort = TRUE) %>%
  head(10) %>%
  ggplot(aes(x = reorder(DevType, n), y = n)) +
  geom_col(fill = "steelblue") +
  coord_flip() +
  labs(
    title = "Top 10 Most Common Developer Types",
    x = "Developer Type",
    y = "Number of Respondents"
  ) +
  theme_minimal()

# Optional: Show percentage of total
dev_types_separated %>%
  count(DevType, sort = TRUE) %>%
  mutate(Percentage = round((n / sum(n)) * 100, 2)) %>%
  head(10)


# Q4: Salary summary statistics
# Calculate summary statistics for ConvertedCompYearly
salary_summary = survey_clean %>%
  summarise(
    Mean = mean(ConvertedCompYearly),
    Median = median(ConvertedCompYearly),
    SD = sd(ConvertedCompYearly),
    Min = min(ConvertedCompYearly),
    Max = max(ConvertedCompYearly),
    Q1 = quantile(ConvertedCompYearly, 0.25),
    Q3 = quantile(ConvertedCompYearly, 0.75),
    IQR = IQR(ConvertedCompYearly)
  )

# Display the summary statistics
print("Salary Summary Statistics:")
print(salary_summary)

# Alternative: Use the built-in summary function
cat("\n\nAlternative summary:\n")
summary(survey_clean$ConvertedCompYearly)

# Calculate the difference between mean and median
mean_salary = mean(survey_clean$ConvertedCompYearly)
median_salary = median(survey_clean$ConvertedCompYearly)
difference = mean_salary - median_salary
percent_diff = round((difference / median_salary) * 100, 2)

cat("\n\nMean vs Median Analysis:\n")
cat("Mean salary: $", format(mean_salary, big.mark = ",", scientific = FALSE), "\n", sep = "")
cat("Median salary: $", format(median_salary, big.mark = ",", scientific = FALSE), "\n", sep = "")
cat("Difference: $", format(difference, big.mark = ",", scientific = FALSE), "\n", sep = "")
cat("Mean is", percent_diff, "% higher than median\n")


# Q5 Create a histogram to visualize the distribution of salaries
ggplot(survey_clean, aes(x = ConvertedCompYearly)) +
  geom_histogram(bins = 50, fill = "steelblue", color = "white") +
  labs(
    title = "Distribution of Annual Compensation",
    x = "Annual Salary (USD)",
    y = "Number of Respondents"
  ) +
  theme_minimal() +
  coord_cartesian() 





# Boxplot to show outliers
ggplot(survey_clean, aes(y = ConvertedCompYearly)) +
  geom_boxplot(fill = "steelblue") +
  labs(
    title = "Salary Distribution with Outliers",
    y = "Annual Salary (USD)"
  ) +
  theme_minimal() +
  scale_y_continuous(labels = scales::comma) +
  coord_flip()

summary(survey_clean$ConvertedCompYearly)

# Remove extreme outliers - keep salaries between $10k and $500k
survey_clean_filtered = survey_clean %>%
  filter(ConvertedCompYearly >= 10000 & ConvertedCompYearly <= 500000)



# Now use this filtered dataset for your plots
ggplot(survey_clean_filtered, aes(x = ConvertedCompYearly)) +
  geom_histogram(bins = 50, fill = "steelblue", color = "white") +
  labs(
    title = "Distribution of Annual Compensation",
    subtitle = "Filtered to $10k-$500k range",
    x = "Annual Salary (USD)",
    y = "Number of Respondents"
  ) +
  theme_minimal()

# Q6: How does compensation vary by age group?
# Calculate median salary for each age group

salary_by_age = survey_clean_filtered %>%
  group_by(Age) %>%
  summarise(
    Median_Salary = median(ConvertedCompYearly),
    Mean_Salary = mean(ConvertedCompYearly),
    Count = n(),
    Q1 = quantile(ConvertedCompYearly, 0.25),
    Q3 = quantile(ConvertedCompYearly, 0.75)
  ) %>%
  arrange(desc(Median_Salary))

# Display the results
print("Median Salary by Age Group:")
print(salary_by_age)

# Bar chart of median salary by age
ggplot(salary_by_age, aes(x = reorder(Age, Median_Salary), y = Median_Salary)) +
  geom_col(fill = "steelblue") +
  coord_flip() +
  labs(
    title = "Median Salary by Age Group",
    x = "Age Group",
    y = "Median Annual Salary (USD)"
  ) +
  theme_minimal() +
  scale_y_continuous(labels = scales::comma)



# Box plots to show distribution by age
ggplot(survey_clean_filtered, aes(x = Age, y = ConvertedCompYearly)) +
  geom_boxplot(fill = "steelblue", alpha = 0.7) +
  coord_flip() +
  labs(
    title = "Salary Distribution by Age Group",
    x = "Age Group",
    y = "Annual Salary (USD)"
  ) +
  theme_minimal() +
  scale_y_continuous(labels = scales::comma)

# Statistical test: Is there a significant difference?
# One-way ANOVA
anova_result <- aov(ConvertedCompYearly ~ Age, data = survey_clean_filtered)
cat("\n\nANOVA Test Results:\n")
summary(anova_result)



# Q7: AI Threat Perception Analysis

# Check what the different response categories are
cat("AI Threat Response Categories:\n")
unique_threats <- survey_clean_filtered %>%
  distinct(AIThreat) %>%
  pull(AIThreat)
print(unique_threats)

# Create frequency table for AIThreat
ai_threat_freq <- survey_clean_filtered %>%drop_na() %>%
  count(AIThreat) %>%
  mutate(Percentage = round((n / sum(n)) * 100, 2)) %>%
  arrange(desc(n))

cat("\n\nAI Threat Perception Frequency Table:\n")
print(ai_threat_freq)




# Alternative: Pie chart (though bar charts are usually better)
ggplot(ai_threat_freq, aes(x = "", y = n, fill = AIThreat)) +
  geom_col(width = 1) +
  coord_polar("y") +
  labs(
    title = "Distribution of AI Threat Perception",
    fill = "Threat Level"
  ) +
  theme_void() +
  geom_text(aes(label = paste0(Percentage, "%")), 
            position = position_stack(vjust = 0.5))

# Horizontal bar chart with percentages
ggplot(ai_threat_freq, aes(x = reorder(AIThreat, Percentage), y = Percentage)) +
  geom_col(fill = "steelblue") +
  coord_flip() +
  labs(
    title = "How Threatened Do Developers Feel by AI?",
    x = "Threat Level",
    y = "Percentage of Respondents (%)"
  ) +
  theme_minimal() +
  geom_text(aes(label = paste0(Percentage, "%")), 
            hjust = -0.2, size = 4)

