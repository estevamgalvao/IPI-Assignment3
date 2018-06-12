# Assignment 3: Safe Landing Zone

Implementation of an image processing algorithm that helps a drone
to identify safe landing zones.

## Getting Started

Just run "Question1.py" and when the program asks for train and test images, you just put they adresses on it

### Prerequisites

External modules used:
 - Numpy
 - OpenCV2

### Results

         - CONFUSION MATRIX - 

Real           	Asphalt	Danger	Grass
Classified
Asphalt	        13	    3	    4
Danger	        4	    14	    5
Grass	        8	    8	    16

Precision: 0.57%

          - SAFETY MATRIX - 

Real           	Safe	Unsafe
Classified
Safe	        13	    7
Unsafe	        12	    43

F-Measure Safe: 0.58%
F-Measure Unsafe: 0.82%

The program took 0 hours, 3 minutes and 43 seconds to finish the classification

## Authors

* **Estevam Galvão Albuquerque**

## Main External References

* [K-nearest Neighbors](https://medium.com/@adi.bronshtein/a-quick-introduction-to-k-nearest-neighbors-algorithm-62214cea29c7)
* [Gustavo Monteiro Menezes - TCC](http://bdm.unb.br/handle/10483/15601)

## Acknowledgments

* Task proposed by professor: Alexandre Zaghetto - [zaghetto](https://github.com/zaghetto)

