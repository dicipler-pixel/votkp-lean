# SCRIPT: TWIN-PAPER-BUILD-V2 — assemble twin_chain_v2.tex from v1 (v1 untouched) plus the new sections
import re
v1=open('twin_chain_v1.tex').read(); new=open('v2_new_sections.tex').read()
mk=open('v2_markov.tex').read() if __import__('os').path.exists('v2_markov.tex') else ''
new=new.replace('%MARKOV%',mk)
t=v1
def rep(a,b,count=1):
    global t
    assert t.count(a)>=1, a[:60]; t=t.replace(a,b,count)
rep(r'\large Endpoint Law, Frame Turn, and the Thread Cut by Every Prime}', r'\large Endpoint Law, Frame Turn, the Thread Cut by Every Prime,\\ and Where the Turn Is Set}')
rep(r'\date{24 November 2026}', r'\date{24 November 2026 \quad (version 2)}')
rep(r'that levels off near $0.13$.'+'\n'+r'\end{enumerate}',
 r'''that levels off near $0.13$.
\item \emph{Where the turn is set.} A curvature dial and its opposite setup show that the turn is set by the walk's first steps, not at the wall crossing. The wall reading is killed in both setups.
\item \emph{Other prime pairs.} Cousin and sexy primes, with one arm rule (the residue mod~$5$), share the slope $1/\sqrt3$ and the early wall crossing. The turn is not a Hardy--Littlewood quantity: twins and cousins share the constant but differ by $2.7^\circ$.
\item \emph{The dodecahedral honeycomb.} The twin arms are the edges of the $\{5,3,4\}$ honeycomb, whose edge has $\cosh\ell=\varphi$ and $\Gamma^2=\sqrt5-2$. Two perpendicular edges turn the frame by exactly $\arctan\tfrac12$. Walked on the honeycomb, the order of the twin end digits alone shows a prime signal at $z=-51$; about $16\%$ of it is memory beyond consecutive pairs.
\item \emph{Two predictions of version 1 settled.} The $7/9$ split offset and the cousin tilt both pass.
\item \emph{The 186 bound.} The main terms of OpenAI's certificate are confirmed independently. The gap $182$ is out of reach with their inputs.
\end{enumerate}''')
# reading section: carving comes early -> first cut
rep(r'  \item about $80\%$ of the turn exists by the wall crossing at twin starts $197$--$227$;',
    r'  \item about $80\%$ of the turn exists by twin start $227$, and Section~\ref{sec:firstcut} shows that the first steps do this carving, not the wall crossing;')
