# Python Library myConvexHull

### Pemanfaatan algortima divide and conquer untuk pembuatan library myConvexHull untuk Linear Separability Dataset Test.
#### Program dalam folder src terdiri dari file main.py yang berisi program untuk me-load data set dan melakukan visualisasi dari convex hull dari pasangan aribut pada data set yang digunakan
#### Pada myConvexHull.py berisi implementasi library myConvexHull dengan algortima divide and conquer yang diterapkan dengan menggunakan metode rekursif

# Author

| NIM      | NAME                     |
|----------|--------------------------|
| 13520141 | Yoseph Alexander Siregar |

# Dataset dan perbandingan atribut dalam program
1. Iris
  * Sepal Width vs Sepal Length
  * Petal Width vs Petal Length
2. Wine
  * Alcohol vs Malic_acid
  * Malic_acid vs Ash
3. Breast Cancer
  * Radius vs Texture
  * Texture vs Perimeter

# Requirement
Requirement untuk menjalankan program
* Environment python
* numpy package
* matplotlib package
* pandas package
* sklearn package

# Directory
```sh
LSD_TestvVisualisation-ConvexHull
├── src                     # Berisi source kode program
│   ├── main.py             # Main program
│   ├── myConvexHull.py     # Implementasi myConvexHull
├── doc                     # Berisi laporan
```

# How To Run
1. Clone repository ini : `https://github.com/yosalx/LSD_TestVisualisation-ConvexHull`
2. Install seluruh package pada requirement : `pip/pip3 install <package_name>`
3. Buka terminal dan ubah path menuju folder src : `cd LSD_TestVisualisation-ConvexHull/src pada terminal `
4. Jalankan `py main.py` atau `python main.py` atau `python3 main.py` pada terminal
5. Program sudah berjalan, apabila saat ingin melakukan run kembali dan dirasa lama muncul meminta input (awal program), silahkan hapus atau kill terminal dan jalankan kembali program
