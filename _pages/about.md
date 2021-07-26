---
permalink: /
title: "Homepage"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

As of September 2020, I am a Hill Assistant Prof. (post-doc) at Rutgers university, with research interests in a broad range of topics relating to number theory, dynamical systems, and mathematical physics. Before this I received my PhD at the University of Bristol under the supervision of [Jens Marklof](https://people.maths.bris.ac.uk/~majm/home.html) and [Bálint Tóth](https://sites.google.com/view/balint-toth-math/home). 

In the Fall of 2021 I will be organizing the Rutgers number theory seminar. Feel free to get in contact about possible talks.

**Research Interests**
=====
***Asymptotic Distribution of Thin Group Orbits***

![Apollonian](/images/Apollonian_3.png)

One of the big-picture topics in mathematics, is the charaterization of symmetry. For example, one object with a great deal of symmetry is a *lattice* (think of a square lattice, or a honey-comb hexagonal lattice). Lattices have been studied for hundreds of years, owing in part to their symmetry and place in nature, but also, they give us a useful tool for embedding number theoretic objects (like sequences of numbers) into objects with lots of symmetry. This symmetry allows us to use group theoretic tools to study the lattices, and thus to study the number theoretic objects. 

If we consider lattices, not in our usual Euclidean geometry, but in hyperbolic geometry (i.e geomoetry of the hyperbolic half-plane), then studying these lattices is actually the same as studying matrices ($2\times 2$ matrices in the case of the half-plane). This connection has led to numerous approaches for studying problems in number theory. For example, given a hyperbolic lattice, we can glue together opposite sides to form a hyperbolic manifold. In past $200$ years, mathematicians have learned a great deal about flows on these hyperbolic manifolds. Thus we can understand certain number theoretic problems by using the tools developed to study these hyperbolic manifolds. 

While lattices are particulary useful, owing to the high degree of symmetry, one can ask what happens when we remove some of these symmetries. If done correctly, the resulting object is a so called thin group (or thin group orbit -- see [this review paper](https://www.ams.org/journals/notices/201906/rnoti-p905.pdf) for more information). One should of these as analogous to lattices, but sparser. Here, one can again make a bridge between the study of certain number theoretic problems and the study of corresponding hyperbolic manifolds (the corresponding manifolds now have infinite volume due to the sparsity of the thin group orbits). Thus we again use tools from dynamical systems on hyperbolic manifolds to understand number theoretic problems. This has become a bit of a hot topic at the moment, owing to the ubiquity of these groups, their applications to number theory, and the development of certain tools in this setting. 

One of the projects from my thesis was to study the fine-scale local properties of these thin groups (see [this paper](https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/abs/directions-in-orbits-of-geometrically-finite-hyperbolic-subgroups/62E5FC227B848B7BCD59FD116BE32627)), and certain number theoretic sequences which correspond to thin groups (Farey sequences for thin groups -- see [this paper](https://academic.oup.com/imrn/advance-article/doi/10.1093/imrn/rnab036/6226703?guestAccessKey=2eae1952-4414-47c3-ab69-a5011548af65)). In both of these papers we used techniques from the world of homogeneous dynamics (namely the equidsitribution of expanding horospheres) to understand fine-scale statistics of these objects relating to thin groups. 

In an ongoing project, with [A. Kontorovich](https://sites.math.rutgers.edu/~alexk/), we are trying to use spectral theory of the Laplacian on hyperbolic manifolds, to understand the (rather old) Apollonian counting problem. That is, consider the three mutually tangent (solid line) circles in the image above on the left. Note that there are exactly two circles tangent to all three in the initial configuration (drawn in dotten line). If we add these circles to the configuration we get some new gaps which we continue to fill with circles. Eventually, we end up with the central image. This is an Apollonian packing (named after Apollonius of Perga circa 200 B.C). These circles have fascinated mathematicians (and even the Nobel prize winning chemist, Frederick Soddy, who eulogized them in a [poem](https://www.nature.com/articles/1371021a0)). Our goal in this project is to count the number of circles in this packing with radius larger than some increasing lower bound by extending techniques from spectral theory to new territory.


***Pseudo-Random Properties of Deterministic Sequences***

In the $20^{th}$ century, starting with the work of Weyl, mathematicians became interested in the statistical properties of monomial sequences of the form $(\alpha n^\theta \mod 1 )_{n>0}$ where $\alpha >0$ and $\theta >0$. From a number theoretic point of view there is a natural question one can ask: in the limit as we consider more and more sequence elements, what can be said about the asymptotic distribution of these points? In other words, can we see random behavior emerging from these sequences?

While this question has a natural motivation from a number theory perspective, there is also a deep connection to quantum chaos. Namely, the Berry-Tabor conjecture (See [these notes](https://people.maths.bris.ac.uk/~majm/bib/3ecm.pdf) by [J. Marklof](https://people.maths.bris.ac.uk/~majm/home.html)) hypothesizes a connection between the the chaotic properties of a given system with the pseudo-random properties of the eigenvalues of corresponding quantom analog. These monomial sequences can appear as the eigenvalues of a quantum system, and thus determining the pseudo-random properties can shed light on this deep hypothesized connection in quantum chaos. 

One very strong measure of pseudo-randomness, is the so-called 'pair correlation function'. In [this paper](https://arxiv.org/abs/2106.09800), together with [A. Sourmelidis](https://www.math.tugraz.at/~sourmelidis/) and [N. Technau](https://sites.google.com/view/niclas-technaus-website), we showed that a wide class of these monomial sequences exhibit Poissonian pair correlation. In fact, this is one the only examples where the pair correlation function has been shown to converge to the Poissonian limit for explicit values of $\alpha$ and $\theta$. The paper builds on a methodology outlined in [this paper](https://arxiv.org/abs/2007.09292) which proved convergence of (so-called) 'long-range correlations' (a weaker measure of pseudo-randomness) for some other monomial sequences.

***Lorentz Gas and Non-Interacting Particle Systems***

![Lorentz](/images/Lorentz.png)


<img src="/images/Lorentz.png" width="700" height="250">

In the $19^{th}$ Centruy physicists started to ask a simple question, which gave rise to an entire field of mathematical physics -- statistical mechanics. The question was the following: given a simple model for the movement of atoms, can we see the laws of physics which goven large scale objects by studying large ensembles of these atoms. For example, can we use particle dynamics to derive the heat equation (the equation governing how heat diffuses outwards)? Since we observe the heat equation in everyday life, any reasonable model of atomistic behavior should have the heat equation as a natural limit.  

