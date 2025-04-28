import pandas as pd

def load_covid_data(covid_file_path):
    # Loads the WHO COVID-19 country data.
    covid_df = pd.read_csv(covid_file_path)
    print(f"COVID-19 dataset loaded with {covid_df.shape[0]} rows and {covid_df.shape[1]} columns.")
    return covid_df


def prepare_covid_summary(covid_df):
    # Aggregates COVID-19 data by country.
    covid_df_sorted = covid_df.sort_values('Date_reported')
    country_df = covid_df_sorted.groupby('Country', as_index=False).last()
    country_df = country_df[['Country', 'Cumulative_cases', 'Cumulative_deaths']]
    country_df.rename(columns={
        'Cumulative_cases': 'Total_Cases', 
        'Cumulative_deaths': 'Total_Deaths'
        }, inplace=True)
    return country_df

def load_population_data(population_csv_path):
    # Loads the World Bank population data.
    pop_df = pd.read_csv(population_csv_path, skiprows=4)
    pop_df = pop_df[['Country Name', '2021']]  # Use 2021 population
    pop_df.rename(columns={'Country Name': 'Country', '2021': 'Population'}, inplace=True)
    pop_df.dropna(inplace=True)
    print(f"Population dataset loaded with {pop_df.shape[0]} countries.")
    return pop_df

def merge_datasets(covid_df, pop_df):
    # Merges COVID-19 data with Population data.
    merged_df = pd.merge(covid_df, pop_df, on='Country', how='left')

    # Drop countries without population info
    merged_df = merged_df.dropna(subset=['Population'])

    # Calculate deaths per 100,000 people
    merged_df['Deaths_per_100k'] = (merged_df['Total_Deaths'] / merged_df['Population']) * 100000
    merged_df['Deaths_per_100k'] = merged_df['Deaths_per_100k'].round(2)

    # Optional: Remove extreme outliers (tiny countries with huge death rates)
    merged_df = merged_df[merged_df['Deaths_per_100k'] < 1500]

    print(f"Final merged dataset has {merged_df.shape[0]} countries.")
    return merged_df

def save_cleaned_data(merged_df, save_path):
    # Saves the cleaned final dataset.
    merged_df.to_csv(save_path, index=False)
    print(f"Cleaned data saved at: {save_path}")

if __name__ == "__main__":
    # Paths (update according to your folders)
    covid_file_path = 'data/raw/WHO-COVID-19-global-daily-data.csv'
    population_extract_path = 'data/raw/population_data/'
    population_csv_path = 'data/raw/population data/API_SP.POP.TOTL_DS2_en_csv_v2_19373.csv'
    save_path = 'data/processed/covid_country_summary_final.csv'

    # Run full wrangling pipeline
    covid_df = load_covid_data(covid_file_path)
    covid_summary = prepare_covid_summary(covid_df)
    population_df = load_population_data(population_csv_path)
    final_df = merge_datasets(covid_summary, population_df)
    save_cleaned_data(final_df, save_path)