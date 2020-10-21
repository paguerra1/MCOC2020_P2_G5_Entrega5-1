# MCOC2020_P2_G5_Entrega5
# Entrega final, diseño de puente

# MCOC2020_P2_G5_Entrega5
# Diseño de puente, Entrega 5 MCOC 2020

# Primer diseño
*  Este fue el diseño inicial del puente 

![Captura de pantalla (14)](https://user-images.githubusercontent.com/69210578/96666144-e6680e80-132c-11eb-918f-273d92140641.png)

![Captura de pantalla (11)](https://user-images.githubusercontent.com/69210578/96666315-3d6de380-132d-11eb-96cf-475ef897f2ae.png)

* Imagen desde arriba:
![Captura de pantalla (12)](https://user-images.githubusercontent.com/69210578/96666138-e2d48780-132c-11eb-9fef-0625ebb6f6fc.png)

* Solo incluyendo lo presentado en las imágenes, sin columnas.
* Para las barras  en el eje x se utilizaron estas propiedades: props:  [8*cm, 5*mm, 200*GPa, 7600*kg/m**3, 420*MPa]
* Para las barras en relación al eje y,z se utilizaron estas propiedades: props2 = [11*cm, 14*mm, 200*GPa, 7600*kg/m**3, 420*MPa]

* Este diseño presentó algunos errores, donde no se cumplia con los requerimientos básicos de los factores de utilización, esbeltez menor a 300.
* Este diseño no cumplió con las combinaciones de cargas requeridas.
* Las barras que presentaron fallas en el diseño fueron las barras inferiores en el eje x e y. 
  


# Diseño final

* El nuevo diseño fue ejecutado de forma similar al anterior, pero esta vez con columnas, como se aprecia en la imagen.
* Para solucionar el problema anterior, se aumentaron las dimensiones de las barras en cuestión, para así aumentar la rigidez del elemento, cumpliendo finalmente con los dos requisitos.
* Cumpliendo con todos los requerimientos de factores de utilización
*  Las propiedades  de las barras  utilizadas fueron las siguientes:
* props = [8*cm, 5*mm, 200*GPa, 7600*kg/m**3, 420*MPa]
* props2 = [12*cm, 15*mm, 200*GPa, 7600*kg/m**3, 420*MPa] (eje x)
* props3 = [13*cm, 15*mm, 200*GPa, 7600*kg/m**3, 420*MPa] (eje y)
* El peso final del puente fue 511 toneladas
