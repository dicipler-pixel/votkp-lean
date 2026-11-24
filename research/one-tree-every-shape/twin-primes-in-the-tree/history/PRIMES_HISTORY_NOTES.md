# How the primes were found: oldest to newest, worldwide (research notes, 24 Nov 2026)

Jeromie Beasley · notes

Grades:
- **record**: a dated document or artifact.
- **attributed**: credited to a person, but the dating or source is indirect.
- **claim**: an interpretation that is disputed.

## Africa and the Near East
- **Ishango bone** (DR Congo; found by J. de Heinzelin, 1950; site dated about 20,000 years ago, and the dating is debated). One column of marks reads 11, 13, 17, 19, the primes between 10 and 20. **Claim**: disputed by Rudman, by Huylebrouck and Pletser, by Keller, and by Joseph, who calls it "suggestive but not conclusive".
- **Old Babylonian reciprocal tables** (about 1800 BCE). The tables list only the regular numbers 2^a·3^b·5^c, which have finite reciprocals in base 60. A number such as 7 or 11 is marked as having no reciprocal ("igi nu"). So the primes 2, 3 and 5 are the scribes' own wheel, and 7 is the first number left outside it. **Record**.
- **Rhind papyrus 2/n table** (Egypt, about 1650 BCE). Its decompositions treat prime denominators differently from composite ones. **Record**; reading it as a deliberate prime-versus-composite rule is a **claim**.

## Greece
- **Pythagoreans** (about 500–300 BCE): primes studied alongside perfect and amicable numbers. **Attributed**.
- **Euclid, *Elements*** (about 300 BCE):
  - VII.31–32: every number has a prime divisor;
  - IX.14: the start of unique factorisation;
  - IX.20: there are infinitely many primes;
  - IX.36: even perfect numbers come from primes of the form 2^p − 1.

  **Record**.
- **Eratosthenes' sieve** (about 240 BCE), preserved by Nicomachus (about 100 CE). **Attributed**.

## China
- ***Nine Chapters***, chapter 1: a gcd algorithm that is essentially Euclid's algorithm or the binary gcd. **Record**.
- **Sunzi** (3rd–5th century CE): the remainder theorem. **Record**.
- **Qin Jiushao** (1247): general remainder method. **Record**.
- **Primes in Confucius' time** (about 500 BCE): argued by S. Zhang, arXiv:0910.0095. **Claim**.
- **"Chinese hypothesis"** (2^n ≡ 2 mod n): traced to a 19th-century misreading. **Claim**, generally treated as a myth.

## India
- **Aryabhata** (499) and **Brahmagupta** (628): kuttaka, the solution of linear congruences. **Record**.
- **Ramanujan** (1919): a short proof of Bertrand's postulate, the origin of "Ramanujan primes". **Record**.
- **Agrawal, Kayal and Saxena** (IIT Kanpur, 2002): primality can be tested in polynomial time (AKS, "PRIMES is in P"). **Record**.

## Islamic world
- **Thabit ibn Qurra** (9th century): a rule that builds amicable pairs from primes. **Record**.
- **Ibn al-Haytham** (about 1000): the property that (p − 1)! + 1 is divisible by p, later called Wilson's theorem. **Attributed**.
- **Kamal al-Din al-Farisi** (about 1300): an early treatment of unique factorisation. **Attributed**.

## Europe, 1202–1900 (records)
- Fibonacci, *Liber Abaci* (1202).
- Cataldi (1588): showed M17 and M19 are prime; M19 stayed the largest known prime for 184 years.
- Fermat (1640): little theorem; Fermat numbers.
- Mersenne (1644).
- Goldbach to Euler (1742).
- Euler:
  - 1737: the prime product formula, and the sum of 1/p diverges;
  - 1732: F5 = 641 × 6700417;
  - 1772: M31 is prime.
- Legendre (1798) and Gauss (1792, letter of 1849): estimates of π(x).
- Dirichlet (1837): infinitely many primes in every coprime arithmetic progression.
- Polignac (1849): every even gap occurs infinitely often, including the twin-prime case.
- Chebyshev (1848–1852): bounds on π(x); proof of Bertrand's postulate.
- Riemann (1859).
- Lucas (1876): M127 is prime.
- Hadamard and de la Vallée Poussin (1896): the prime number theorem.

## 20th century (records)
- Brun (Norway, 1915–1919): the sieve; the sum of reciprocals of twin primes converges.
- Hardy and Littlewood (1923): the prime-tuple constants.
- Vinogradov (USSR, 1937): every large odd number is a sum of three primes.
- Selberg (Norway) and Erdős (Hungary), 1948–49: an elementary proof of the prime number theorem.
- Robinson (1952): first Mersenne primes found by computer.
- Bombieri–Vinogradov theorem (1965).
- Chen Jingrun (China, 1966/1973): every large even number is p + P2.
- GIMPS (1996).

## 21st century (records)
- Green and Tao (2004): arbitrarily long arithmetic progressions of primes.
- Zhang (2013): bounded gaps, under 70 million.
- Maynard and Tao (2013); Polymath (2014): bound 246.
- Helfgott (2013): ternary Goldbach.
- Lemke Oliver and Soundararajan (2016): biases in the end digits of consecutive primes.
- Largest known twin primes:
  - 2996863034895·2^1290000 ± 1 (September 2016; 388,342 digits);
  - third largest, 152748736824915·2^480480 ± 1 (January 2026).
- Guth and Maynard (2024): a new zero-density bound.
- Green and Sawhney (2024): infinitely many primes p² + 4q² with p and q prime.
- Durant (October 2024): M136279841, 41,024,320 digits, the first record found on GPUs; still the largest known prime.
- Stadlmann (arXiv:2608.31126, 31 August 2026): bounded gap 240.
- Axiom Math: 212 (claimed). OpenAI "GPT-6 Astra": 186. Paper dated 30 August 2026, announced 3 September; Lean formalisation is conditional and unreviewed.
- OpenAI quasi-Riemann hypothesis (October 2026): all zeros have real part in [1/12, 11/12]. Experts largely agree it is correct; not yet published.

## Links to the twin chain (from this session's results)
- **The Babylonian wheel is the twin screw's turn.** 2·3·5 = 30 are exactly the scribes' regular primes, and the twin classes 11, 17, 29 mod 30 come from those three. The prime 7, the first number left outside the wheel, is the cut that sets the sign of the end-digit tilt.
- **Euclid's algorithm and the Chinese gcd** are the frame-free form's ancestors: the remainders walk on their own.
- **Euler's product over all primes** is the shape of the every-prime thread (Hardy–Littlewood local factors).
- **Brun's convergent twin sum (1919)** is the model for the convergent frame turn.
- **Polignac (1849)** set the gap question; Stadlmann, Axiom and OpenAI moved its bound in 2026.
- **Lemke Oliver–Soundararajan** is the family the all-primes end-digit tilt belongs to.
