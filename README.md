# Schwarz Methods for Solving the Poisson Equation

This repository contains the code and resources used for the numerical experiments in my bachelor thesis, which focuses on Schwarz methods for solving the Poisson equation. The thesis explores both the restricted additive Schwarz (RAS) and additive Schwarz (ASM) methods, implemented in the FreeFem++ environment, with data processing and analysis done using MATLAB. In the **Schwarz Methods** folder you will find everything you need for the numerical experiments themselves. While in the **Convergence Analysis** folder you will find a python script to display the 1D convergence of Schwarz methods.

## Repository Contents

### Schwarz_Methods

- `Schwarz-Preconditioner.edp`: FreeFem++ script for implementing the ASM method as preconditioner for CG.
- `Schwarz-Solver.edp`: FreeFem++ script for solving the 3D Poisson problem using Schwarz methods, mainly with RAS method, but it is possible to try ASM method.
- `Schwarz-Solver-time.edp`: FreeFem++ script for the time measurement experiment of the RAS method    
- `createPartition3d.idp`: Script for creating overlaps for individual subdomains in 3D.
- `decomp3d.idp`: Script for domain decomposition in 3D.
- `PCG.idp`: Script implementing the preconditioned Conjugate Gradient method.
- `Wheel.mesh`: Mesh file representing the toothed metallic wheel used in the numerical experiments.
- `MoreComplexDomain.mesh`: Mesh file representing the more complex domain used in the numerical experiments.
- `SchwarzPreconditioner.m`: MATLAB script for data processing the Schwarz methods as preconditioner for GMRES and CG methods.
- `SchwarzSolver.m`: MATLAB script for data processing Schwarz methods as stand-alone solvers.    

### Convergence_Analysis

- `1DconvergenceAnalysis.py`: Python script for analyzing the convergence of Schwarz methods in one-dimensional cases.