rep(r'\item \emph{In standard physics} \grade{cited}:', r'''\item \emph{Plato's triangles.} The exact numbers of this paper are the numbers of the \emph{Timaeus}. Its isosceles right triangle, $1:1:\sqrt2$, carries $1/\sqrt2$, the wall ($\Gamma^2=\tfrac12$). Its half-equilateral triangle, $1:\sqrt3:2$, carries $1/\sqrt3$, the endpoint slope. The dodecahedron, Plato's shape for the whole, carries $\sqrt5$: the honeycomb edge has $\cosh\ell=\varphi$, and two perpendicular edges turn by $\arctan\tfrac12$, the angle of the $1:2:\sqrt5$ triangle. The twins walk the cube, Plato's earth. These identities are exact. Any physical meaning is untested.
\item \emph{In standard physics} \grade{cited}:''')
# insert new sections before "The ruler"
rep(r'%=====================================================' + '\n' + r'\section{The ruler: stretching and compressing}', new+'\n'+r'%=====================================================' + '\n' + r'\section{The ruler: stretching and compressing}')
# predictions 6 and 7 settled
rep(r'\begin{prediction}[The split between digits 7 and 9]\label{pr:split} \grade{untested}', r'\begin{prediction}[The split between digits 7 and 9]\label{pr:split} \grade{settled in version 2: pass}')
rep(r"reproduces the walk's split, $+0.72$ and $+0.20$, rather than the prediction's $+0.81$ and $+0.14$."+'\n'+r'\end{prediction}',
 r'''reproduces the walk's split, $+0.72$ and $+0.20$, rather than the prediction's $+0.81$ and $+0.14$.

\emph{Result.} The direct gap-weighted count on $23{,}988{,}173$ twin starts in $(10^9,10^{10}]$, sieved for this test, gives $(-0.950,\ +0.775,\ +0.175)$, with block se $(0.032,0.033,0.036)$ and mean gap $375.2$. Against the prediction $(-0.945,+0.809,+0.136)$ the misses are $z=(-0.2,-1.0,+1.1)$. Digit~7 is closer to the prediction than to the walk, so the kill does not fire. The method was checked first on $(10^8,10^9]$, where it returns $(-0.924,+0.839,+0.085)$ exactly.
\end{prediction}''')
rep(r'\begin{prediction}[Cousin primes] \grade{untested}', r'\begin{prediction}[Cousin primes] \grade{settled in version 2: pass}')
rep(r'\emph{Kill} if digit-level agreement within $2$ se fails at $10^8$--$10^9$.'+'\n'+r'\end{prediction}',
 r'''\emph{Kill} if digit-level agreement within $2$ se fails at $10^8$--$10^9$.

\emph{Result.} Real cousins in $(10^8,10^9]$, classes $7,13,19$: $\mathrm{dev}\times G=(+0.680,\ +0.241,\ -0.921)$, block se $(0.072,0.081,0.092)$. The full product with $\{0,-4,h,h-4\}$ gives $(+0.705,\ +0.143,\ -0.847)$, so $z=(-0.3,+1.2,-0.8)$: \textbf{pass}. The same code reproduces the twin prediction $(-0.939,+0.820,+0.119)$ exactly. A caveat: the block se here is wider than the se used in version~1 (on twins, $0.068$ against $0.041$). Under the narrower kind of estimate, class $13$ would sit near $2$ se.
\end{prediction}''')
# new predictions before Position
rep(r'%=====================================================' + '\n' + r'\section{Position}', r'''\begin{prediction}[Honeycomb drift beyond $10^9$] \grade{untested}
On the $\{5,3,4\}$ honeycomb, the twin end-digit order keeps drifting more slowly than its shuffles in every later block of $10^6$ steps.
\emph{Kill} if a block of $10^6$ twin steps beyond $10^9$ has real drift within $2$ sd of its shuffles.
\end{prediction}

\begin{prediction}[Sexy-prime turn] \grade{untested}
The sexy-3 turn keeps climbing, by less each decade, and stays below the twin turn.
\emph{Kill} if its gain per decade grows over two consecutive decades beyond $10^9$, or it passes $12.27^\circ$ at $10^{10}$.
\end{prediction}

%=====================================================
\section{Position}''')
# figures
rep(r'\caption{Connection energy between the forward and reversed readings of the chain.}\label{fig:ce}\end{figure}',
 r'''\caption{Connection energy between the forward and reversed readings of the chain.}\label{fig:ce}\end{figure}

\begin{figure}[h!]\centering\includegraphics[width=0.98\textwidth]{fig/f9_first_cut.png}
\caption{The first cut. Left: turn runout from arm scrambles against the curvature dial. Right: before/after-wall ratio against where the wall sits.}\label{fig:firstcut}\end{figure}

\begin{figure}[h!]\centering\includegraphics[width=0.8\textwidth]{fig/f10_families.png}
\caption{The frame turn of each prime-pair family, by decade.}\label{fig:families}\end{figure}''')
# test register rows
rep(r'$\beta=\arccos(1/\sqrt3)$ & within $0.5^\circ$ & fails ($57.7^\circ$)\\',
 r'''$\beta=\arccos(1/\sqrt3)$ & within $0.5^\circ$ & fails ($57.7^\circ$)\\
\multicolumn{3}{l}{\emph{version 2}}\\
wall bite (scramble) & far runout $\ge\tfrac12$ first & pass (ratio $0.0004$)\\
curvature dial & before/after $<1.5$ wherever wall $>10^4$ & fires: wall is not the bite\\
opposite setup (late start) & before/after $<1.5$ at both starts & fires again ($0.52$, $1.30$)\\
families: slope & cousins, sexy-3 within $0.005$ of $1/\sqrt3$ & pass ($9\times10^{-5}$, $2.2\times10^{-3}$)\\
families: bounded $d$, octahedron & grows $<0.3$ & pass ($0.034$)\\
families: turn not HL & twins vs cousins differ $\ge0.3^\circ$ & pass ($2.72^\circ$)\\
families: wall crossing & $L^*\in[2.3,3.8]$ & pass for cube arms; octahedron never crosses\\
families: ordinary draw & $|z|\le3$ vs random arms & pass ($|z|\le1.49$)\\
honeycomb pentagon loop & closes, rotation $90^\circ$ & pass\\
honeycomb drift & within $2$ sd of shuffles & fires: signal at $z=-51$\\
%MKROW%
$7/9$ split (v1 Prediction 6) & direct count closer to walk & pass\\
cousin tilt (v1 Prediction 7) & within $2$ se & pass ($|z|\le1.2$)\\
186: $\mathrm{Kl}_3$ & $\le3$, $p\le160$ & pass ($2.665$)\\
186: correlation & $\le8p\sqrt p$, $p\le160$ & pass ($4.06$)\\
186: cap rebuild, $k=40$ & lands on their values & pass\\
186: $k=39$ best trial & quotient $\ge1$ & fails ($0.99439$)\\
186: recentering & any setting reaches $0.99871$ & fires: their setup is already centred\\''')
mkrow=open('v2_markov_row.tex').read() if __import__('os').path.exists('v2_markov_row.tex') else ''
t=t.replace('%MKROW%',mkrow)
rep(r'\item \texttt{paper/make\_figs.py}: every figure.',
 r'''\item \texttt{swarm/thread/} (version 2): \texttt{wall\_bite.py}, \texttt{curvature\_dial.py}, \texttt{curvature\_dial\_b.py}, \texttt{honeycomb\_534.py}, \texttt{honeycomb\_534\_markov.py}, \texttt{split\_and\_cousin.py}, with the conditions written before each run in \texttt{*\_PREREG.md}.
\item \texttt{swarm/families/}: \texttt{f1\_sieve.py}, \texttt{f2\_families.py}, \texttt{f3\_transitions.py}, \texttt{PREDICTION.txt}.
\item \texttt{gaps186/}: axiom checks, cap Gram rebuild, exact convolution, best trial, recentering scan.
\item \texttt{history/PRIMES\_HISTORY\_NOTES.md}: the history notes behind Appendix~C.
\item \texttt{paper/make\_figs.py}, \texttt{paper/make\_figs\_v2.py}: every figure.''')
# bibliography additions
rep(r'\end{thebibliography}', r'''\bibitem{OAI} OpenAI, Improved short gaps between primes, and Lean certificate, \texttt{github.com/openai/PrimeGaps186} (2026).
\bibitem{Stad} J.~Stadlmann, Bounded gaps between primes, arXiv:2608.31126.
\bibitem{May} J.~Maynard, Small gaps between primes, \emph{Ann. of Math.} 181 (2015).
\bibitem{Poly} D.~H.~J.~Polymath, Variants of the Selberg sieve, and bounded intervals containing many primes, \emph{Res. Math. Sci.} 1 (2014).
\bibitem{FKM} \'E.~Fouvry, E.~Kowalski and Ph.~Michel, Algebraic trace functions over the primes, arXiv:1207.0617.
\bibitem{Cox} H.~S.~M.~Coxeter, \emph{Regular Honeycombs in Hyperbolic Space}, Proc. ICM Amsterdam (1954); \emph{Regular Polytopes}, Dover, 1973.
\bibitem{Sutherland} A.~V.~Sutherland, narrow admissible tuples, OEIS A008407.
\end{thebibliography}''')
# history appendix before thebibliography
rep(r'\begin{thebibliography}{99}\small', r'''\section{How the primes were found: a short record}
These are background notes, kept to dated records; disputed readings are marked. The full notes, with sources, are in \texttt{history/PRIMES\_HISTORY\_NOTES.md}.
\begin{itemize}
\item Old Babylonian reciprocal tables (about 1800 BCE) list only numbers built from $2,3,5$; $7$ is marked as having no reciprocal. The first written prime arithmetic is the wheel $2\cdot3\cdot5=30$, the same wheel the twin classes $11,17,29\pmod{30}$ come from, with $7$ the first number left out. In Section~\ref{sec:thread}, cutting the thread by $7$ is what gives the tilt its real sign.
\item Ishango bone (about 20{,}000 years ago): one column reads $11,13,17,19$. Whether that is deliberate is disputed.
\item Euclid, \emph{Elements} VII.31--32, IX.20, IX.36 (about 300 BCE); Eratosthenes' sieve (about 240 BCE).
\item Sunzi (3rd--5th century) and Qin Jiushao (1247): the remainder theorem, which is how the mod-30 wheel is assembled.
\item Aryabhata (499) and Brahmagupta (628): linear congruences.
\item Euler (1737): the product over all primes, the shape of the every-prime cut of Section~\ref{sec:thread}.
\item Polignac (1849): every even gap occurs infinitely often.
\item Brun (1919): the twin reciprocals converge, the same reason the chain's turn converges.
\item Hardy and Littlewood (1923): the local factors used for the tilt.
\item Zhang (2013); Maynard, Tao and Polymath (2014): bounded gaps, $246$.
\item Lemke Oliver and Soundararajan (2016): consecutive-prime end-digit bias.
\item Stadlmann (2026): $240$; Axiom Math: $212$ (claimed); OpenAI: $186$ (conditional on three stated assumptions; Section~\ref{sec:186}). Gap $2$ is still open.
\end{itemize}

\begin{thebibliography}{99}\small''')
open('twin_chain_v2.tex','w').write(t); print('written',len(t))
