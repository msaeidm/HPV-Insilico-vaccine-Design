import pandas as pd

def main():
    # Simulated epitope prediction results as a dictionary (or load from files)
    epitopes = {
        "B_cell": [{"Position": "249-268", "Sequence": "GPICSQKPGGGGGGGGMEDD", "Score": 1}],
        "CTL": [{"Rank": 1, "Start": 418, "Sequence": "GTSEFLSKL", "Score": 0.97}],
        "IFN_gamma": [{"Sequence": "GPICSQKPGGGGGGGGMEDD", "Score": 1.66}],
        "MHC_I": [{"Position": 332, "HLA": "B0801", "Sequence": "MMKLIINSL", "Affinity": 9.02, "%Rank": 0.01}],
        "MHC_II": [{"Allele": "DRB4_0101", "Position": 362, "Sequence": "KIRLMSLTDDQALAA", "Affinity": 20.3, "%Rank": 0.60}]
    }
    # Convert dictionaries to DataFrames and save to CSV files
    for key, value in epitopes.items():
        df = pd.DataFrame(value)
        df.to_csv(f"results/tables/{key}_epitopes.csv", index=False)
        print(f"Saved {key} epitope predictions to results/tables/{key}_epitopes.csv")
    
if __name__ == "__main__":
    main()
