---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
classes: research
---

I am interested in how geometry and arithmetic influence the spectrum of a space, and in the statistical behavior of deterministic systems. Here are a few things I have been thinking about recently.

## Šeba billiards

A single point impurity barely affects classical motion: almost every trajectory misses it. A quantum wave does feel the impurity, and its energy levels change. This is the idea behind the Šeba billiard.

I study a version on the cubic three-torus, which one can think of as a cube with opposite faces identified. Adding the impurity produces one new eigenvalue between each pair of consecutive distinct eigenvalues of the Laplacian. I am interested in the gaps between these new energy levels.

In recent work, I prove that these gaps, normalized to have mean one, have a limiting distribution independent of the fixed interaction parameter. There is strong level repulsion: the proportion of gaps smaller than $s$ is of order $s^5$, with a periodic modulation on a logarithmic scale. The arithmetic of sums of three squares is visible in the limiting law.

[Paper](https://arxiv.org/abs/2610.10031) · [PDF]({{ '/files/Seba_fine_v38.pdf' | relative_url }})

<figure class="research-figure research-figure--plot">
  <a href="{{ '/images/research-seba-distribution.png' | relative_url }}" aria-label="Enlarge the simulated Šeba spacing distribution">
    <img src="{{ '/images/research-seba-distribution.png' | relative_url }}" alt="Simulated density of normalized gaps between new eigenvalues, compared with the Poisson density and the GOE Wigner surmise." width="888" height="713" loading="lazy">
  </a>
  <figcaption>A numerical approximation to the spacing law, compared with Poisson and the GOE Wigner surmise.</figcaption>
</figure>

## Spherical density

On a compact hyperbolic surface, Laplace eigenvalues below $1/4$ are called exceptional. They influence the rate of mixing and the error terms in counting problems. In higher rank there is an analogous notion of exceptional spectrum. I am interested in how much of it can occur as we pass to larger and larger covers of a fixed space.

Density estimates make this question quantitative: the more exceptional a spectral component is, the less often it should occur. The spherical density hypothesis is a precise version of this principle. Here, “spherical” refers to the part of the representation-theoretic spectrum seen by functions on the locally symmetric space.

My result gives a geometric criterion for this hypothesis in towers of compact locally symmetric spaces. The criterion, called the weak injective radius property, controls the average number of short returns in the covers. I prove that it implies spherical density with the same parameter. Together with the converse theorem of Golubev and Kamber, this gives an equivalence between a geometric counting condition and a spectral density bound.

[Paper](https://arxiv.org/abs/2610.00298) · [PDF]({{ '/files/Spherical_density.pdf' | relative_url }})

## Poissonian correlations

Take the sequence $\alpha n^d$ and keep only the fractional parts. For irrational $\alpha$ and a positive integer $d$, these points are uniformly distributed in the unit interval. But this says little about what happens when we zoom in to the scale of the average gap, $1/N$ among the first $N$ points.

Poissonian correlations mean that small configurations of points occur with the same limiting frequencies as they would for independent random points. Pair correlation measures how often two points lie close together; higher correlations keep track of triples and larger configurations.

In joint work with Nick Rome and Niclas Technau, we prove Poissonian correlations of any fixed order for almost every $\alpha$, provided the degree $d$ is sufficiently large in terms of that order. This extends the pair-correlation theorem of Rudnick and Sarnak. A central ingredient is counting solutions to diagonal equations while keeping track of the special solutions lying on smaller-dimensional varieties. These questions are closely related to the Berry–Tabor prediction of Poissonian statistics for generic integrable quantum systems.

[Paper](https://arxiv.org/abs/2605.06974) · [PDF]({{ '/files/LRT.pdf' | relative_url }})

<figure class="research-figure">
  <img src="{{ '/images/research-spacings.png' | relative_url }}" alt="Fifty points in each of three examples: equally spaced points, fractional parts of square root of two times n squared, and independent uniform random points." width="1385" height="631" loading="lazy">
  <figcaption>Equal spacing, an arithmetic sequence, and independent random points. Uniform distribution alone does not distinguish their local statistics.</figcaption>
</figure>

## Growth, spectrum, and temperedness

For a hyperbolic surface, there is a beautiful relation between the growth of an orbit and the bottom of the Laplace spectrum. With Tobias Weich and Lasse Wolf, I studied how this relation extends to higher rank, where growth has several independent directions.

The appropriate spectral object is the joint spectrum of the invariant differential operators: we record several commuting operators together. We prove a precise connection between directional orbit growth, polyhedral bounds on this joint spectrum, and the decay of matrix coefficients, which measure correlations under the group action.

One consequence is a geometric characterization of temperedness, the standard decay behavior of these correlations. It holds precisely when the orbit-growth indicator is bounded by half the ambient volume-growth rate in every direction. This confirms a conjecture of Hee Oh.

[Paper](https://arxiv.org/abs/2402.02530) · [PDF]({{ '/files/LWW2024.pdf' | relative_url }})

<figure class="research-figure research-figure--polyhedral">
  <a href="{{ '/images/research-ww-spectrum.png' | relative_url }}" aria-label="Enlarge the polyhedral spectral bounds">
    <img src="{{ '/images/research-ww-spectrum.png' | relative_url }}" alt="Polyhedral spectral bounds for SL(3,R): a blue outer hexagonal tube and a smaller orange tube, with green spectral planes and a red boundary point." width="1484" height="983" loading="lazy">
  </a>
  <figcaption>For $\mathrm{SL}_3(\mathbb{R})$, the blue tube gives the general bound; orbit growth determines the smaller orange tube. The red point belongs to the spectrum. The imaginary directions are compressed into one axis.</figcaption>
</figure>

<figure class="research-figure research-figure--polyhedral">
  <a href="{{ '/images/research-ww-product.png' | relative_url }}" aria-label="Enlarge the joint spectrum in the product example">
    <img src="{{ '/images/research-ww-product.png' | relative_url }}" alt="Joint spectrum in a product example, showing continuous spectral pieces, a joint eigenvalue, and orange polyhedral bounds." width="1201" height="994" loading="lazy">
  </a>
  <figcaption>A product example: the joint spectrum has both continuous pieces and isolated points. Both figures are from our paper.</figcaption>
</figure>
