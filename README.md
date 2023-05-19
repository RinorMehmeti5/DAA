                                              DIZAJNI DHE ANALIZA E ALGORITMEVE
✸ Në këtë projekt kemi dizajnuar një program Python që zgjidh problemin N-Queens duke përdorur një algoritëm rekurziv të backtracking variacioni Depth Limited Search (DLS) si dhe Forward Checking.

✸ Problemi N-Queens është një enigmë klasike ku qëllimi është vendosja e N mbretëreshave në një tabelë shahu NxN në mënyrë që asnjë mbretëreshë të mos kërcënojë njëra-tjetrën. Një mbretëreshë mund të sulmojë një mbretëreshë tjetër nëse ndajnë të njëjtin rresht, kolonë ose diagonale. 

                                                   INFORMACIONE RRETH PROGRAMIT
                                       
➢ Reth funksionit: `solve_n_queens(n, m, depth, MR)`

 `n`(int)      -  Madhësia e dimensionit të tabelës së shahut (nxn).
 
 `m`(int)      -  Numri i mbretëreshave për t'u vendosur në tabelë.
 
 `depth`(int)  -  The depth for Depth-Limited Search. Përcakton thellësinë maksimale të rekursionit.
 
 `MR`(str)     -  "po" për të përfshirë zgjidhjet e pasqyruara dhe të rrotulluara, "jo" ndryshe.
 
 ♦`RETURNS`♦
 `solutions` (list): Një listë me lista, ku secila nënlistë përfaqëson një zgjidhje të vlefshme për problemin N-Queens
 
 😀 `RUN PROGRAM` 😀 Download chess.py pastaj ne follderin e njejte run ne `console/terminal` • `py chess.py` •
