# Published element representation for the nearest-neighbour control

The frozen reference is the 200-coordinate mat2vec input embedding distributed with CrabNet. The distance is one minus the cosine between two element vectors. This metric and the choice of embedding were specified before reading its benchmark score. We applied no column scaling, feature selection, supervised fitting or imputation. The symbol is a lookup key. All 77 eligible symbols F through At have distinct, finite, nonzero vectors.

Tshitoyan and colleagues trained word embeddings on scientific abstracts. Element vectors can therefore encode periodic relationships and chemical knowledge already present in the literature. They provide a published comparison for reconstructing known columns. They do not constitute a blind test of an undiscovered column or an independent wall measurement. The paper distinguishes this source from Jeromie's nine input ionization thresholds per element. [Tshitoyan et al., Nature (2019)](https://doi.org/10.1038/s41586-019-1335-8) · [Wang et al., npj Computational Materials (2021)](https://doi.org/10.1038/s41524-021-00545-1)

## Data and checks

- Full CSV, 118 symbols, SHA-256 `5dcde1a0fe13040af99dbcb7b3d73eb022ffd085e7f598dce70844d0af83b137`. CrabNet and CBFV distribute byte-identical copies. [Pinned CrabNet data](https://github.com/anthony-wang/CrabNet/blob/457b4d4835737ecbe4dd33e53174bd818bd82143/data/element_properties/mat2vec.csv) · [Pinned CBFV data](https://github.com/kaaiian/CBFV/blob/0b6be45db0b96374899a3aa77f11ff7764a7dfa4/cbfv/element_properties/mat2vec.csv)
- Extracted CSV, 77 symbols and 200 coordinates, SHA-256 `0e373f15ce32d0a730c836ea2791e407885b202053bbb296a97a716a5eee5b20`. Extraction preserves the published decimal strings and the peel census order. Original coordinate headers 0 through 199 are renamed f001 through f200.
- The original project and CrabNet supply MIT notices. Copies are preserved alongside these data. [Original project notice](https://github.com/materialsintelligence/mat2vec/blob/7ca8961c09ad9995694a41edfd80da6c4ac7e307/LICENSE) · [CrabNet notice](https://github.com/anthony-wang/CrabNet/blob/457b4d4835737ecbe4dd33e53174bd818bd82143/LICENSE.md)

The benchmark runs offline with the included CSV. To recreate it independently, run from this directory:

```sh
curl -fsSL https://raw.githubusercontent.com/anthony-wang/CrabNet/457b4d4835737ecbe4dd33e53174bd818bd82143/data/element_properties/mat2vec.csv -o /tmp/crabnet_mat2vec.csv
python3 extract_mat2vec.py /tmp/crabnet_mat2vec.csv
sha256sum published_features.csv
```
