---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
classes: research
---

Much of my work concerns the relation between geometry, arithmetic, and spectral theory. I am particularly interested in how these structures shape the statistical behavior of a system. Here are a few of the questions I have been thinking about recently.

## Quantum chaos and Šeba billiards

A central question in quantum chaos is how classical dynamics are reflected in quantum energy levels. The Berry–Tabor conjecture predicts Poissonian statistics for generic integrable systems: at small scales, the levels should look like independent random points. The Bohigas–Giannoni–Schmit conjecture predicts random-matrix statistics for generic chaotic systems, with nearby levels tending to repel one another.

The Šeba billiard tests this picture in a particularly simple way. What happens if we add a single point impurity? Almost every classical trajectory misses the point, so the classical motion is essentially unchanged. A quantum wave does feel it, and the energy levels change.

I study this question on the cubic three-torus, a cube with opposite faces identified. The impurity creates a new eigenvalue between each pair of consecutive distinct Laplace eigenvalues. In recent work, I prove that the gaps between these new levels have a limiting distribution and exhibit strong level repulsion. The law is governed by the arithmetic of sums of three squares and differs from both Poisson and random-matrix statistics. This gives an explicit setting in which arithmetic and a single impurity produce their own spectral statistics.

[Paper](https://arxiv.org/abs/2610.10031) · [PDF]({{ '/files/Seba_fine_v38.pdf' | relative_url }})

<figure class="research-figure research-figure--plot">
  <a href="{{ '/images/research-seba-distribution.png' | relative_url }}" aria-label="Enlarge the simulated Šeba spacing distribution">
    <img src="{{ '/images/research-seba-distribution.png' | relative_url }}" alt="Simulated density of normalized gaps between new eigenvalues, compared with the Poisson density and the GOE Wigner surmise." width="888" height="713" loading="lazy">
  </a>
  <figcaption>A numerical approximation to the spacing law, compared with Poisson and the GOE Wigner surmise.</figcaption>
</figure>

## Exceptional spectrum and spherical density

Spectral gaps connect geometry with dynamics and counting. On a hyperbolic surface, for example, small Laplace eigenvalues influence how quickly correlations decay and how accurately we can count orbit points. Much effort goes into ruling out exceptional eigenvalues, those below $1/4$.

A related question is how many exceptional eigenvalues can occur. As we pass to larger covers of a fixed space, can we show that the exceptional part of the spectrum remains sparse? This is the idea behind the density hypothesis of Sarnak and Xue: the more exceptional a spectral component is, the less often it should occur.

Golubev and Kamber formulated a geometric counterpart to this question, in terms of counting short returns averaged over a cover. In recent work, I prove that their geometric condition implies the spherical density hypothesis for towers of compact locally symmetric spaces, with the same parameter. Together with their converse theorem, this gives an equivalence. Here, the spherical spectrum is the part seen by functions on the locally symmetric space. The result allows us to obtain these density bounds from geometric counting information, including in higher rank.

[Paper](https://arxiv.org/abs/2610.00298) · [PDF]({{ '/files/Spherical_density.pdf' | relative_url }})

## Poissonian correlations

When does a deterministic sequence look random? Take $\alpha n^d$ and keep only the fractional parts. For irrational $\alpha$ and a positive integer $d$, Weyl's theorem tells us that these points are uniformly distributed in the unit interval. But uniform distribution says little about the distances between neighboring points. For that, we need to zoom in to the scale of the average gap, $1/N$ among the first $N$ points.

Correlation functions measure the frequencies of small configurations: pairs, triples, and larger groups of nearby points. The correlations are Poissonian if these frequencies agree, in the limit, with those of independent random points. For $d\geq 2$, this behavior is expected for almost every $\alpha$. Such questions provide arithmetic models for the Poissonian statistics predicted by Berry–Tabor.

In joint work with Nick Rome and Niclas Technau, we prove this prediction for correlations of any fixed order, provided the degree is sufficiently large in terms of that order. This extends the pair-correlation theorem of Rudnick and Sarnak. The general problem, particularly for low-degree polynomials, remains difficult: understanding pairs is only the first step towards understanding the full local statistics.

[Paper](https://arxiv.org/abs/2605.06974) · [PDF]({{ '/files/LRT.pdf' | relative_url }})

<figure class="research-figure">
  <img src="{{ '/images/research-spacings.png' | relative_url }}" alt="Fifty points in each of three examples: equally spaced points, fractional parts of square root of two times n squared, and independent uniform random points." width="1385" height="631" loading="lazy">
  <figcaption>Equal spacing, an arithmetic sequence, and independent random points. Uniform distribution alone does not distinguish their local statistics.</figcaption>
</figure>

## Orbit growth and the spectrum

For a hyperbolic surface, there is a beautiful relation between three things: the growth of an orbit, the bottom of the Laplace spectrum, and the decay of correlations. This lets us use geometric counting information to answer questions about the spectrum and dynamics.

What is the right version of this relation in higher rank? There are now several independent directions in which an orbit can grow. There are also several commuting invariant differential operators, and their simultaneous spectral parameters form the joint spectrum. Both the geometric and spectral information are naturally multidimensional.

In joint work with Tobias Weich and Lasse Wolf, we prove a precise connection between directional orbit growth, sharp polyhedral bounds on the joint spectrum, and the decay of matrix coefficients, which measure correlations under the group action. In particular, we characterize temperedness, the standard decay behavior of these correlations, by a geometric condition: orbit growth must be bounded by half the ambient volume-growth rate in every direction. This confirms a conjecture of Hee Oh and extends the relation between growth and spectrum beyond rank one.

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
