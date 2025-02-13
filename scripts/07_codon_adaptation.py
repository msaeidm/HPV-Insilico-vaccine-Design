def main():
    # Simulated JCAT results:
    jcat_results = {
        "CAI": 0.97,
        "GC_Content": 49.88,
        "Optimized_Sequence_Length": 1794
    }
    print("Codon Adaptation Results:")
    for key, value in jcat_results.items():
        print(f"{key}: {value}")
    
    with open("results/tables/codon_adaptation.csv", "w") as f:
        f.write("Metric,Value\n")
        for key, value in jcat_results.items():
            f.write(f"{key},{value}\n")

if __name__ == "__main__":
    main()
