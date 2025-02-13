def main():
    # Typically, you would parse a SWISS-MODEL output file.
    # Here we simulate by reading a summary from a file.
    model_info = {
        "Model_ID": "Model_1",
        "Global Score": -6.04,
        "PDB_File": "data/templates/Model1.pdb"
    }
    print("3D Model Selected:")
    for key, value in model_info.items():
        print(f"{key}: {value}")
    
    # Save a summary table
    with open("results/tables/3d_model_summary.csv", "w") as f:
        f.write("Parameter,Value\n")
        for key, value in model_info.items():
            f.write(f"{key},{value}\n")

if __name__ == "__main__":
    main()
