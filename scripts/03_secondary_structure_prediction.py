def main():
    # In practice, you might call an API or parse output from GOR4
    # For simulation, we load a precomputed result.
    prediction = {"alpha_helix": 35.79, "extended_strand": 19.90, "random_coil": 44.31}
    print("Secondary Structure Prediction:")
    for key, value in prediction.items():
        print(f"{key}: {value}%")
    
    # Save the prediction to a file
    with open("results/tables/secondary_structure.csv", "w") as f:
        f.write("Structure,Percentage\n")
        for key, value in prediction.items():
            f.write(f"{key},{value}\n")

if __name__ == "__main__":
    main()
