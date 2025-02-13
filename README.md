# HPV Vaccine Design – In Silico Fusion Protein Pipeline

This repository contains the code and documentation for an in silico pipeline aimed at designing a novel recombinant fusion protein as a candidate vaccine against HPV. The project is based on the work described in:

**In silico approach for designing a novel recombinant fusion protein as a Candidate Vaccine against HPV**

## Project Overview

The pipeline comprises several stages:

1. **Sequence Design:**  
   - Retrieve protein sequences (HPV16 E6, HPV16 E7, and the N-terminal domain of GP96).
   - Join the antigen and adjuvant using a flexible 8×G (GGGGGGGG) linker.

2. **Physicochemical Analysis:**  
   - Calculate molecular weight, isoelectric point, instability index, aliphatic index, and GRAVY using tools such as Expasy ProtParam.

3. **Secondary Structure Prediction:**  
   - Predict secondary structure using GOR4 or similar tools.

4. **3D Model Construction & Validation:**  
   - Generate 3D models via SWISS-MODEL.
   - Validate and refine the models using ProSA-web, ERRAT, and Ramachandran plot analysis.
  
5. **Docking Studies:**  
   - Perform docking studies with TLR2 and TLR4 using SwarmDock and refine models with FireDock.

6. **Codon Adaptation & Cloning Simulation:**  
   - Optimize the fusion construct for expression in E. coli using JCAT.
   - Simulate cloning into an expression vector (e.g., pET28a(+)).

7. **Immunoinformatics Evaluations:**  
   - Predict antigenicity, allergenicity, B-cell epitopes, CTL epitopes, and IFN-γ inducing epitopes using various bioinformatics tools.

## Repository Structure

