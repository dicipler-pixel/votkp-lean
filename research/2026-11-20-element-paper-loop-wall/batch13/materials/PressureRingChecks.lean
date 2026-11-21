/- Exact discrete checks for the shortest-shell graph of Fddd origin choice 1, 8a.
   The input graph is justified independently from the refined crystal axes and boxes.
   Vertices are in signed integer quarter-cell coordinates. -/
namespace ElementPaper.FdddRings

structure V where
  x : Int
  y : Int
  z : Int
  deriving DecidableEq, BEq, Inhabited

def zero : V := ⟨0,0,0⟩
def plus (p q : V) : V := ⟨p.x+q.x,p.y+q.y,p.z+q.z⟩
def neg (p : V) : V := ⟨-p.x,-p.y,-p.z⟩
def minus (p q : V) : V := plus p (neg q)
def triple (a b c : V) : Int :=
  a.x*(b.y*c.z-b.z*c.y)+a.y*(b.z*c.x-b.x*c.z)+a.z*(b.x*c.y-b.y*c.x)
def bonds : List V := [⟨1,1,1⟩,⟨1,-1,-1⟩,⟨-1,1,-1⟩,⟨-1,-1,1⟩]

/-- Start by adding a bond from the origin. Neighbouring sublattices alternate sign.
    The reversed walk is stored current vertex first; a premature revisit is excluded. -/
def grow : Nat → Bool → List V → List (List V)
  | 0, add, path =>
    if bonds.any (fun b => plus path.head! (if add then b else neg b) == zero)
    then [path] else []
  | n+1, add, path =>
    bonds.flatMap fun b =>
      let next := plus path.head! (if add then b else neg b)
      if path.contains next then [] else grow n (!add) (next :: path)

def paths (n : Nat) := grow (n-1) true [zero]

/-- Fix a line of sight. Each other vertex must be strictly to the same side of
    every oriented projected edge. Signed areas are scalar triple products. -/
def sideTests (p : List V) (normal : V) : List Int :=
  (p.zip (p.tail ++ [p.head!])).flatMap fun (a,b) =>
    (p.filter (fun q => q != a && q != b)).map (fun q => triple normal (minus b a) (minus q a))

def hasConvexProjection (p : List V) : Bool :=
  bonds.any fun normal =>
    let determinants := sideTests p normal
    determinants.length==24 &&
      (determinants.all (fun d => decide (0<d)) || determinants.all (fun d => decide (d<0)))

set_option maxRecDepth 262144
set_option maxHeartbeats 10000000

theorem noShortRings : (paths 3).isEmpty ∧ (paths 4).isEmpty ∧ (paths 5).isEmpty := by decide +kernel
theorem bothOrientations : (paths 6).length = 24 := by decide +kernel
theorem allSixRingsProjectSimply : (paths 6).all hasConvexProjection = true := by decide +kernel

#print axioms noShortRings
#print axioms bothOrientations
#print axioms allSixRingsProjectSimply
end ElementPaper.FdddRings
